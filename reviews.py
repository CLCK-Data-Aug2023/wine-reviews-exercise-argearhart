import zipfile
import pandas as pd
import numpy as np

# Create a Python program that reads in the `data/winemag-data-130k-v2.csv.zip` file

# Open the ZIP file and read the CSV data
with zipfile.ZipFile('data/winemag-data-130k-v2.csv.zip', 'r') as zip_file:
    with zip_file.open('winemag-data-130k-v2.csv') as csv_file:
        df = pd.read_csv(csv_file, index_col=0)

# Create a summary of the data that contains the name, number of reviews, and #
# the average points for each unique country in the dataset.
df.head()

# Calculate average number of points for each country
reviews_per_country = df['country'].value_counts()
average_points_per_country = df.groupby('country')['points'].mean().round(1)
print(reviews_per_country)
print(average_points_per_country)


# Create a summary of the data that contains the name, number of reviews, and
# the average points for each unique country in the dataset.
summary_df = pd.DataFrame({
    'count': reviews_per_country,
    'points': average_points_per_country
})
summary_df.index.name = 'country'


# Write the summary data to a new file in the `data` folder named
# `reviews-per-country.csv`.d your code here
summary_df.to_csv('data/reviews-per-country.csv')

print(summary_df)
