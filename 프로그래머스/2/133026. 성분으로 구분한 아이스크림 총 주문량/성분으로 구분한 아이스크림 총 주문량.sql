-- 코드를 입력하세요
SELECT ii.ingredient_type, sum(ff.total_order) as total_order from first_half as ff
join icecream_info as ii
on ff.flavor = ii.flavor
group by ii.ingredient_type
order by ff.total_order
