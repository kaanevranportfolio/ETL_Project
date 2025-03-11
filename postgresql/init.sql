-- Create a table for storing customer data
CREATE TABLE IF NOT EXISTS customers (
    "Index" SERIAL PRIMARY KEY,  -- Auto-incrementing primary key
    "Customer Id" INTEGER NOT NULL,  -- Unique identifier for the customer
    "First Name" VARCHAR(255) NOT NULL,  -- Customer's first name
    "Last Name" VARCHAR(255) NOT NULL,  -- Customer's last name
    "Company" VARCHAR(255),  -- Company name, if applicable
    "City" VARCHAR(255),  -- City of residence
    "Country" VARCHAR(255),  -- Country of residence
    "Phone 1" VARCHAR(50),  -- Primary phone number
    "Phone 2" VARCHAR(50),  -- Secondary phone number, optional
    "Email" VARCHAR(255) UNIQUE NOT NULL,  -- Email address, must be unique
    "Subscription Date" DATE,  -- Date of subscription
    "Website" VARCHAR(255)  -- Website URL, if applicable
);

-- Optional: Insert sample data
INSERT INTO customers ("Customer Id", "First Name", "Last Name", "Company", "City", "Country", "Phone 1", "Phone 2", "Email", "Subscription Date", "Website")
VALUES
(1, 'John', 'Doe', 'Acme Corp', 'New York', 'USA', '123-456-7890', '098-765-4321', 'john.doe@example.com', '2023-01-01', 'http://johndoe.com'),
(2, 'Jane', 'Smith', 'Tech Solutions', 'San Francisco', 'USA', '555-123-4567', NULL, 'jane.smith@example.com', '2023-02-15', NULL);