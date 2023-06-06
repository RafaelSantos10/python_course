-- isso é um comentário
# outro comentário
/* mais um comentário  */

-- Seleciona a base de dados
use base_de_dados;

-- mostra as tabelas da base de dados 
show tables;

-- descreve as colunas da tabela
describe users;

-- inserir registros na base de dados
insert INTO users (first_name, last_name, email, password_hash) 
values ("João", "Lucas", "joaolucas@gmail.com", "joaolucas"),
("Maria", "Carvalho", "mariacarvalho@gmail.com", "mariacarvalho"),
("Helena", "Maria", "helenamaria@gmail.com", "helenamaria");

