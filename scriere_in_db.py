from sqlalchemy import create_engine
import pandas as pd

from credentiale import parola
from sda_1 import  read_tabel_din_wiki
engine = create_engine(f"mysql+mysqldb://root:{parola}@localhost/romania")

tabel = read_tabel_din_wiki()
with engine.begin() as connection