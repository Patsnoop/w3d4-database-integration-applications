import sqlite3  # Import the sqlite3 module for interacting with SQLite databases

# Connect to the SQLite database
conn = sqlite3.connect('bloggingDatabase.sqlite')  # Establish a connection to the 'bloggingDatabase.sqlite' database file
cur = conn.cursor()  # Create a cursor object to execute SQL commands

# Function to execute SQL queries
def execute_query(query):
    cur.execute(query)  # Execute the SQL query
    rows = cur.fetchall()  # Fetch all rows returned by the query
    for row in rows:  # Iterate over each row
        print(row)  # Print the row

# Function to close the connection
def close_connection():
    conn.close()  # Close the connection to the SQLite database

def main():
    # Basic SELECT query to fetch the first 10 rows from the 'bloggingDatabase' table
    print("Fetching first 3 rows from the 'bloggingDatabase' table:")
    execute_query("SELECT * FROM bloggingDatabase LIMIT 3;")

    # Close the connection
    close_connection()  # Close the connection to the SQLite database

if __name__ == "__main__":
    main()