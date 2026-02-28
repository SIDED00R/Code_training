-- 코드를 입력하세요
SELECT ri1.food_type, rest_id, rest_name, ri1.favorites from rest_info ri1
join (SELECT food_type, max(favorites) favorites from rest_info ri group by food_type) ri2 
on ri1.food_type = ri2.food_type and ri1.favorites = ri2.favorites
order by ri1.food_type desc