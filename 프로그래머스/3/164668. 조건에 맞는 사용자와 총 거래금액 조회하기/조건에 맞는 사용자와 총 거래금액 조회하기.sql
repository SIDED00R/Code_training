-- 코드를 입력하세요
SELECT uu.user_id, uu.nickname, sum(ub.price) as total_sales from USED_GOODS_USER  uu
join USED_GOODS_BOARD ub on uu.USER_ID = ub.WRITER_ID
where status = "DONE"
group by user_id
having total_sales >= 700000
order by total_sales