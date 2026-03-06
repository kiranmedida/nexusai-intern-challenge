import asyncpg
from typing import List, Dict


class CallRecordRepository:

    def __init__(self, db_url: str):
        self.db_url = db_url


    async def save(self, call_data: dict):

        conn = await asyncpg.connect(self.db_url)

        query = """
        INSERT INTO call_records(
            customer_phone,
            channel,
            transcript,
            ai_response,
            outcome,
            confidence_score,
            csat_score,
            duration
        )
        VALUES($1,$2,$3,$4,$5,$6,$7,$8)
        """

        await conn.execute(
            query,
            call_data["customer_phone"],
            call_data["channel"],
            call_data["transcript"],
            call_data["ai_response"],
            call_data["outcome"],
            call_data["confidence_score"],
            call_data.get("csat_score"),
            call_data["duration"]
        )

        await conn.close()


    async def get_recent(self, phone: str, limit: int = 5) -> List[Dict]:

        conn = await asyncpg.connect(self.db_url)

        query = """
        SELECT *
        FROM call_records
        WHERE customer_phone = $1
        ORDER BY timestamp DESC
        LIMIT $2
        """

        rows = await conn.fetch(query, phone, limit)

        await conn.close()

        return [dict(row) for row in rows]


async def lowest_resolution_intents(db_url: str):

    conn = await asyncpg.connect(db_url)

    query = """
    SELECT
        transcript AS intent,
        AVG(CASE WHEN outcome = 'resolved' THEN 1 ELSE 0 END) AS resolution_rate,
        AVG(csat_score) AS avg_csat
    FROM call_records
    WHERE timestamp >= NOW() - INTERVAL '7 days'
    GROUP BY intent
    ORDER BY resolution_rate ASC
    LIMIT 5
    """

    rows = await conn.fetch(query)

    await conn.close()

    return [dict(row) for row in rows]