create database Saidas_SIGA
use Saidas_SIGA
CREATE TABLE SIGA
(
	Id varchar(20),
	RE_Funcionario int,
	Dia date,
	Opera��o varchar (20) not null,
	Situa��o  varchar(10),
	constraint pkSIGA primary key (Id),
	constraint fkRE foreign key 
	(RE_Funcionario) references Funcionario(RE)
)

CREATE TABLE Funcionario
(
	RE int,
	Nome varchar(50) not null,
	Maquina varchar(7),
	Monitor varchar(7),
	Senha varchar(12),
	Situa��o  varchar(10),
	Constraint pkFuncionario primary key (RE)
)