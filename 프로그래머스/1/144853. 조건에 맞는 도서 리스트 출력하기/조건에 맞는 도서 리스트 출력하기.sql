-- 코드를 입력하세요
SELECT book_id, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE from book
where book_id in (3, 4) and PUBLISHED_DATE >= '2021-01-01' and PUBLISHED_DATE < '2022-01-01' and category = '인문'
order by published_date