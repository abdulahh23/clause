from app.services.chat import RAGService

def main() -> None:
    rag_services = RAGService()
    try:
        query = input("You: ").strip()
        result = rag_services.ask(question=query)
        print(f"AI: {result.answer}")
    except:
        pass
    finally:
        rag_services.close()

if __name__ == "__main__":
    main()

    #cd api
    #uv run python -m app.cli