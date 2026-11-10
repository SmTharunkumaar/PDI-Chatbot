
import pandas as pd
from pathlib import Path

project_folder = Path(__file__).parent.parent
excel_file_path = project_folder / "data" / "manufacturing_dataset.xlsx"


def load_excel_data():

    if not excel_file_path.exists():
        print("Manufacturing dataset not found!")
        return []

    excel_file = pd.ExcelFile(excel_file_path)
    manufacturing_documents = []

    print("\nReading manufacturing dataset...")
    print("=" * 50)

    for sheet_name in excel_file.sheet_names:

        sheet_data = pd.read_excel(
            excel_file_path,
            sheet_name=sheet_name
        )

        sheet_data = sheet_data.fillna("Not specified")

        print(sheet_name, ":", len(sheet_data), "records")

        for record_number, row in sheet_data.iterrows():

            document_content = "\n".join(
                f"{column_name}: {value}"
                for column_name, value in row.items()
            )

            document_metadata = {
                "source_sheet": str(sheet_name),
                "record_index": int(record_number)
            }

            for column_name, value in row.items():

                metadata_name = str(column_name).lower().strip()

                if metadata_name in [
                    "plant_id",
                    "plant_name",
                    "model_id",
                    "model_name",
                    "shop_id",
                    "shop_name",
                    "line_id",
                    "line_name",
                    "station_id",
                    "station_name",
                    "station_sequence",
                    "checkpoint_id",
                    "checkpoint_name",
                    "sequence_no",
                    "defect_id",
                    "defect_name"
                ]:

                    if value != "Not specified":
                        document_metadata[metadata_name] = str(value)

            manufacturing_documents.append({
                "content": f"Sheet: {sheet_name}\n{document_content}",
                "metadata": document_metadata
            })

    print("=" * 50)
    print("Total documents prepared:", len(manufacturing_documents))

    return manufacturing_documents


if __name__ == "__main__":

    documents = load_excel_data()

    if documents:
        print("\nFirst document:")
        print(documents[0]["content"])

    print("\nDocument preparation completed!")
