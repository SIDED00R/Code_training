-- 코드를 입력하세요
SELECT ai.animal_id, ai.name from ANIMAL_INS ai
join animal_outs ao on ai.ANIMAL_ID = ao.ANIMAL_ID
order by abs(datediff(ai.DATETIME, ao.DATETIME)) desc
limit 2