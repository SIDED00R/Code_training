-- 코드를 작성해주세요
select id, (case when child_count is null then 0 else child_count end) child_count from ecoli_data ed1
left join (select parent_id, count(*) child_count from ecoli_data
group by parent_id) ed2
on ed1.id = ed2.parent_id
order by id


