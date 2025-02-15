import pandas as pd

# Load cleaned dataset
df = pd.read_csv("Netflix_shows_movies_cleaned.csv")

# Display basic information
print("Dataset Info:\n")
print(df.info())

# Summary statistics
print("\nSummary Statistics:\n")
print(df.describe(include='all'))

# Check unique values in key columns
print("\nUnique Ratings:\n", df['rating'].unique())
print("\nUnique Genres:\n", df['listed_in'].unique())

