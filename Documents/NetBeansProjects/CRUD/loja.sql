-- Remove o BANCO DE DADOS caso exista, e o cria novamente
	drop schema if exists loja;

-- Criação do Banco de Dados
	create schema loja;

-- Habilitar (abrir) o Banco de Dados LOJA para USO
	use loja;
    
-- Criando a tabela de jogos
	create table Jogos(
		ID_jogo int primary key not null auto_increment,
		titulo varchar(50) not null,
        descricao varchar(100) not null,
        ID_genero int not null,
		preco double not null,
        estoque int not null,
        desenvolvedor varchar(50) not null,
        foreign key (ID_genero) references Genero(ID_genero)
    
    );
    
    create table Genero(
		ID_genero int primary key not null auto_increment,
        nome varchar(30) not null
	);
    