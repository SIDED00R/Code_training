SELECT fp.category,
       fp.price AS MAX_PRICE,
       fp.product_name
FROM food_product fp
JOIN (
    SELECT category, MAX(price) AS max_price
    FROM food_product
    WHERE category IN ('과자', '국', '김치', '식용유')
    GROUP BY category
) m
ON fp.category = m.category
AND fp.price = m.max_price
ORDER BY fp.price DESC