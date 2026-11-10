@'
from pathlib import Path
from langchain_chroma import Chroma

project_folder = Path(__file__).parent.parent
database_folder = project_folder / "data" / "chroma_db"
collection_name = "pdi_manufacturing_knowledge"


def get_vector_database():
    return Chroma(
        collection_name=collection_name,
        persist_directory=str(database_folder)
    )


def search_manufacturing_information(question, number_of_results=5, source_sheet=None):
    vector_database = get_vector_database()

    search_filter = None

    if source_sheet:
        search_filter = {"source_sheet": source_sheet}

    return vector_database.similarity_search(
        query=question,
        k=number_of_results,
        filter=search_filter
    )


def search_station_information(question, number_of_results=5):
    return search_manufacturing_information(
        question=question,
        number_of_results=number_of_results,
        source_sheet="station_technical_reference"
    )


def search_checkpoint_information(question, number_of_results=5):
    return search_manufacturing_information(
        question=question,
        number_of_results=number_of_results,
        source_sheet="checkpoints"
    )


if __name__ == "__main__":
    print("PDI MANUFACTURING KNOWLEDGE RETRIEVAL")

    question = input("\nEnter your manufacturing question: ")
    results = search_station_information(question)

    print("\nSTATION INFORMATION")
    print("=" * 50)

    if not results:
        print("No relevant station information found.")

    for number, document in enumerate(results, start=1):
        print(f"\nResult {number}")
        print(document.page_content)
        print("Source:", document.metadata.get("source_sheet"))

    print("\nSearch completed!")
'@ | Set-Content -Encoding UTF8 .\agents\retrieval.py