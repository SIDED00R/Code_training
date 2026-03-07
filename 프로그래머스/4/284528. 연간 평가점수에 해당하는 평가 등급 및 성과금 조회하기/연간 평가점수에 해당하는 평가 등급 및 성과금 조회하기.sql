-- 코드를 작성해주세요
select he.emp_no, emp_name, 
case when hg.score >= 96 then 'S'
when hg.score >= 90 then 'A'
when hg.score >= 80 then 'B'
else 'C' end grade, 
case when hg.score >= 96 then sal * 0.2
when hg.score >= 90 then sal * 0.15
when hg.score >= 80 then sal * 0.1
else 0 end bonus 
from hr_employees he
join (select emp_no, avg(score) score from hr_grade
group by emp_no) hg 
on he.emp_no = hg.emp_no

