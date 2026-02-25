import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv("data/cafes_cleaned.csv")

# --- 1. Ratings distribution ---
plt.figure(figsize=(8,5))
sns.histplot(df["rating"], bins=10, kde=True)
plt.title("Distribution of Café Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Cafés")
plt.tight_layout()
plt.show()

# --- 2. Average reviews by district ---
avg_reviews = df.groupby("district")["review_count"].mean().reset_index()

plt.figure(figsize=(8,5))
sns.barplot(x="district", y="review_count", data=avg_reviews)
plt.title("Average Reviews per District")
plt.xlabel("District")
plt.ylabel("Average Number of Reviews")
plt.tight_layout()
plt.show()

# --- 3. Price level vs rating ---
plt.figure(figsize=(8,5))
sns.boxplot(x="price_level", y="rating", data=df)
plt.title("Rating Distribution by Price Level")
plt.xlabel("Price Level")
plt.ylabel("Rating")
plt.tight_layout()
plt.show()