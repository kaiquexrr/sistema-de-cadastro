import psycopg2

conn = psycopg2.connect(
    dbname="agenda",
    user="postgres",
    password="103115",
    host="localhost"
)


def cadastrar_contato(nome,email,telefone):
    cursor = conn.cursor()
    cursor.execute(
            "INSERT INTO contatos (nome, email ,telefone) VALUES (%s, %s, %s)",
            (nome,email,telefone)
    )
    conn.commit()
    print(f'contato {nome} cadastrado com sucesso!')


def listar_contatos():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()
    
    if not contatos:
        print("nenhum contato cadastrado")
    else:
        for contato in contatos:
            print(f"ID:{contato[0]} nome: {contato[1]} email: {contato[2]} telefone:{contato[3]}")


def buscar_contato(nome):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contatos WHERE nome = %s",(nome,))
    contatos = cursor.fetchall()

    if not contatos:
        print("desculpa mas esse contato nao existe")
    else:
        print(contatos)


def deletar_contato(email):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contatos where email = %s",(email,))
    contato = cursor.fetchone()

    if not contato:
        print("contato nao encontrado")
    else:
        cursor.execute("DELETE FROM contatos WHERE email = %s",(email,))
        conn.commit()
        print(f'contato deletado com sucesso!')

    
def menu():
    while True:
        print('[1] cadastrar contatos')
        print('[2] listar contatos')
        print('[3] buscar contatos')
        print('[4] deletar contatos')
        print('[5] sair')
        try:
            resposta = int(input(''))
        except ValueError:
            print('digite um numero valido')
            continue

        if resposta == 1:
            nome = input('nome:')
            email = input('email:')
            telefone = input('telefone:')
            cadastrar_contato(nome,email,telefone)
        elif resposta == 2:
            listar_contatos()
        elif resposta ==3:
            buscar_contato(input('digite o nome:'))
        elif resposta == 4:
            deletar_contato(input('digite o email:'))
        elif resposta == 5:
            break
        else:
            print('opcao invalida digite novamente')

if __name__ == '__main__':
    menu()