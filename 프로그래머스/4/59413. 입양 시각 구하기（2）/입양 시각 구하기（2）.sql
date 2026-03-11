-- 코드를 입력하세요

with recursive hours as (
    select 0 as h
    union all
    select h + 1 from hours where h < 23
)

SELECT h hour, count(datetime) count from hours
left join animal_outs ao
on hour(ao.datetime) = h
group by hour
order by hour