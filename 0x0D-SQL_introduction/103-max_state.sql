-- display average temperature (Fahrenheit) by city order by temperature descending
-- import temperature data dump into hbtn_0c_0;
-- top 3 cities during July and August
SELECT state , MAX(value) AS max_temp 
FROM temperatures  
GROUP BY state 
ORDER BY max_temp DESC;
