-- in seleciona elementos entres os valores enviados
select * from users
where id in (10,15,20,25,30) and 
first_name in ('Keelie', 'Xyla');