#Read README.md
import pandas as pd
import psycopg2

# Load the CSV file into a DataFrame with the first row as the header
df = pd.read_csv('sports_car(uds).csv', header=0)

# Replace missing values with "NaN"
df.fillna("NaN", inplace=True)

# Remove commas from the 'Price (in USD)' column
df['Price (in USD)'] = df['Price (in USD)'].str.replace(',', '').astype(float)

# Convert 'Engine Size (L)' to numeric, setting errors='coerce' to handle non-numeric values
df['Engine Size (L)'] = pd.to_numeric(df['Engine Size (L)'], errors='coerce')

# Convert 'Horsepower' to numeric, setting errors='coerce' to handle non-numeric values
df['Horsepower'] = pd.to_numeric(df['Horsepower'].str.replace('+', ''), errors='coerce')

# Convert 'Torque (lb-ft)' to numeric, setting errors='coerce' to handle non-numeric values
df['Torque (lb-ft)'] = pd.to_numeric(df['Torque (lb-ft)'].replace('-', 'NaN'), errors='coerce')

# Convert '0-60 MPH Time (seconds)' to numeric, setting errors='coerce' to handle non-numeric values
df['0-60 MPH Time (seconds)'] = pd.to_numeric(df['0-60 MPH Time (seconds)'].str.replace('<', '').str.strip(), errors='coerce')

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host='localhost',  # Replace with your host
    database='test',  # Replace with your actual database name
    user='postgres',  # Replace with your actual username
    password='Sampad@5505'  # Replace with your actual password
)

# Create a cursor object
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sports_car (
        id SERIAL PRIMARY KEY,
        car_make VARCHAR(255),
        car_model VARCHAR(255),
        year INT,
        engine_size FLOAT,
        horsepower FLOAT,  
        torque FLOAT,  
        zero_to_sixty FLOAT,
        price FLOAT
    )
''')

# Insert DataFrame records one by one
for i, row in df.iterrows():
    sql = '''
        INSERT INTO sports_car (
            car_make, car_model, year, engine_size, horsepower, torque, zero_to_sixty, price
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''
    values = row[['Car Make', 'Car Model', 'Year', 'Engine Size (L)', 'Horsepower', 'Torque (lb-ft)', '0-60 MPH Time (seconds)', 'Price (in USD)']].tolist()
    cursor.execute(sql, values)

# Commit the transaction
conn.commit()
conn.close()
