import os

old_name = "netflix_data.csv"
new_name = "Netflix_shows_movies.csv"

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print(f"File renamed to {new_name}")
else:
    print("File not found. Ensure the file is in the correct directory.")
