
from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document

from excel_to_documents import load_excel_data


project_folder = Path(__file__).parent.parent
database_folder = project_folder / "data" / "chroma_db"

collection_name = "pdi_manufacturing_knowledge"
batch_size = 500


def create_vector_database():

    print("\nCreating manufacturing vector database...")

    manufacturing_records = load_excel_data()

    if not manufacturing_records:
        print("No manufacturing records found!")
        return

    manufacturing_documents = []
    document_ids = []

    for record in manufacturing_records:

        document = Document(
            page_content=record["content"],
            metadata=record["metadata"]
        )

        manufacturing_documents.append(document)

        document_id = (
            f'{record["metadata"]["source_sheet"]}_'
            f'{record["metadata"]["record_index"]}'
        )

        document_ids.append(document_id)

    vector_database = Chroma(
        collection_name=collection_name,
        persist_directory=str(database_folder)
    )

    total_documents = len(manufacturing_documents)

    for start in range(0, total_documents, batch_size):

        end = start + batch_size

        document_batch = manufacturing_documents[start:end]
        id_batch = document_ids[start:end]

        vector_database.add_documents(
            documents=document_batch,
            ids=id_batch
        )

        print(f"Stored {min(end, total_documents)} of {total_documents} documents")

    print("\nVector database created successfully!")
    print("Total documents stored:", total_documents)
    print("Database location:", database_folder)


if __name__ == "__main__":
    create_vector_database()
