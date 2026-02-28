-- 코드를 입력하세요
SELECT fd.product_id, fd.product_name, sum(fd.price * fo.amount) total_Sales from food_product fd
join food_order fo on fd.product_id = fo.product_id
where fo.PRODUCE_DATE >= "2022-05-01" and fo.PRODUCE_DATE < "2022-06-01"
group by fd.product_id
order by total_sales desc, product_id