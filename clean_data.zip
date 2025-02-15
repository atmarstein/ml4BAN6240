import pandas as pd

# Load the dataset
df = pd.read_csv("Netflix_shows_movies.csv")

# Check for missing values
missing_values = df.isnull().sum()
print("Missing Values in Each Column:\n", missing_values)

# Fill missing values with appropriate values (e.g., empty string for text, median for numbers)
df.fillna("Unknown", inplace=True)

# Save cleaned data
df.to_csv("Netflix_shows_movies_cleaned.csv", index=False)
print("Missing values handled and dataset saved as Netflix_shows_movies_cleaned.csv")
