
import pandas as pd
from pathlib import Path

file_path = Path(__file__).parent.parent / "data" / "manufacturing_dataset.xlsx"

if not file_path.exists():
    print("Manufacturing dataset not found!")
    exit()

excel_file = pd.ExcelFile(file_path)

print("\nMANUFACTURING DATASET INSPECTION")
print("=" * 50)

print("Total sheets:", len(excel_file.sheet_names))

for sheet_name in excel_file.sheet_names:

    data = pd.read_excel(file_path, sheet_name=sheet_name)

    print("\nSheet name:", sheet_name)
    print("Total records:", len(data))
    print("Total columns:", len(data.columns))
    print("Column names:", list(data.columns))

    print("\nFirst 3 records:")
    print(data.head(3).to_string(index=False))

print("\nDataset inspection completed!")
