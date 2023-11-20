# # import os
# # os.environ['OBJC_DISABLE_INITIALIZE_FORK_SAFETY'] = 'YES'
#
# import matplotlib
# matplotlib.use("TkAgg")  # Use the TkAgg backend

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'movies_metadata.csv'
dtype_options = {'original_language': str}
df = pd.read_csv(file_path)

print(df.head())

# 1. What are the top 10 highest grossing films in the data set? Create a chart to show this data
# Convert the 'revenue' column to numeric, and handling errors by converting them to NaN
# Sort and select top 10 highest grossing films
df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')
sorted_df = df.sort_values(by='revenue', ascending=False)
top_10_highest_gross_films = sorted_df.head(10)

print("The Top 10 Highest Grossing Films: ")
print(top_10_highest_gross_films[['title', 'revenue']])

plt.figure(figsize=(12, 6))
plt.bar(top_10_highest_gross_films['title'], top_10_highest_gross_films['revenue'], color='royalblue')
plt.title('The Top 10 Highest Grossing Films')
plt.xlabel('Film Title')
plt.ylabel('Revenue (bil)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.savefig('The Top 10 Highest Grossing Films.png')
plt.show(block=True)

# 2. What are the total box office dollars by year?
# Start with the earliest year in the data set and go to the last one. Create a chart that shows the results.
# Convert the 'release_date' to datetime, extract the year to create new column 'year'
# Group by year and calc the total revenue for each year
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
df['year'] = df['release_date'].dt.year
total_rev_by_yr = df.groupby('year')['revenue'].sum()

plt.figure(figsize=(12, 6))
total_rev_by_yr.plot(kind='line', marker='o', color='orange')
plt.title('The Total Box Office Dollars by Year')
plt.xlabel('Year')
plt.ylabel('Total Revenue (bil)')
plt.grid(True)
plt.tight_layout()

plt.savefig('The Total Box Office Dollars by Year.png')
plt.show()

# 3. What is the average box office gross by language? Create a chart that shows this data.

# Label numbers used instead of the language abbreviations as "Unknown"
# Apply convert_to_language function to the 'original_language' column so the numbers will be displayed as "Unknown"
def convert_to_language(value):
    if isinstance(value, str):
        return 'Unknown' if any(char.isdigit() for char in value) else value
    else:
        return value

df['original_language'] = df['original_language'].apply(convert_to_language)

# Group by language and calculate the average revenue for each language
avg_rev_by_language = df.groupby('original_language')['revenue'].mean()

plt.figure(figsize=(16, 6))
avg_rev_by_language.sort_values(ascending=False).plot(kind='bar', color='royalblue')
plt.title('Average Box Office Gross by Language')
plt.xlabel('Language')
plt.ylabel('Average Revenue (bil)')
plt.xticks(rotation=90, ha='right')
plt.tight_layout()

plt.savefig('Average Box Office Gross by Language.png')
plt.show()

# 4. What is the relationship between vote_average and vote_count? Create a scatterplot that shows this data.
df['vote_average'] = pd.to_numeric(df['vote_average'], errors='coerce')
df['vote_count'] = pd.to_numeric(df['vote_count'], errors='coerce')

plt.figure(figsize=(14, 6))
plt.scatter(df['vote_average'], df['vote_count'], alpha=0.5, color='green')
plt.title('Vote Average vs Vote Count')
plt.xlabel('Vote Average')
plt.ylabel('Vote Count')
plt.grid(True)
plt.tight_layout()

plt.savefig('Vote Average vs Vote Count.png')
plt.show()

# 5. What relationship, if any, is there between movie runtime and revenue?
df['runtime'] = pd.to_numeric(df['runtime'], errors='coerce')

plt.figure(figsize=(16, 6))
plt.scatter(df['runtime'], df['revenue'], alpha=0.5, color='purple')
plt.title('Movie Runtime vs Revenue')
plt.xlabel('Runtime (min)')
plt.ylabel('Revenue (bil)')
plt.grid(True)
plt.tight_layout()

plt.savefig('Movie Runtime vs Revenue.png')
plt.show()

# 6. What are the top 10 most profitable films? This should be the difference between budget and revenue.
df['budget'] = pd.to_numeric(df['budget'], errors='coerce')
df['profit'] = df['revenue'] - df['budget']

sorted_df = df.sort_values(by='profit', ascending=False)
top_10_profit_films = sorted_df.head(10)

print("Top 10 Most Profitable Films: ")
print(top_10_profit_films[['title', 'profit']])

plt.figure(figsize=(12, 6))
plt.bar(top_10_profit_films['title'], top_10_profit_films['profit'], color='orange')
plt.title('Top 10 Most Profitable Films')
plt.xlabel('Film Title')
plt.ylabel('Profit (bil)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.savefig('Top 10 Most Profitable Films.png')
plt.show()