select count(fi.fish_type) as fish_count, name.fish_name from fish_info fi
join fish_name_info name
on fi.fish_type = name.fish_type
group by name.fish_name
order by fish_count desc