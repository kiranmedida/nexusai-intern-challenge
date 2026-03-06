CREATE TABLE call_records (
    id SERIAL PRIMARY KEY,

    customer_phone VARCHAR(15) NOT NULL,

    channel TEXT NOT NULL CHECK (
        channel IN ('voice','whatsapp','chat')
    ),

    transcript TEXT NOT NULL,

    ai_response TEXT NOT NULL,

    outcome TEXT NOT NULL CHECK (
        outcome IN ('resolved','escalated','failed')
    ),

    confidence_score REAL NOT NULL CHECK (
        confidence_score >= 0 AND confidence_score <= 1
    ),

    csat_score SMALLINT CHECK (
        csat_score BETWEEN 1 AND 5
    ),

    timestamp TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,

    duration_seconds INTEGER NOT NULL
);