from rag_system import build_rag

qa = build_rag()

print("Hellobooks AI Assistant")
print("Ask accounting questions (type 'exit' to quit)\n")

while True:
    question = input("Question: ")

    if question.lower() == "exit":
        break

    answer = qa.run(question)

    print("\nAnswer:", answer)
    print()