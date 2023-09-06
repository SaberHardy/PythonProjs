from sqlalchemy import create_engine, text

# Create an engine object
engine = create_engine('mysql+pymysql://saber:Flex2020Flex@localhost:3306/BIGDATABASE')

# Create a text clause object
query = text('SELECT * FROM Employee')

# Execute the query
connection = engine.connect()
cursor = connection.execute(query)
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the connection
connection.close()
