CRUD de produtos com Python e MySQL.

O projeto CRUD de Produtos com Python e MySQL é uma aplicação de console desenvolvida para facilitar a gestão de um catálogo de vendas. 
O sistema permite o cadastro, consulta, edição e remoção de registros de produtos, 
proporcionando uma administração eficiente.

Funcionalidades:
Criar Produto: Adiciona um novo produto e seu valor ao banco de dados.
Ler Produtos: Exibe uma lista completa de todos os produtos e seus respectivos valores cadastrados.
Atualizar Produto: Permite alterar o valor de um produto existente.
Deletar Produto: Remove um produto do banco de dados.

Tecnologias Utilizadas:
-Python
-MySQL

Pré-requisitos
-Antes de executar este projeto, certifique-se de ter o seguinte instalado em seu computador:
-Python 3.x
-MySQL Server (ou qualquer ambiente com MySQL, como o XAMPP ou WampServer)
-A biblioteca mysql-connector-python. Você pode instalá-la usando pip:

Bash

pip install mysql-connector-python
Instalação e Configuração
Siga estes passos para colocar o projeto em funcionamento:

Clone o Repositório:
Abra o terminal e clone o projeto para o seu computador:

Bash

git clone https://github.com/Pablobr11/Crud-test.git
Navegue até o Diretório do Projeto:
Acesse a pasta do projeto:

Bash

cd Crud-test
Configuração do Banco de Dados:
Você precisa de um banco de dados chamado bdyoutube e uma tabela chamada vendas. Conecte-se ao seu MySQL e execute os seguintes comandos SQL:

SQL

CREATE DATABASE bdyoutube;

USE bdyoutube;

CREATE TABLE vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(255) NOT NULL,
    valor FLOAT NOT NULL
);
Observação: Se os seus dados de conexão (usuário, senha, host) forem diferentes de root e 1234, você precisará editar o arquivo seu_arquivo.py e atualizar a função conectar_banco() com as suas credenciais.

Como Usar
Para iniciar a aplicação, basta executar o arquivo principal do projeto no seu terminal:

Bash

python seu_arquivo.py
Após a execução, um menu interativo será exibido. Digite o número da opção desejada e pressione Enter.

--- Menu CRUD ---
1. Criar Produto
2. Ler Produtos
3. Atualizar Produto
4. Deletar Produto
5. Sair
Tecnologias Utilizadas
Python

MySQL

Autor
Feito Pablo 
GitHub: https://github.com/Pablobr11

