-- 1. High-income districts with more than 50 projected plugs, sorted by projected EVs descending
SELECT district_name, income_tier, projected_evs, projected_plugs
FROM districts
WHERE income_tier = 'High' AND projected_plugs > 50
ORDER BY projected_evs DESC;
-- 2. Charging statistics per customer: number of sessions, average kWh charged, min and max total cost
SELECT customer_id, COUNT(*) AS session_count, AVG(kwh_charged) AS avg_kwh_charged, MIN(total_cost) AS min_cost, MAX(total_cost) AS max_cost
FROM charging_sessions
GROUP BY customer_id;
-- 3. Charging sessions in mid-range income districts with station details
SELECT cs.session_id, cs.customer_id, cs.kwh_charged, cs.total_cost, st.district_name, st.operator_name
FROM charging_sessions cs
JOIN charging_stations st ON cs.station_id = st.station_id
WHERE st.income_tier = 'Mid-Range';
-- 4. Average battery capacity per income tier
SELECT income_tier, AVG(battery_capacity_kwh) AS avg_battery_capacity
FROM customers
GROUP BY income_tier;
-- 5. Number of charging stations per district
SELECT district_name, COUNT(*) AS stations_count
FROM charging_stations
GROUP BY district_name
ORDER BY stations_count DESC;
-- 6. Total kWh charged and total revenue per day
SELECT DATE(session_start_time) AS day, SUM(kwh_charged) AS total_kwh, SUM(total_cost) AS total_revenue
FROM charging_sessions
GROUP BY day;
-- 7. Top 5 customers by total spending
SELECT customer_id, SUM(total_cost) AS total_spent
FROM charging_sessions
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 5;
-- 8. Average session duration per station (assuming 50 kW charging rate)
SELECT cs.station_id, st.district_name, AVG(cs.kwh_charged / 50.0) AS avg_session_duration_hours 
FROM charging_sessions cs 
JOIN charging_stations st ON cs.station_id = st.station_id 
GROUP BY cs.station_id, st.district_name 
ORDER BY avg_session_duration_hours DESC;
-- 9. Average cost per kWh per car model
SELECT c.car_model, AVG(s.cost_per_kwh) AS avg_cost_per_kwh
FROM customers c
JOIN charging_sessions s ON c.customer_id = s.customer_id
GROUP BY c.car_model;
-- 10. Projected vs actual unique customers per district
SELECT d.district_name, d.projected_regular_customers, COUNT(DISTINCT s.customer_id) AS actual_unique_customers
FROM districts d
LEFT JOIN charging_stations st ON d.district_name = st.district_name
LEFT JOIN charging_sessions s ON st.station_id = s.station_id
GROUP BY d.district_name, d.projected_regular_customers;