
from langchain_core.tools import tool

from retrieval import search_manufacturing_information


@tool
def search_manufacturing_data(question: str) -> str:
    """Search the manufacturing knowledge database for relevant information."""

    results = search_manufacturing_information(question)

    if not results:
        return "No relevant manufacturing information found."

    answer = []

    for number, document in enumerate(results, start=1):
        answer.append(
            f"Result {number}:\n{document.page_content}"
        )

    return "\n\n".join(answer)


@tool
def find_station_information(station_name: str) -> str:
    """Find manufacturing information about a particular station."""

    results = search_manufacturing_information(
        f"Station name: {station_name}"
    )

    if not results:
        return "No station information found."

    return "\n\n".join(
        document.page_content for document in results
    )


@tool
def find_checkpoint_information(checkpoint_name: str) -> str:
    """Find inspection checkpoint information."""

    results = search_manufacturing_information(
        f"Checkpoint name: {checkpoint_name}"
    )

    if not results:
        return "No checkpoint information found."

    return "\n\n".join(
        document.page_content for document in results
    )


manufacturing_tools = [
    search_manufacturing_data,
    find_station_information,
    find_checkpoint_information
]


if __name__ == "__main__":

    question = input("Enter your manufacturing question: ")

    result = search_manufacturing_data.invoke({
        "question": question
    })

    print("\nMANUFACTURING INFORMATION")
    print("=" * 50)
    print(result)
