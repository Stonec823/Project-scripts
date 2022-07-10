DROP DATABASE IF EXISTS company;
CREATE DATABASE company;

-- I'll be designing a simple database for a fictional SaaS company 
-- Create employee table 

CREATE TABLE employee (
empID INT PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR(64) NOT NULL,
last_name VARCHAR(64) NOT NULL,
title VARCHAR(64),
departmentID INT,
loc_id INT,
start_date date);

-- Deaprtment Table, 
CREATE TABLE departments (
id INT PRIMARY KEY AUTO_INCREMENT,
deprtment_name VARCHAR(64),
dept_head VARCHAR(64)
);

-- Location table
CREATE TABLE locations (
loc_id int PRIMARY KEY,
loc_desc VARCHAR(64),
loc_manager VARCHAR(64),
date_opened date
);

-- Client table
CREATE TABLE clients (
client_id INT PRIMARY KEY,
client_name VARCHAR(255),
acct_manager VARCHAR(64),
acct_opened DATETIME
);

-- Setting up foreign key references

ALTER TABLE employee
ADD CONSTRAINT deptID_fkey FOREIGN KEY (departmentID) REFERENCES departments (id);
ALTER TABLE employee
ADD CONSTRAINT locID_fkey FOREIGN KEY (loc_id) REFERENCES locations (loc_id);

-- Need to change data types here to add fkeys

ALTER TABLE departments
MODIFY COLUMN dept_head INT;
ALTER TABLE clients
MODIFY COLUMN acct_manager INT;

ALTER TABLE departments
ADD CONSTRAINT depthead_fkey FOREIGN KEY (dept_head) REFERENCES employee (empID);
ALTER TABLE clients
ADD CONSTRAINT acct_mgr_fkey FOREIGN KEY (acct_manager) REFERENCES employee (empID);

-- Insert a value for each table

INSERT INTO departments VALUES(
1,
'Sales', 
NULL);

INSERT INTO locations VALUES(
1,
'Scranton', 
NULL,
'2001-05-22');


INSERT INTO employee VALUES (
1,
'Jim',
'Halpert',
'Sales Representative',
1,
1,
'2005-10-05');

INSERT INTO clients VALUES(
1,
'HammerMill Paper',
1,
'2012-08-22 10:02:13');

-- Going back to update where we had to put nulls initally

UPDATE departments
SET dept_head = 1
WHERE deprtment_name = 'Sales';

UPDATE locations
SET loc_manager = 1
WHERE loc_id = 1;

-- Set up trigger to record when new employee entries are added

DROP TABLE IF EXISTS new_employee;
CREATE TABLE new_employee (
     message VARCHAR(100),
     time_stamp datetime
);

-- trigger table will include message and current timestamp

DROP TRIGGER IF EXISTS trigger2;
DELIMITER $$
CREATE
    TRIGGER trigger2 BEFORE INSERT
    ON employee
    FOR EACH ROW BEGIN
        INSERT INTO new_employee VALUES('added new employee', NOW());
    END$$
DELIMITER ;

-- Testing by adding values

INSERT INTO employee VALUES (
2, 'Michael', 'Scott', 'Sales Representative', 1, 1, '2022-07-10');

-- testing trigger table

SELECT *
FROM new_employee
