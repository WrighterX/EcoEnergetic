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

    # Query 1: High-income districts with more than 50 projected plugs
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

    # Query 2: Charging statistics per customer
    query2 = """
    SELECT customer_id, COUNT(*) AS session_count, AVG(kwh_charged) AS avg_kwh_charged, 
           MIN(total_cost) AS min_cost, MAX(total_cost) AS max_cost
    FROM charging_sessions
    GROUP BY customer_id;
    """
    cursor.execute(query2)
    results2 = cursor.fetchall()
    headers2 = ['Customer ID', 'Session Count', 'Avg kWh Charged', 'Min Cost', 'Max Cost']
    print("\nQuery 2: Charging Statistics per Customer")
    print(tabulate(results2, headers=headers2, tablefmt='psql', floatfmt='.2f'))

    # Query 3: Charging sessions in mid-range income districts with station details
    query3 = """
    SELECT cs.session_id, cs.customer_id, cs.kwh_charged, cs.total_cost, 
           st.district_name, st.operator_name
    FROM charging_sessions cs
    JOIN charging_stations st ON cs.station_id = st.station_id
    WHERE st.income_tier = 'Mid-Range';
    """
    cursor.execute(query3)
    results3 = cursor.fetchall()
    headers3 = ['Session ID', 'Customer ID', 'kWh Charged', 'Total Cost', 'District Name', 'Operator Name']
    print("\nQuery 3: Charging Sessions in Mid-Range Income Districts")
    print(tabulate(results3, headers=headers3, tablefmt='psql', floatfmt='.2f'))

    # Query 4: Average battery capacity per income tier
    query4 = """
    SELECT income_tier, AVG(battery_capacity_kwh) AS avg_battery_capacity
    FROM customers
    GROUP BY income_tier;
    """
    cursor.execute(query4)
    results4 = cursor.fetchall()
    headers4 = ['Income Tier', 'Avg Battery Capacity (kWh)']
    print("\nQuery 4: Average Battery Capacity per Income Tier")
    print(tabulate(results4, headers=headers4, tablefmt='psql', floatfmt='.2f'))

    # Query 5: Number of charging stations per district
    query5 = """
    SELECT district_name, COUNT(*) AS stations_count
    FROM charging_stations
    GROUP BY district_name
    ORDER BY stations_count DESC;
    """
    cursor.execute(query5)
    results5 = cursor.fetchall()
    headers5 = ['District Name', 'Stations Count']
    print("\nQuery 5: Number of Charging Stations per District")
    print(tabulate(results5, headers=headers5, tablefmt='psql'))

    # Query 6: Total kWh charged and total revenue per day
    query6 = """
    SELECT DATE(session_start_time) AS day, SUM(kwh_charged) AS total_kwh, 
           SUM(total_cost) AS total_revenue
    FROM charging_sessions
    GROUP BY day;
    """
    cursor.execute(query6)
    results6 = cursor.fetchall()
    headers6 = ['Day', 'Total kWh', 'Total Revenue']
    print("\nQuery 6: Total kWh Charged and Revenue per Day")
    print(tabulate(results6, headers=headers6, tablefmt='psql', floatfmt='.2f'))

    # Query 7: Top 5 customers by total spending
    query7 = """
    SELECT customer_id, SUM(total_cost) AS total_spent
    FROM charging_sessions
    GROUP BY customer_id
    ORDER BY total_spent DESC
    LIMIT 5;
    """
    cursor.execute(query7)
    results7 = cursor.fetchall()
    headers7 = ['Customer ID', 'Total Spent']
    print("\nQuery 7: Top 5 Customers by Total Spending")
    print(tabulate(results7, headers=headers7, tablefmt='psql', floatfmt='.2f'))

    # Query 8: Average session duration per station (assuming 50 kW charging rate)
    query8 = """
    SELECT cs.station_id, st.district_name, AVG(cs.kwh_charged / 50.0) AS avg_session_duration_hours
    FROM charging_sessions cs
    JOIN charging_stations st ON cs.station_id = st.station_id
    GROUP BY cs.station_id, st.district_name
    ORDER BY avg_session_duration_hours DESC;
    """
    cursor.execute(query8)
    results8 = cursor.fetchall()
    headers8 = ['Station ID', 'District Name', 'Avg Session Duration (Hours)']
    print("\nQuery 8: Average Session Duration per Station")
    print(tabulate(results8, headers=headers8, tablefmt='psql', floatfmt='.2f'))

    # Query 9: Average cost per kWh per car model
    query9 = """
    SELECT c.car_model, AVG(s.cost_per_kwh) AS avg_cost_per_kwh
    FROM customers c
    JOIN charging_sessions s ON c.customer_id = s.customer_id
    GROUP BY c.car_model;
    """
    cursor.execute(query9)
    results9 = cursor.fetchall()
    headers9 = ['Car Model', 'Avg Cost per kWh']
    print("\nQuery 9: Average Cost per kWh per Car Model")
    print(tabulate(results9, headers=headers9, tablefmt='psql', floatfmt='.2f'))

    # Query 10: Projected vs actual unique customers per district
    query10 = """
    SELECT d.district_name, d.projected_regular_customers, 
           COUNT(DISTINCT s.customer_id) AS actual_unique_customers
    FROM districts d
    LEFT JOIN charging_stations st ON d.district_name = st.district_name
    LEFT JOIN charging_sessions s ON st.station_id = s.station_id
    GROUP BY d.district_name, d.projected_regular_customers;
    """
    cursor.execute(query10)
    results10 = cursor.fetchall()
    headers10 = ['District Name', 'Projected Customers', 'Actual Unique Customers']
    print("\nQuery 10: Projected vs Actual Unique Customers per District")
    print(tabulate(results10, headers=headers10, tablefmt='psql'))

except Exception as e:
    print(f"Error: {e}")

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
