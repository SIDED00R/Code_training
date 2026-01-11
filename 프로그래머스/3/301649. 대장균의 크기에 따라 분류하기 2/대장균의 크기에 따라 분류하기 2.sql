-- 코드를 작성해주세요
SELECT id, 
case when grp = 1 then "CRITICAL"
when grp = 2 then "HIGH"
when grp = 3 then "MEDIUM"
else "LOW" end as colony_name
FROM (
    SELECT *,
           NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC) AS grp
    FROM ECOLI_DATA 
) t
order by id
