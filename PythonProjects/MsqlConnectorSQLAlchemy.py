import sqlalchemy
import pandas as pd
from sqlalchemy import text

# Create a SQLAlchemy engine
password = "type your password here"
database_name = "BIGDATABASE"
engine = sqlalchemy.create_engine(f'mysql+mysqlconnector://root:{password}@127.0.0.1:3306/{database_name}')

# Wrap the SQL query in a sqlalchemy.text() object
sql_query = text('SELECT * FROM Employee')

# Read the data into a Pandas DataFrame
df = pd.read_sql(sql_query, engine)

# Print the DataFrame to the console
print(df.head())

