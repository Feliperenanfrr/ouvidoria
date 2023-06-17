# Ouvidoria

## Operações BD

Pacote que possui todos os métodos utilizados para fazer operações no banco de dados, sendo eles:

- **Abrir banco de dados**

    *Tem como função estabelecer a conexão com o banco de dados*

    * Recebe como parâmetros: 
        - host (Máquina do banco de dados)
        - User (Usuário que irá ter acesso ao banco de dados)
        - Password (Senha do banco de dados)
        - Database (Nome do banco de dados)
        
- **Encerrar banco de dados**

    *Tem como função encerrar a conexão com o banco de dados após a utilização*
    - Recebe como parâmetros:
        - Conexão
    
- **Insert no banco de dados**

    *Tem como função inserir ocorrências no banco de dados da ouvidoria*
    - Recebe como parâmetros:
        - Connection (Variável de conexão com o banco de dados)
        - Sql (Consulta em linguagem sql)
        - dados (Dados que serão inseridos no banco de dados)
        
        