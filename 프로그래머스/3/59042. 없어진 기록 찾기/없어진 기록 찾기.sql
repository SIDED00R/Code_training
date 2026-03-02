-- 코드를 입력하세요
SELECT ao.animal_id, ao.name from ANIMAL_INS ai
right join animal_outs ao on ai.animal_id = ao.animal_id
where ai.animal_id is null
order by animal_id