-- 코드를 입력하세요
SELECT ri.rest_id, rest_name, food_type, favorites, address, round(avg(REVIEW_SCORE), 2) score from rest_info ri
join rest_review rr on ri.rest_id = rr.rest_id
where address like '서울%'
group by rest_id
order by score desc, favorites desc