from base import Base, engine
# Import the PprRawAll table
from common.tables import SummerOlympics

# Create the table in the database
if __name__ == "__main__":
    Base.metadata.create_all(engine)