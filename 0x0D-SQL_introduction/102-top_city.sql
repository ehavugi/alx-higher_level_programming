-- display average temperature (Fahrenheit) by city order by temperature descending
-- import temperature data dump into hbtn_0c_0;
-- top 3 cities during July and August
SELECT city , AVG(value) AS avg_temp 
FROM temperatures  
WHERE month in (7, 8) 
GROUP BY city 
ORDER BY avg_temp DESC 
LIMIT 3; 
