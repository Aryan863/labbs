import csv
import random

# Function to generate a random 128-dimensional vector
def generate_random_vector(dim=128):
    return [round(random.uniform(0, 1), 6) for _ in range(dim)]

# Number of rows of data to generate
num_rows = 10

# File name for the CSV
file_name = 'sample_data.csv'

# Field names (schema) for the CSV
fieldnames = ['id', 'vector']

# Create and write to the CSV file
with open(file_name, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Write the header
    writer.writeheader()
    
    # Write rows of data
    for i in range(1, num_rows + 1):
        vector = generate_random_vector()
        writer.writerow({'id': i, 'vector': str(vector)})

print(f'Sample CSV file "{file_name}" created with {num_rows} rows.')
