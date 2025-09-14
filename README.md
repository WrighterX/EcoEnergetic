# EcoEnergetic

EcoEnergetic is the company that provides exploratory data analysis (EDA) and visualization. They analyze the correlation between income and EV adoption, examine the distribution of charging stations across different areas, etc.

# Main Analytics

Number of charging stations per district:
<img width="1014" height="459" alt="{1919D332-F41B-4AEF-8240-709E07AE4199}" src="https://github.com/user-attachments/assets/42fc4bbf-b46f-479b-81fd-8dafd69f9a72" />

Top 5 customer by total spending:
<img width="796" height="205" alt="{451198DB-39E8-4B0B-B99E-C15157F9C413}" src="https://github.com/user-attachments/assets/349c4d02-ba41-437a-bdc4-5f2c52b6b862" />

# ER Diagram

<img width="1834" height="1084" alt="EcoEnergetic ERD" src="https://github.com/user-attachments/assets/9b4e1d24-8639-42cb-a932-5eed918ca74c" />

# Tools and Resources

Python, PostgreSQL.

# Instructions

First you need to ensure that you have Python and PostgreSQL installed. If you don't have them, check their documentation on how to do it.

Then, we connect to postgreSQL server, I recommend to do it through *psql* shell with credentials you defined during installation.

Next, create a database called "ecoenergetic". You can name it differently, but "ecoenergetic" is recommended for consistency. After this, download the dataset provided in this GitHub repository.

## Setting Up the Database

1. **Create the Database**:
   In the `psql` shell, create the database:
   ```
   CREATE DATABASE ecoenergetic;
   ```
2. **Connect to the Database**:
   Switch to the new database:
   ```
   \c ecoenergetic
   ```
3. **Create Tables**:
   Run the following SQL commands to create the required tables:
```
   CREATE TABLE districts (
    district_name VARCHAR(100) PRIMARY KEY,
    income_tier VARCHAR(100),
    projected_evs NUMERIC(10, 2),
    projected_plugs NUMERIC(10, 2),
    projected_regular_customers NUMERIC(10, 2)
);

CREATE TABLE customers (
    customer_id VARCHAR(100) PRIMARY KEY,
    income_tier VARCHAR(100),
    car_model VARCHAR(100),
    battery_capacity_kwh NUMERIC(10, 2)
);

CREATE TABLE charging_stations (
    station_id INTEGER PRIMARY KEY,
    district_name VARCHAR(100),
    income_tier VARCHAR(100),
    operator_name VARCHAR(100),
    plugs_count INTEGER,
    latitude NUMERIC(11, 8),
    longitude NUMERIC(11, 8),
    FOREIGN KEY (district_name) REFERENCES districts(district_name)
);

CREATE TABLE charging_sessions (
    session_id VARCHAR(100) PRIMARY KEY,
    customer_id VARCHAR(100),
    station_id INTEGER,
    session_start_time TIMESTAMP,
    kwh_charged NUMERIC(11, 8),
    cost_per_kwh NUMERIC(11, 8),
    total_cost NUMERIC(11, 8),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (station_id) REFERENCES charging_stations(station_id)
);
```

4. **Load the Dataset**:
Copy the CSV files (districts.csv, customers.csv, charging_stations.csv, charging_sessions.csv) from the repository to your local machine. Use the psql \copy command to import the data (adjust file paths as needed):
```
\copy districts FROM 'path/to/districts.csv' DELIMITER ',' CSV HEADER;
\copy customers FROM 'path/to/customers.csv' DELIMITER ',' CSV HEADER;
\copy charging_stations FROM 'path/to/charging_stations.csv' DELIMITER ',' CSV HEADER;
\copy charging_sessions FROM 'path/to/charging_sessions.csv' DELIMITER ',' CSV HEADER;
```

## Running the Script

To run `as1.py`, which connects to the "ecoenergetic" PostgreSQL database and executes three SQL queries with formatted output, follow these steps:

1. **Install Dependencies**:
   Ensure Python is installed, then install required packages:
   ```
   pip install psycopg2-binary tabulate
   ```
2. **Update Database Credentials**:
   Edit as1.py and update the db_params dictionary with your PostgreSQL connection details (host, port, username, password, and database name).
   **Run the Script**:
3. **Execute the script from the terminal**:
   ```
   python as1.py
   ```
4. **Expected Output**:
   The script will display three tables in the terminal:

   High-income districts with >50 projected plugs.
   Average battery capacity per income tier.
   Number of charging stations per district.

Note: Ensure the PostgreSQL database "ecoenergetic" is running and accessible with the provided credentials.
