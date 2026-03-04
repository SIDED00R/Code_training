SELECT
    YEAR(os.sales_date)  AS year,
    MONTH(os.sales_date) AS month,
    ui.gender,
    COUNT(DISTINCT ui.user_id) AS users
FROM user_info ui
JOIN online_sale os
  ON ui.user_id = os.user_id
WHERE ui.gender IS NOT NULL
GROUP BY YEAR(os.sales_date), MONTH(os.sales_date), ui.gender
ORDER BY year, month, ui.gender;