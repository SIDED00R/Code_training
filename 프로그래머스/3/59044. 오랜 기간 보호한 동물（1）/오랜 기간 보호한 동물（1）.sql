-- 코드를 입력하세요
SELECT ai.name, ai.datetime from ANIMAL_INS ai
left join ANIMAL_OUTS ao on ai.ANIMAL_ID = ao.ANIMAL_ID
where ao.animal_id is null
order by datetime
limit 3
