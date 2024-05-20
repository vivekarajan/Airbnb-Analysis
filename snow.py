import csv
import snowflake.connector
import os
import json

def csv_to_json(csv_file, json_file):
    # Read CSV file and convert to list of dictionaries
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        data = list(csv_reader)
    
    # Write JSON data to file
    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)

# Specify input CSV file and output JSON file
csv_file = r"E:\airbnb project\cleaned_Data.csv"
json_file = r"E:\airbnb project\output.json"



# Print the values to debug
#print(f"Account: {account}")
#print(f"User: {user}")
#print(f"Password: {password}")
#print(f"Warehouse: {warehouse}")
#print(f"Database: {database}")
#print(f"Schema: {schema}")

# Convert CSV to JSON
csv_to_json(csv_file, json_file)


# Define connection parameters
account = 'cylgfoq-rz47686'
user = 'VIVEKSTARK'
password = '*****'
warehouse = 'AIRBNB'
database = 'AIRBNB'
schema = 'PROJECT'
stage_name = 'NEW_DATA'
table_name = 'DETAILS'  # Assuming schema is already set in the connection

# Specify the path to the JSON file
json_file_path = r"E:\airbnb project\output.json"

try:
    # Establish the connection
    conn = snowflake.connector.connect(
        account=account,
        user=user,
        password=password,
        warehouse=warehouse,
        database=database,
        schema=schema
    )

    # Create a cursor object
    cur = conn.cursor()

    # Upload the JSON file to Snowflake stage
    cur.execute(f"PUT file://{json_file_path} @{stage_name}")
    print("JSON file uploaded to stage successfully.")

    # Load data from stage into a Snowflake table
    cur.execute(f"COPY INTO {table_name} FROM @{stage_name}")
    print("Data loaded from stage into Snowflake table successfully.")

except snowflake.connector.errors.ProgrammingError as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    cur.close()
    conn.close()
