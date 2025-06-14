-- Create the database
CREATE DATABASE IF NOT EXISTS tolldata;

-- Select the database
USE tolldata;

-- Create the table
CREATE TABLE IF NOT EXISTS livetolldata (
    timestamp DATETIME,
    vehicle_id INT,
    vehicle_type CHAR(15),
    toll_plaza_id SMALLINT
);
