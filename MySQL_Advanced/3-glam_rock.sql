-- Assuming the table name from the metal_bands.sql dump is 'bands' with columns 'band_name', 'style', 'formed', and 'split'
-- If the table or column names are different, adjust accordingly

-- Calculate the lifespan for Glam rock bands and order by lifespan in descending order
SELECT 
    band_name, 
    CASE 
        WHEN split IS NULL THEN YEAR(CURDATE()) - formed 
        ELSE split - formed 
    END AS lifespan
FROM bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
