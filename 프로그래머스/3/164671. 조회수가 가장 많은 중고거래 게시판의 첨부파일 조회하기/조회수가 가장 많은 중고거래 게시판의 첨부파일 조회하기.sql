-- 코드를 입력하세요
SELECT concat('/home/grep/src/', uf.board_id, '/', file_id, file_name, file_ext)file_path 
from USED_GOODS_FILE uf
join USED_GOODS_BOARD ub 
on uf.board_id = ub.board_id
where views = (select max(views) from USED_GOODS_BOARD)
order by uf.file_id desc