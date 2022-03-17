from sqlalchemy import Column, Integer, String, Date, cast
from sqlalchemy.orm import declarative_base
# Import the function required
from sqlalchemy.orm import column_property

# Import the objects needed


# Initialize the base and set inheritance
Base = declarative_base()

class PprRawAll(Base):
    __tablename__ = "ppr_raw_all"

    id = Column(Integer, primary_key=True)
    date_of_sale = Column(String(55))
    address = Column(String(255))
    postal_code = Column(String(55))
    county = Column(String(55))
    price = Column(String(55))
    description = Column(String(255))
    # Create a unique transaction id
    transaction_id = column_property(
        date_of_sale + "_" + address + "_" + county + "_" + price
    )

