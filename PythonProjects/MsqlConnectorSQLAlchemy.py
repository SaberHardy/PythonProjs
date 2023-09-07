import sqlalchemy
import pandas as pd
from sqlalchemy import text

# Create a SQLAlchemy engine
engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:Flex2020Flex@127.0.0.1:3306/BIGDATABASE')

# Wrap the SQL query in a sqlalchemy.text() object
sql_query = text('SELECT * FROM Employee')

# Read the data into a Pandas DataFrame
df = pd.read_sql(sql_query, engine)

# Print the DataFrame to the console
print(df.head())

