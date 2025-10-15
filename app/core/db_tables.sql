-- Create the clients table
CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address TEXT,
    balance DECIMAL(10, 2) DEFAULT 0.00
);

-- Insert sample data into the clients table
INSERT INTO clients (name, email, phone_number, address, balance) 
VALUES 
    ('John Doe', 'john.doe@example.com', '123-456-7890', '1234 Elm St, Springfield, IL', 100.50),
    ('Jane Smith', 'jane.smith@example.com', '987-654-3210', '5678 Oak St, Springfield, IL', 250.75);

-- Create the stored procedure to insert a client into the clients table
CREATE OR REPLACE PROCEDURE insert_client(
    p_name VARCHAR,
    p_email VARCHAR,
    p_phone_number VARCHAR,
    p_address TEXT,
    p_balance DECIMAL
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO clients (name, email, phone_number, address, balance)
    VALUES (p_name, p_email, p_phone_number, p_address, p_balance);
END;
$$;

-- Example of calling the stored procedure to insert a new client
CALL insert_client(
    'Alice Johnson', 
    'alice.johnson@example.com', 
    '555-1234-5678', 
    '789 Maple St, Cityville, CA', 
    500.00
);
