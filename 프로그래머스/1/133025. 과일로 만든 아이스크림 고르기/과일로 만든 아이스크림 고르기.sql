-- 코드를 입력하세요
SELECT ii.FLAVOR from icecream_info ii
join first_half fh
on ii.FLAVOR = fh.FLAVOR
where fh.total_order > 3000 and ii.INGREDIENT_TYPE = 'fruit_based'
