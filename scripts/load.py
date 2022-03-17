import os
import csv
from datetime import datetime
from common.tables import SummerOlympics
#from common.tables import SummerOlympics
from common.base import session
from sqlalchemy import text

#base_path = os.path.dirname(os.path.abspath("__file__"))
base_path = os.path.abspath(__file__ + "/../../")
#print(base_path)
transformed_path = f"{base_path}/data/raw/new_summer.csv"

def truncate_table():
    """
    Ensure that the tables are in an empty state before running any transformations.
    And primary key (id) restarts from 1.
    """
    session.execute(
        text("TRUNCATE TABLE athletes ;ALTER SEQUENCE athletes_id_seq RESTART;")
    )
    session.commit()

def transform_new_data():
    """
    Apply all transformations for each row in the .csv file before saving it into database
    """
    with open(transformed_path, mode="r", encoding="windows-1252") as csv_file:
        # Read the new CSV snapshot ready to be processed
        reader = csv.DictReader(csv_file)
        # Initialize an empty list 
        new_objects = []
        for row in reader:
            # Apply transformations and save as object
            new_objects.append(
                SummerOlympics(
                    year = row["year"],
                    city = row["city"],
                    sport = row["sport"],
                    discipline = row["discipline"],
                    athlete = row['athlete'],
                    country = row['country'],
                    gender = row['gender'],
                    medal_event = row['medal_event'],
                    medal = row['medal']               
                )
            )
        # Save all new processed objects and commit
        session.bulk_save_objects(new_objects)
        session.commit()

def main():
    print("[Load] Start")   
    print("[Load] Truncating table")  
    truncate_table  
    print("[Load] Data going in Postgres...")
    transform_new_data()
    print("[Load] End")