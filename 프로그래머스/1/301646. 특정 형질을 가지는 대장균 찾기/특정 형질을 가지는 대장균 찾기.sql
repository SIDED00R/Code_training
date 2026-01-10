-- 코드를 작성해주세요
select count(*) as count from ecoli_data
where genotype % 8 in (1, 4, 5)