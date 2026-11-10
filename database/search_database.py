
print("PDI CHATBOT SEARCH STARTED!")

from pathlib import Path
from langchain_chroma import Chroma

project_folder = Path(__file__).parent.parent
database_folder = project_folder / "data" / "chroma_db"

print("Connecting to ChromaDB...")

vector_database = Chroma(
    collection_name="pdi_manufacturing_knowledge",
    persist_directory=str(database_folder)
)

print("Connected to ChromaDB successfully!")

search_question = input("\nEnter your manufacturing question: ")

search_results = vector_database.similarity_search(
    search_question,
    k=5
)

print("\nSEARCH RESULTS")
print("=" * 50)

if not search_results:
    print("No matching information found.")

for number, document in enumerate(search_results, start=1):
    print(f"\nResult {number}")
    print(document.page_content)
    print("Source:", document.metadata.get("source_sheet"))

print("\nSearch completed!")
