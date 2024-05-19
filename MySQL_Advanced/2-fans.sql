-- Assuming the table name from the metal_bands.sql dump is 'bands' with columns 'origin' and 'fans'
-- If the table or column names are different, adjust accordingly

-- Calculate the number of fans for each origin and order by the number of fans in descending order
SELECT origin, SUM(fans) AS nb_fans
FROM bands
GROUP BY origin
ORDER BY nb_fans DESC;
