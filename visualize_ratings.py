import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("Netflix_shows_movies_cleaned.csv")

# Plot ratings distribution
plt.figure(figsize=(10, 5))
df['rating'].value_counts().plot(kind='bar', color='red')
plt.title("Ratings Distribution")
plt.xlabel("Ratings")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()
