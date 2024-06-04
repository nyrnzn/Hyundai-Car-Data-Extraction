## Hyundai Car Data Extraction Script

This is a Python script designed to extract car data from Hyundai's Click to Buy platform. The script fetches a list of car models and then retrieves details (including variant and price) for each selected model. Finally, the extracted data is exported to a CSV file.

**Requirements:**

* Python 3
* Libraries: requests, json, csv, datetime

**Instructions:**

1. Save the script as a Python file (e.g., `hyundai_car_data.py`).
2. Run the script using Python (`python hyundai_car_data.py`).

**Output:**

The script will generate a CSV file named `car_data_[timestamp].csv` containing the following columns:

* Model
* Varient
* ExShowroomPrice

**Notes:**

* This script relies on Hyundai's Click to Buy APIs, which might be subject to change.
* Error handling is included to capture potential issues during data retrieval.
* The script currently extracts data for all available models. You can modify it to filter specific models based on your needs.

**Disclaimer:**

This script is provided for educational purposes only. It is recommended to respect Hyundai's terms and conditions when using their platform.
