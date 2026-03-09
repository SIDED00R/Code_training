-- 코드를 작성해주세요
select id, fish_name, length from (select id, fi1.fish_type, fi1.length from fish_info fi1
                                   join (select fish_type, max(length) length from fish_info
                                         group by fish_type) fi2
                                   on fi1.fish_type = fi2.fish_type and fi1.length = fi2.length) fi
join fish_name_info fni on fi.fish_type = fni.fish_type
order by id