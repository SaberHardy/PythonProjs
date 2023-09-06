# from sqlalchemy import create_engine, text
#
# # Create an engine object
# engine = create_engine('mysql+pymysql://saber:Flex2020Flex@localhost:3306/BIGDATABASE')
#
# # Create a text clause object
# query = text('SELECT * FROM Employee')
#
# # Execute the query
# connection = engine.connect()
# cursor = connection.execute(query)
# results = cursor.fetchall()
#
# # Print the results
# for row in results:
#     print(row)
#
# # Close the connection
# connection.close()

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

