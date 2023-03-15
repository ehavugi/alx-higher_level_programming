-- display average temperature (Fahrenheit) by city order by temperature descending
-- import temperature data dump into hbtn_0c_0;
SELECT city , AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC; 
