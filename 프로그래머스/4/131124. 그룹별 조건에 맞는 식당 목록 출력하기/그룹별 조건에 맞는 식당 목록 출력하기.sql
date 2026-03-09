-- 코드를 입력하세요
select mp.member_name, review_text, date_format(review_date, '%Y-%m-%d') review_date from member_profile mp
join ( 
    select rr1.member_id, review_text, review_date from rest_review rr1
    join (select member_id, count(*) c from rest_review
          group by member_id
          order by c desc
          limit 1) rr2
    on rr1.member_id = rr2.member_id
    ) rr
on mp.member_id = rr.member_id
order by review_date, review_text