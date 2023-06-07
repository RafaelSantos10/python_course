-- limit limita a qtd de valored 
-- offset desloca o cursor para exibir os resultados
select * from users
where first_name like ('%ma%_')
order by created_at asc
limit 4 offset 2;