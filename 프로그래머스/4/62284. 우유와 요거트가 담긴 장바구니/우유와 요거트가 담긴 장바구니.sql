-- 코드를 입력하세요
SELECT cp1.cart_id from cart_products cp1
join (select cart_id from cart_products where name like "Yogurt") cp2 on cp1.cart_id = cp2.cart_id
where name like "Milk"
order by cart_id