# read requirements.md
import pandas as pd

# Read the CSV file
df = pd.read_csv('Sport car price(dds).csv')

# Filter the data for the years 2022 and 2023
filtered_df = df[(df['Year'] == 2022) | (df['Year'] == 2023)]

# Drop duplicates based on "Car Make", "Car Model", and "Year"
filtered_df = filtered_df.drop_duplicates(subset=['Car Make', 'Car Model', 'Year'])

# Write the filtered data to a new CSV file
filtered_df.to_csv('sports_car_filtered.csv', index=False)

# Create a new DataFrame for the years 2021, 2022, and 2023
new_df = df[(df['Year'] == 2022) | (df['Year'] == 2023) | (df['Year'] == 2021)]

# Drop duplicates based on "Car Make", "Car Model", and "Year"
new_df = new_df.drop_duplicates(subset=['Car Make', 'Car Model', 'Year'])

# Write the new DataFrame to a new CSV file
new_df.to_csv('sports_car(uds).csv', index=False)

print("Filtered and merged data written to 'sports_car_filtered.csv' and 'sports_car.csv'.")