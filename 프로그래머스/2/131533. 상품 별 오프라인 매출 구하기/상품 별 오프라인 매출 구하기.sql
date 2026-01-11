SELECT p.product_code, sum(p.price * os.SALES_AMOUNT) as sales 
from product p
join OFFLINE_SALE os
on p.product_id = os.product_id
group by p.product_code
order by sales desc, product_code