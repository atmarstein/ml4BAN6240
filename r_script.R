library(ggplot2)

# Load the dataset
df <- read.csv("Netflix_shows_movies_cleaned.csv")

# Create a bar plot for ratings distribution
ggplot(df, aes(x=rating)) +
  geom_bar(fill="red") +
  ggtitle("Ratings Distribution") +
  xlab("Ratings") +
  ylab("Count") +
  theme(axis.text.x = element_text(angle=45, hjust=1))

