from sqlalchemy import Column, Integer, String, Date, cast
from sqlalchemy.orm import declarative_base
# Import the function required
from sqlalchemy.orm import column_property

# Import the objects needed
# Initialize the base and set inheritance
Base = declarative_base()

class SummerOlympics(Base):
    __tablename__ = "athletes"

    id = Column(Integer, primary_key=True)
    year = Column(String(55))
    city = Column(String(255))
    sport = Column(String(55))
    discipline = Column(String(55))
    athlete = Column(String(55))
    country = Column(String(255))
    gender = Column(String(255))
    medal_event = Column(String(255))
    medal = Column(String(255))

