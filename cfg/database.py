""""""

import os

import pyodbc
from dotenv import load_dotenv
import sqlalchemy as sqlA

environment = os.getenv("ENVIRONMENT")

if environment == "PRODUCTION":
    # Your production code here
    pass

else:

    load_dotenv()
    username = os.getenv("DB-DW-USERNAME")
    host = os.getenv("DB-DW-HOST")
    password = os.getenv("DB-DW-PASSWORD")
    database = os.getenv("DB-DW-DATABASE")
    driver = "driver=SQL Server"

    engine = sqlA.create_engine(
        "mssql+pyodbc://"
        + username
        + ":" + password
        + "@" + host
        + "/" + database
        + "?" + driver
    )

    connection = engine.connect()
