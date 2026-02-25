import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cafes_cleaned.csv")

print("Dataset loaded successfully!\n")

# Preview data
print("First 5 rows:")
print(df.head())

# --- DATA OVERVIEW ---
print("\nDataset shape (rows, columns):")
print(df.shape)

print("\nColumn types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nBasic statistics:")
print(df.describe())

# --- ANALYSIS ---
print("\nNumber of cafés per district:")
print(df['district'].value_counts())

print("\nAverage rating per district:")
print(df.groupby('district')['rating'].mean().sort_values(ascending=False))

print("\nAverage review count per district:")
print(df.groupby('district')['review_count'].mean().sort_values(ascending=False))