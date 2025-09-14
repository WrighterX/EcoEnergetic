import psycopg2
from tabulate import tabulate

db_params = {
    'dbname': 'ecoenergetic',
    'user': 'postgres',
    'password': 'password',
    'host': 'localhost',
    'port': '5432'
}

try:
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Query 1: High-income districts with more than 50 projected plugs, sorted by projected EVs
    query1 = """
    SELECT district_name, income_tier, projected_evs, projected_plugs 
    FROM districts 
    WHERE income_tier = 'High' AND projected_plugs > 50 
    ORDER BY projected_evs DESC;
    """
    cursor.execute(query1)
    results1 = cursor.fetchall()
    headers1 = ['District Name', 'Income Tier', 'Projected EVs', 'Projected Plugs']
    print("\nQuery 1: High-Income Districts with >50 Projected Plugs")
    print(tabulate(results1, headers=headers1, tablefmt='psql'))

    # Query 2: Average battery capacity per income tier
    query2 = """
    SELECT income_tier, AVG(battery_capacity_kwh) AS avg_battery_capacity 
    FROM customers 
    GROUP BY income_tier;
    """
    cursor.execute(query2)
    results2 = cursor.fetchall()
    headers2 = ['Income Tier', 'Avg Battery Capacity (kWh)']
    print("\nQuery 2: Average Battery Capacity per Income Tier")
    print(tabulate(results2, headers=headers2, tablefmt='psql', floatfmt='.2f'))

    # Query 3: Number of charging stations per district
    query3 = """
    SELECT district_name, COUNT(*) AS stations_count 
    FROM charging_stations 
    GROUP BY district_name 
    ORDER BY stations_count DESC;
    """
    cursor.execute(query3)
    results3 = cursor.fetchall()
    headers3 = ['District Name', 'Stations Count']
    print("\nQuery 3: Number of Charging Stations per District")
    print(tabulate(results3, headers=headers3, tablefmt='psql'))

except Exception as e:
    print(f"Error: {e}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()