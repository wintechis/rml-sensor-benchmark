import random
from datetime import datetime, timedelta
import csv
import os

# Scale factor
scale = [15,25,55]

##################################
# Seed for reproducibility
random.seed(0)

# Function to generate random dates
def generate_random_dates_with_time(start, end, n):
    delta = end - start
    return [start + timedelta(seconds=random.randint(0, int(delta.total_seconds()))) for _ in range(n)]

# Function to save data to CSV
def save_to_csv(dataset, path, fieldnames):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for data in dataset:
            writer.writerow(data)

# Event names and IDs for Dataset 3
event_names = ['Event_A', 'Event_B', 'Event_C', 'Event_D']
event_ids = list(range(1, len(event_names) + 1))

# Mapping of event IDs to names
event_id_to_name = {eid: name for eid, name in zip(event_ids, event_names)}

# Dataset 1: Temperature, Humidity, and Event ID data
start_date = datetime(2023, 1, 1, 0, 0, 0)
end_date = datetime(2023, 1, 10, 23, 59, 59)
id_counter = 1

n_sample_array = scale

for i in range(len(n_sample_array)):
    n_samples = n_sample_array[i]
    dates_temp_humid = generate_random_dates_with_time(start_date, end_date, n_samples)
    temperatures = [random.uniform(15, 35) for _ in range(n_samples)]
    humidities = [random.uniform(30, 90) for _ in range(n_samples)]
    event_ids_dataset1 = [random.choice(event_ids) for _ in range(n_samples)]

    dataset1 = []
    for date, temp, humid, eid in zip(dates_temp_humid, temperatures, humidities, event_ids_dataset1):
        dataset1.append({
            'ID': id_counter,
            'DateTime': date.isoformat(),  # Convert date to ISO format
            'Temperature': temp, 
            'Humidity': humid, 
            'EventID': eid
        })
        id_counter += 1

    # Dataset 2: Light Intensity and Air Quality data
    light_intensities = [random.uniform(100, 1000) for _ in range(n_samples)]
    air_qualities = [random.uniform(0, 500) for _ in range(n_samples)]

    dataset2 = [{'DateTime': date.isoformat(), 'LightIntensity': light, 'AirQuality': air_qual}
                for date, light, air_qual in zip(dates_temp_humid, light_intensities, air_qualities)]

    # Dataset 3: Event ID and Event Name data
    dataset3 = [{'EventID': eid, 'EventName': name} for eid, name in event_id_to_name.items()]

    # Sorting the datasets by DateTime
    dataset1_sorted = sorted(dataset1, key=lambda x: x['DateTime'])
    dataset2_sorted = sorted(dataset2, key=lambda x: x['DateTime'])

    # Saving the datasets to CSV files
    dataset1_path = f"./{n_sample_array[i]}/sensor_data_temperature_humidity_events.csv"
    dataset2_path = f"./{n_sample_array[i]}/sensor_data_light_air_quality.csv"
    dataset3_path = f"./{n_sample_array[i]}/event_data.csv"

    # Create directory if it does not exist
    os.makedirs(os.path.dirname(dataset1_path), exist_ok=True)

    # Save the datasets
    save_to_csv(dataset1_sorted, dataset1_path, ['ID', 'DateTime', 'Temperature', 'Humidity', 'EventID'])
    save_to_csv(dataset2_sorted, dataset2_path, ['DateTime', 'LightIntensity', 'AirQuality'])
    save_to_csv(dataset3, dataset3_path, ['EventID', 'EventName'])