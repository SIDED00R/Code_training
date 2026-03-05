-- 코드를 작성해주세요
select count(1) fish_count, max(length) max_length, fi1.fish_type from fish_info fi1
join (select fish_type, avg(case when length is null then 10 else length end) l from fish_info group by fish_type having l >= 33) fi2
on fi1.fish_type = fi2.fish_type
group by fish_type
order by fish_type
