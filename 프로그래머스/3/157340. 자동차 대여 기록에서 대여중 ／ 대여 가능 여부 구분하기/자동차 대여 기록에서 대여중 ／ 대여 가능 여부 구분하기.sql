-- 코드를 입력하세요
SELECT car_id, 
case 
when exists (
    select 1 from car_rental_company_rental_history h2
    where h2.car_id = h1.car_id
    and start_date <= '2022-10-16' 
    and end_date >= '2022-10-16') 
    then '대여중'
    else '대여 가능' 
end availaility 
from car_rental_company_rental_history h1
group by car_id
order by car_id desc