import sqlite3
# Connect to the database (creates the database file if it doesn't exist)
con = sqlite3.connect("bloggingDatabase.sqlite")
# Create a cursor object
cur = con.cursor()
# Execute a SQL command to create a table (optional)
cur.execute('''CREATE TABLE IF NOT EXISTS bloggingDatabase (
                user INTEGER PRIMARY KEY,
                posts INTEGER,
                comments TEXT
            )''')



# # Execute a SQL command to insert data into the table (optional)
cur.execute("INSERT INTO bloggingDatabase (posts, comments) VALUES (?, ?)", (37, "They always get things wrong"))
cur.execute("INSERT INTO bloggingDatabase (posts, comments) VALUES (?, ?)", (11, "Has insight, but not foresight"))
cur.execute("INSERT INTO bloggingDatabase (posts, comments) VALUES (?, ?)", (3, "NEW USER: NOT ENOUGH DATA"))
# # Execute a SQL command to select data from the table
cur.execute("SELECT * FROM bloggingDatabase")
print(cur.fetchall())  # Output: [(1, 'Movie A', 2020)]
# Commit changes (if necessary)
con.commit()
# Close the connection
con.close()