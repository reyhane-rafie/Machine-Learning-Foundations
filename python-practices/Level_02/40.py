# 40. Research Paper Tracker
# Store papers you've read.
# Columns
# Title
# Year
# Journal
# Topic
# Rating
# Allow
#     • Search
#     • Filter
#     • Highest-rated papers
# Practice
#     • Pandas
#     • filtering
# ------------------------------

import pandas as pd

# Load the data
papers = pd.read_csv("papers.csv")

print("\n--- Research Paper Tracker ---")

# Show all papers
print("\nAll Papers:")
print(papers)


# Search papers by title
keyword = input("\nEnter search keyword: ")

search_results = papers[
    papers["Title"].str.contains(keyword, case=False, na=False)
]

print("\n--- Search Results ---")
print(search_results)


# Filter papers by topic
topic = input("\nEnter topic to filter: ")

topic_results = papers[
    papers["Topic"].str.lower() == topic.lower()
]

print("\n--- Topic Results ---")
print(topic_results)


# Find highest-rated papers
highest_rating = papers["Rating"].max()

highest_rated = papers[
    papers["Rating"] == highest_rating
]

print("\n--- Highest-Rated Papers ---")
print("Highest Rating:", highest_rating)
print(highest_rated)