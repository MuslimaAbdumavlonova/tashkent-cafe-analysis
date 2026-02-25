import pandas as pd

# Load the dataset
df = pd.read_excel("data/data.xlsx")

# Preview data
print("First 5 rows:")
print(df.head())

# Dataset info
print("\nDataset Info:")
df.info()

# Clean column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nCleaned Columns:")
print(df.columns)

# Save cleaned dataset
df.to_csv("data/cafes_cleaned.csv", index=False)

print("\nClean dataset saved successfully.")