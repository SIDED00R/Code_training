with recursive tree as(
    select id, parent_id, 1 as generation from ecoli_data where parent_id is null
    union all
    select ed.id, ed.parent_id, tree.generation + 1 as generation
    from ecoli_data ed
    join tree on ed.parent_id = tree.id
)

select count(*) count, generation from (select * from tree
where id not in (select parent_id from ecoli_data where parent_id is not null)) t
group by generation