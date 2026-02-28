-- 코드를 작성해주세요
select hd.dept_id, hd.dept_name_en, round(avg(sal)) avg_sal from hr_department hd
join hr_employees he on hd.dept_id = he.dept_id
group by dept_id, dept_name_en
order by avg_sal desc