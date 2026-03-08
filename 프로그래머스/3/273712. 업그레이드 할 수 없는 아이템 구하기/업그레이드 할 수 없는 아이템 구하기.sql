-- 코드를 작성해주세요
select item_id, item_name, rarity from item_info
where item_id not in (select distinct ii.item_id from item_info ii
join item_tree it on ii.item_id = it.PARENT_ITEM_ID)
order by item_id desc