-- 코드를 작성해주세요
select * from(
select 
    case
        when ((select code from skillcodes where name = 'Python') & skill_code) <> 0
        and exists (select 1 from skillcodes where category = 'Front End' and (code & skill_code) <> 0) then 'A' 
        when ((select code from skillcodes where name = 'C#') & skill_code) <> 0 then 'B'
        when exists (select 1 from skillcodes where category = 'Front End' and (code & skill_code) <> 0) then 'C' 
    end grade, 
    id,
    email 
from developers) x
where grade is not null
order by grade, id
