# 📒 Sistema de Agenda de Contatos

Sistema de gerenciamento de contatos desenvolvido em Python com integração direta ao PostgreSQL. Permite cadastrar, listar, buscar e deletar contatos via terminal, com os dados persistidos em banco de dados relacional.

## 📋 Funcionalidades

- Cadastrar contato com nome, email e telefone
- Listar todos os contatos cadastrados
- Buscar contato pelo nome
- Deletar contato pelo email com validação de existência
- Validação de entradas inválidas no menu

## 🛠️ Tecnologias utilizadas

- Python 3
- PostgreSQL 16
- [Psycopg2](https://pypi.org/project/psycopg2-binary/) — driver de conexão Python + PostgreSQL

## ▶️ Como executar

**1. Clone o repositório**
```bash
git clone https://github.com/kaiquexrr/sistema-de-cadastro.git
cd sistema-de-cadastro
```

**2. Crie e ative o ambiente virtual**
```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Instale a dependência**
```bash
pip install psycopg2-binary
```

**4. Configure o banco de dados**

Acesse o PostgreSQL e crie o banco e a tabela:
```sql
CREATE DATABASE agenda;
\c agenda
CREATE TABLE contatos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(20)
);
```

**5. Configure a conexão**

No arquivo `agenda.py`, ajuste as credenciais conforme seu ambiente:
```python
conn = psycopg2.connect(
    dbname="agenda",
    user="seu_usuario",
    password="sua_senha",
    host="localhost"
)
```

**6. Execute o programa**
```bash
python3 agenda.py
```

## 🖥️ Como usar

Ao executar, o menu aparece no terminal:

```
[1] cadastrar contatos
[2] listar contatos
[3] buscar contatos
[4] deletar contatos
[5] sair
```

## 💡 Conceitos aplicados

- Integração Python com banco de dados relacional via psycopg2
- Operações CRUD completas com SQL puro — INSERT, SELECT, UPDATE, DELETE
- Uso de placeholders `%s` para prevenção de SQL Injection
- Validação de existência antes de deletar registros
- Tratamento de exceções com `try/except`
- Ambiente virtual com venv
- Estrutura com `if __name__ == '__main__'`

## 📌 Melhorias futuras

- [ ] Usar variáveis de ambiente para as credenciais do banco
- [ ] Adicionar atualização de contatos
- [ ] Busca por email além do nome
- [ ] Exportar contatos para arquivo CSV

---

Desenvolvado por [Kaique](https://github.com/kaiquexrr) durante os estudos de Python e PostgreSQL.