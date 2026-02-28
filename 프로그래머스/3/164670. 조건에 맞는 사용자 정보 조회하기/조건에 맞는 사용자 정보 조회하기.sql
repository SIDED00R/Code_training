-- 코드를 입력하세요
SELECT 
    uu.user_id,
    uu.nickname,
    CONCAT(uu.CITY, ' ', uu.STREET_ADDRESS1, ' ', uu.STREET_ADDRESS2) AS 전체주소,
    CONCAT(
        SUBSTRING(uu.TLNO, 1, 3), '-',
        SUBSTRING(uu.TLNO, 4, 4), '-',
        SUBSTRING(uu.TLNO, 8, 4)
    ) AS 전화번호
FROM used_goods_user uu
JOIN (
    SELECT WRITER_ID
    FROM used_goods_board
    GROUP BY WRITER_ID
    HAVING COUNT(*) >= 3
) ub
ON uu.user_id = ub.WRITER_ID
ORDER BY uu.user_id desc