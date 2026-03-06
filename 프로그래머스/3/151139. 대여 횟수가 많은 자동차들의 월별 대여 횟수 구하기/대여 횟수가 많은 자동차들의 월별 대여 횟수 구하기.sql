-- 코드를 입력하세요
SELECT month(start_date) month, c1.car_id, count(*) records from car_rental_company_rental_history c1
join (SELECT car_id, count(*) records from car_rental_company_rental_history
where start_date >= '2022-08-01' and start_date < '2022-11-01' 
group by car_id
having records >= 5) c2
on c1.car_id = c2.car_id
where start_date >= '2022-08-01' and start_date < '2022-11-01' 
group by month, car_id
order by month, car_id desc