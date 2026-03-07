-- 코드를 입력하세요
select flavor 
from (SELECT fh.flavor, (fh.total_order + j.total_order) total 
      from first_half fh
      join (select flavor, sum(total_order) total_order
           from july
           group by flavor) j 
      on fh.flavor = j.flavor
      order by total desc limit 3) t
