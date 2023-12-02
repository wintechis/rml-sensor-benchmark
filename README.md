# RML-SENSOR Benchmark

## Overview
The RML-SENSOR Benchmark is designed to evaluate the performance of RML processors, especially in microcontroller and IoT device contexts. It simulates data from two types of sensors: a temperature and humidity sensor, and another sensor capable of measuring light intensity and air quality. It also generates a third dataset containing information about various events, offering a diverse range of data for performance evaluation. The tool generates datasets exclusively in CSV format. A notable feature of this benchmark is that the scale factor, when multiplied by 10, indicates the expected result size of the datasets.

## Requirements
- Python 3.10 or higher

## Installation
No additional libraries are required to run the script.

## Usage
To generate a dataset, follow these steps:
1. Open the `rml_sensor_generator.py` file.
2. Modify line 7 to include your desired scale factors. The scale factor determines the number of lines in the generated CSV file. For example:
   ```python
   scale = [15, 25, 55]
   ```
3. Run the script with the following command:
    ```bash
   python3 rml_sensor_generator.py
   ```
4. Place the provided `sensor_mapping.ttl` file in the generated directories and execute the mappings using an RML processor.

In the default configuration, datasets with scales of 15, 25, and 55 are generated.