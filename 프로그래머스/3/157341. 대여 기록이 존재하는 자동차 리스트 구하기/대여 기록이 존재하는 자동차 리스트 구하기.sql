-- 코드를 입력하세요
SELECT DISTINCT ch.car_id from CAR_RENTAL_COMPANY_RENTAL_HISTORY  as ch
join CAR_RENTAL_COMPANY_CAR cc on ch.car_id = cc.car_id
where car_type = "세단" and month(ch.start_date) = 10
order by car_id desc