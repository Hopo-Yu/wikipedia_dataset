from src.wikipedia_fetcher.langchain_wikipedia import fetch_via_langchain
from src.wikipedia_fetcher.wikipedia_api_wrapper import fetch_via_wrapper
from src.chatgpt_processor.chatgpt_analyzer import analyze_with_chatgpt


def main():
    # For demonstration purposes:
    query = "History of France from 1900-2000"

    # Fetch data via LangChain
    context_text_langchain = fetch_via_langchain(query)

    print(context_text_langchain)
    # Or fetch data via Wikipedia API wrapper
    # context_text_wrapper = fetch_via_wrapper(query)

    # Analyze with ChatGPT
    # result = analyze_with_chatgpt(query, context_text_langchain)

    # Print the result
    # print(result)


if __name__ == "__main__":
    main()
