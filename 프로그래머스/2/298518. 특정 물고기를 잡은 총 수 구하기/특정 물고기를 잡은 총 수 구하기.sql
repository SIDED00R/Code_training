-- 코드를 작성해주세요
select count(*) as fish_count from fish_info fi
join fish_name_info name
on fi.fish_type = name.fish_type
where name.fish_name in ('bass', 'snapper')
