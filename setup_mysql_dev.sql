-- Script to set up MySQL server for the HBNB project

-- Drop the user if it exists
DROP USER IF EXISTS 'hbnb_dev'@'localhost';

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant the user all privileges on the hbnb_dev_db database
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to ensure all changes take effect
FLUSH PRIVILEGES;

-- Switch to the database
USE hbnb_dev_db;

-- Create the states table if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Clear the states table if needed
TRUNCATE TABLE states;

-- Insert sample data into the states table
INSERT INTO states (name) VALUES ('California'), ('Texas'), ('Florida');

-- Optionally, check inserted data
SELECT * FROM states;
