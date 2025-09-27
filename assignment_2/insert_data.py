import psycopg2

# Database connection parameters (update these for your environment)
db_params = {
    'dbname': 'ecoenergetic',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432'
}

try:
    # Connect to the database
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Insert a new charging station with a new operator
    insert_sql = """
    INSERT INTO charging_stations (station_id, district_name, income_tier, operator_name, plugs_count, latitude, longitude)
    VALUES (999, 'Ursynow', 'Mid-Range', 'NewEcoCharge', 6, 52.120000, 21.000000);
    """
    cursor.execute(insert_sql)
    conn.commit()
    print("Inserted new charging station with operator 'NewEcoCharge'. Re-run the visualization script to see changes in the pie chart.")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close database connection
    if cursor:
        cursor.close()
    if conn:
        conn.close()