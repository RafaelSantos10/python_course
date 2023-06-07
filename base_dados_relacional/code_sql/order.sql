-- order ordena
select * from users
where first_name like ('%ma%_')
order by created_at asc;