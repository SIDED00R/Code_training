-- 코드를 입력하세요
SELECT order_id, product_id, 
case when out_date is null then out_date
else date_format(out_date, '%Y-%m-%d') end as out_date, 
case when out_date <= '2022-05-01' then "출고완료"
when out_date is null then "출고미정"
else "출고대기" end as '출고여부' from food_order
order by order_id