#Read README.md
import pandas as pd
import os

# Load the CSV file into a DataFrame with the first row as the header
df = pd.read_csv('sports_car(uds).csv', header=0)

# Define the base path where the folders will be created
base_path = r"E:\New folder (3)\car photos"

# Iterate over each row in the DataFrame
for i, row in df.iterrows():
    # Extract the Car Make, Car Model, and Year
    car_make = row['Car Make']
    car_model = row['Car Model']
    year = row['Year']
    
    # Create the folder name with a unique identifier
    folder_name = f"{i+1}, {car_make}, {car_model}, {year}"
    
    # Create the full path for the folder
    full_path = os.path.join(base_path, folder_name)
    
    # Create the folder if it doesn't exist
    if not os.path.exists(full_path):
        os.makedirs(full_path)

print("Folders created successfully.")
