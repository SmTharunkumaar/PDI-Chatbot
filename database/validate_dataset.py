
import pandas as pd
from pathlib import Path

file_path = Path(__file__).parent.parent / "data" / "manufacturing_dataset.xlsx"

if not file_path.exists():
    print("Manufacturing dataset not found!")
    exit()

excel_file = pd.ExcelFile(file_path)

print("\nMANUFACTURING DATASET VALIDATION")
print("=" * 50)

for sheet_name in excel_file.sheet_names:

    data = pd.read_excel(file_path, sheet_name=sheet_name)

    duplicate_rows = data.duplicated().sum()
    missing_values = data.isnull().sum().sum()

    print("\nSheet name:", sheet_name)
    print("Total records:", len(data))
    print("Duplicate rows:", duplicate_rows)
    print("Missing values:", missing_values)

    if duplicate_rows == 0 and missing_values == 0:
        print("Status: Data looks good")
    else:
        print("Status: Needs checking")

print("\nDataset validation completed!")
