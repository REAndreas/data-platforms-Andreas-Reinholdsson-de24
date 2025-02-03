--- Problem 1
SELECT
    *
FROM
    it_educations
WHERE
    LOWER(utbildningsnamn) LIKE 'data eng%';
 
 --- Problem 2
SELECT
    count(*),
    beslut
FROM 
    it_educations
WHERE
    lower(utbildningsnamn) LIKE 'data eng%'
GROUP BY 
    beslut;

---Problem 3

SELECT 
    count(*),
    beslut,
    utbildningsområde
FROM
    myh_2024
WHERE 
    beslut = 'Beviljad'
GROUP BY 
    utbildningsområde, beslut;

--- Problem 4

SELECT 
    count(*),
    beslut,
    kommun
FROM
    myh_2024
WHERE 
    beslut = 'Beviljad'
GROUP BY 
    kommun, beslut;

--- Problem 5

SELECT
    utbildningsområde,
    round(COUNT(CASE WHEN beslut = 'Beviljad' THEN 1 END) * 100.0 / COUNT(*), 2) AS procent_OK,
    round(COUNT(CASE WHEN beslut != 'Beviljad' THEN 1 END) * 100.0 / COUNT(*), 2) AS procent_icke_beviljad
FROM
    myh_2024
GROUP BY
    utbildningsområde;
 