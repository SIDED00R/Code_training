-- 코드를 입력하세요
SELECT id, name, p1.host_id from places p1
join (select count(*) c, host_id from places group by host_id having c >= 2) p2
on p1.host_id = p2.host_id