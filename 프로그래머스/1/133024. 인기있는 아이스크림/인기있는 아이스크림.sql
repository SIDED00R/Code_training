-- 코드를 입력하세요
SELECT flavor
from first_half
group by flavor
order by SUM(TOTAL_ORDER) desc, shipment_id asc