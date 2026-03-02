-- 코드를 입력하세요
SELECT apnt_no, p.pt_name, a.pt_no, a.mcdp_cd, dr_name, apnt_ymd from appointment a
join patient p on a.pt_no = p.pt_no
join doctor d on d.dr_id = a.mddr_id
where apnt_ymd >= '2022-04-13' and apnt_ymd < '2022-04-14' and a.mcdp_cd = 'CS' and a.APNT_CNCL_YN = 'N'
order by apnt_ymd