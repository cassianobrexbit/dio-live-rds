# Bancos de Dados Relacionais (SQL) na AWS com Amazon RDS
Repositório para o Live Coding DIO do dia 24/11/2021

## Serviços utilizados

- Amazon RDS
- AWS Lambda
- MySQL Workbench

## Criando o banco de dados no Amazon RDS

- AWS Console -> Amazon RDS -> Create database -> Standard create -> MySQL -> Versão padrão -> Free Tier -> DB instance identifier [dio-live-db] -> Master username [admin] -> Master password [sua_senha_forte] -> DB instance size - padrão -> Storage - configurações padrão -> Connectivity - vpc padrão -> Publicly accessible [yes] -> VPC Security - padrão -> Database authentication [password authentication] -> Create database
- Selecionar o DB criado -> Connectivity & security -> Copiar endpoint.

### No MySQL Workbench

- MySQL Connections -> New -> Connection name [DioLive] -> Hostname - colar o endpoint copiado no passo anterior -> Username [admin] -> Teste Connection -> Password [sua_senha]

#### Em caso de problemas na conexão

- Security -> VPC security groups -> Acessar o SG criado -> Inbound -> Edit -> Add rule -> type [All traffic] -> Source [Anywhere] -> Save

### No MySQL Workbench

- Selecionar a conexão criada -> Password [sua_senha_forte]

## Criando queries

 - Criar um database:
 
    ```CREATE DATABASE ORDERS_DB;```

- Acessar o db criado

    ```USE ORDERS_DB;```

- Criar uma tabela de produtos

    ```
    CREATE TABLE PRODUCTS (
      id INT PRIMARY KEY,
      value DECIMAL(15,2) NOT NULL
    );
    ```
    
- Criar uma tabela de carrinho de compras
    
    ```
    CREATE TABLE CARTS (
      id INT PRIMARY KEY,
      user_id INT NOT NULL
    );
    ```
- Criar uma tabela associativa de itens em um carrinho de compras

    ```
    CREATE TABLE ITEMS (
      cart_id INT NOT NULL,
      product_id INT NOT NULL,
      quantity DECIMAL(15,2) NOT NULL,
      FOREIGN KEY (cart_id) REFERENCES CARTS (id),
      FOREIGN KEY (product_id) REFERENCES PRODUCTS (id)
    );
    ```
- Descrevendo o esquema de uma tabela 
 
    ```
    DESC [table_name];
    ```
  
- Inserindo dados em tabelas

  ```
  INSERT INTO CARTS (id, user_id) VALUES (1,1);
  ```
  ```
  INSERT INTO PRODUCTS (id, value) VALUES (1,200);
  ```
  
  ```
  INSERT INTO ITEMS (cart_id, product_id, quantity) VALUES (1,1, 300);
  ```
  
- Selecionando todos os registros de uma tabela

  ```
  SELECT * FROM [table_name];
  ```

