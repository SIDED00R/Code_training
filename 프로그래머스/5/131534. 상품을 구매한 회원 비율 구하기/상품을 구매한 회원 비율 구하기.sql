-- 코드를 입력하세요
SELECT year(SALES_DATE) year, month(SALES_DATE) month, count(distinct os.user_id) purchased_users, 
round(count(distinct os.user_id) / (select count(*) from user_info where year(joined) = 2021), 1) puchased_ratio 
from online_sale os
join (select user_id from user_info where year(joined) = 2021) ui on os.user_id = ui.user_id
group by year, month
order by year, month