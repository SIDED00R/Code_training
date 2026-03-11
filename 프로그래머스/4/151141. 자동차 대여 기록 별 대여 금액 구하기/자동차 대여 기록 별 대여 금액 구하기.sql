-- 코드를 입력하세요
SELECT history_id, fee
FROM (
    SELECT
        t.history_id,
        FLOOR(t.daily_fee * t.d_diff * (100 - COALESCE(cp.dr, 0)) / 100) AS fee
    FROM (
        SELECT
            ch.history_id,
            cc.car_id,
            cc.car_type,
            cc.daily_fee,
            DATEDIFF(ch.end_date, ch.start_date) + 1 AS d_diff
        FROM CAR_RENTAL_COMPANY_CAR cc
        JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY ch
          ON cc.car_id = ch.car_id
        WHERE cc.car_type = '트럭'
    ) t
    LEFT JOIN (
        SELECT
            car_type,
            CAST(duration_type AS UNSIGNED) AS dt,
            CAST(discount_rate AS UNSIGNED) AS dr
        FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    ) cp
      ON t.car_type = cp.car_type
     AND cp.dt = CASE
                    WHEN t.d_diff >= 90 THEN 90
                    WHEN t.d_diff >= 30 THEN 30
                    WHEN t.d_diff >= 7 THEN 7
                    ELSE NULL
                 END
) total
order by fee desc, history_id desc
