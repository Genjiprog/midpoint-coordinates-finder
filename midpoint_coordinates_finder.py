import csv


# Function to read data from a CSV file
def read_data_from_csv(csv_file_path):
    coordinates = []
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Split coordinates into latitude and longitude
            lat, lon = map(float, row['Coordinates'].split(','))
            coordinates.append((lat, lon))
    return coordinates


# Function to calculate the midpoint
def calculate_midpoint(coordinates):
    total_lat = sum(coord[0] for coord in coordinates)
    total_lon = sum(coord[1] for coord in coordinates)
    return total_lat / len(coordinates), total_lon / len(coordinates)


# Path to the CSV file (replace 'your_csv_file.csv' with the actual file path)
csv_file_path = "your_csv_file.csv"

# Read data from the CSV file
coordinates = read_data_from_csv(csv_file_path)

# Calculate the midpoint
midpoint = calculate_midpoint(coordinates)
print("Midpoint Coordinates (Latitude, Longitude):", midpoint)
