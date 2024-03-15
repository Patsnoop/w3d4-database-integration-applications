const sqlite3 = require('sqlite3').verbose(); // Import the sqlite3 module

// Connect to the SQLite database
const db = new sqlite3.Database('bloggingDatabase.sqlite', (err) => {
    if (err) {
        console.error("Error connecting to database:", err.message);
    } else {
        console.log("Connected to the database");
    }
});

// Function to execute a SQL query
function executeQuery(query) {
    db.all(query, [], (err, rows) => {
        if (err) {
            console.error("Error executing query:", err.message);
        } else {
            console.log("Query results:");
            rows.forEach(row => {
                console.log(row);
            });
        }
    });
}

// Function to close the database connection
function closeConnection() {
    db.close((err) => {
        if (err) {
            console.error("Error closing database:", err.message);
        } else {
            console.log("Database connection closed");
        }
    });
}

// Main function to execute queries and close connection
function main() {
    // Basic SELECT query to fetch the first 3 rows from the 'bloggingDatabase' table
    console.log("Fetching first 3 rows from the 'bloggingDatabase' table:");
    executeQuery("SELECT * FROM bloggingDatabase LIMIT 3;");
    
    // Close the connection
    closeConnection();
}

// Execute the main function
main();