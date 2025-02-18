import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv('Netflix_shows_movies_cleaned.csv') 

# Check column names
print(df.columns)

# Ensure 'listed_in' exists in the cleaned dataset
if 'listed_in' in df.columns:
    # Split multiple categories and count occurrences
    categories = df['listed_in'].str.split(', ').explode()
    
    # Visualize the top 10 categories
    categories.value_counts().head(10).plot(kind='bar', color='blue')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.title('Top 10 Netflix Categories')
    plt.xticks(rotation=45)
    plt.show()
else:
    print("Error: 'listed_in' column not found in cleaned dataset.")
