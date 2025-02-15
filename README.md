# Netflix Data Visualization

## Overview

This project analyzes Netflix data to provide insights into the most-watched categories and ratings distribution using Python and R. It includes data cleaning, exploration, and visualization tasks.

## Project Structure

The project includes the following files:

- **netflix_shows_movies** - Uncleaned dataset
- **rename_file.py** – Script for renaming and organizing files.
- **clean_data.py** – Script for cleaning the Netflix dataset.
- **explore_data.py** – Script for exploring key aspects of the dataset.
- **visualize_genres.py** – Script for visualizing the most popular genres based on the `listed_in` column.
- **visualize_ratings.py** – Script for visualizing the distribution of ratings.
- **r_script.R** – R script for generating a ratings distribution chart.
- **Netflix_shows_movies_cleaned.csv** – Cleaned dataset used for analysis.
- **README.md** – Instructions for running the project.

## Steps to Run the Project

### Using Python

1. Install dependencies if not already installed:
   ```bash
   pip install pandas seaborn matplotlib
   ```
2. Run the Python scripts in the following order:
   ```bash
   python clean_data.py
   python explore_data.py
   python visualize_genres.py
   python visualize_ratings.py
   ```
3. The scripts will load `Netflix_shows_movies_cleaned.csv`, perform exploratory analysis, and generate visualizations.

### Using R (RStudio)

1. Open `r_script.R` in RStudio.
2. Ensure you have `ggplot2` installed:
   ```r
   install.packages("ggplot2")
   ```
3. Run the script to generate the ratings distribution chart using `Netflix_shows_movies_cleaned.csv`.

## Example Outputs

- **Most Watched Categories**: A bar chart displaying the most frequently watched categories using the `listed_in` column.
- **Ratings Distribution**: A histogram showing the distribution of ratings.
