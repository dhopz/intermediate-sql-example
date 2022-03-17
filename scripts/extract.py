import os
import csv
import tempfile
from turtle import down
from zipfile import ZipFile

import requests

# Settings
base_path = os.path.abspath(__file__ + "/../../")

# Source path where we want to save the .zip file downloaded from the website
source_path = f"{base_path}/data/source/summer.csv"

# Raw path where we want to extract the new .csv data
raw_path = f"{base_path}/data/raw/new_summer.csv"


def create_folder_if_not_exists(path):
    """
    Create a new folder if it doesn't exists
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)

def save_new_raw_data():
    """
    Save new raw data from the source
    """    
    # Open the CSV file in read mode
    with open(source_path, mode="r", encoding="windows-1252") as csv_file:
        reader = csv.DictReader(csv_file)

        row = next(reader)  # Get first row from reader
        print("[Extract] First row example:", row)

        # Open the CSV file in write mode
        with open(
            raw_path,
            mode="w",
            encoding="windows-1252"
        ) as csv_file:
            # Rename field names so they're ready for the next step
            fieldnames = {
                "Year": "year",
                "City": "city",
                "Sport": "sport",
                "Discipline": "discipline",
                "Athelete": "athlete",
                "Country": "country",
                "Gender":"gender",
                "Event":"event",
                "Medal":"medal"
            }
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            # Write headers as first line
            writer.writerow(fieldnames)
            for row in reader:
                # Write all rows in file
                writer.writerow(row)

# Main function called inside the execute.py script
def main():
    print("[Extract] Start")
    print(f"[Extract] Saving data from '{source_path}' to '{raw_path}'")
    save_new_raw_data()
    print(f"[Extract] End")