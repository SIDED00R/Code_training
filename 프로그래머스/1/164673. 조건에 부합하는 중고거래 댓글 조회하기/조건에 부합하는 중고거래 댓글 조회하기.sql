-- 코드를 입력하세요
SELECT ugb.title, ugb.BOARD_ID, ugr.REPLY_ID, ugr.WRITER_ID, ugr.CONTENTS, Date_format(ugr.CREATED_DATE, "%Y-%m-%d") as CREATED_DATE
from USED_GOODS_REPLY as ugr
join USED_GOODS_BOARD as ugb
on ugr.board_id = ugb.board_id
where ugb.created_date >= "2022-10-01" and ugb.created_date < "2022-11-01"
order by CREATED_DATE, ugb.title
