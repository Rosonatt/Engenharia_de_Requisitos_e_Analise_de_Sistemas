import re  # Importa o módulo de expressões regulares para validar senhas
from datetime import datetime  # Importa a classe datetime para registrar a hora

# Lista para armazenar os livros na biblioteca
livros = [
    {'titulo': 'O Senhor dos Anéis', 'autor': 'J.R.R. Tolkien', 'genero': 'Fantasia', 'disponivel': True},
    {'titulo': '1984', 'autor': 'George Orwell', 'genero': 'Ficção Científica', 'disponivel': True},
    {'titulo': 'Dom Casmurro', 'autor': 'Machado de Assis', 'genero': 'Literatura Brasileira', 'disponivel': True},
    {'titulo': 'A Revolução dos Bichos', 'autor': 'George Orwell', 'genero': 'Fábula', 'disponivel': True},
    {'titulo': 'O Pequeno Príncipe', 'autor': 'Antoine de Saint-Exupéry', 'genero': 'Fábula', 'disponivel': True},
    {'titulo': 'Harry Potter e a Câmara Secreta', 'autor': 'J.K. Rowling', 'genero': 'Fantasia', 'disponivel': True},
    {'titulo': 'Um Amor para Recordar', 'autor': 'Nicholas Sparks', 'genero': 'Romance', 'disponivel': True},
    {'titulo': 'Coraline', 'autor': 'Neil Gaiman', 'genero': 'Fantasia Dark', 'disponivel': True},
]

# Dicionário para armazenar os usuários registrados
usuarios = {}

# Dicionário para armazenar as senhas dos usuários registrados
senhas = {}

# Dicionário para registrar ações no sistema
registro_atividades = []

# Definição do administrador
ADMIN_NOME = "admin"  # Nome do administrador
ADMIN_SENHA = "Admin@123"  # Senha do administrador (pré-definida)

def adicionar_livro(titulo:str, autor:str, genero:str):
    """
    Adiciona um livro à lista de livros.

    Parâmetros:
    titulo (str): Título do livro.
    autor (str): Autor do livro.
    genero (str): Gênero do livro.
    """
    livro = {
        'titulo': titulo,
        'autor': autor,
        'genero': genero,
        'disponivel': True  # O livro está disponível por padrão
    }
    livros.append(livro)
    print(f'Livro "{titulo}" adicionado com sucesso!')

def remover_livro(titulo:str):
    """
    Remove um livro da lista de livros com base no título.

    Parâmetros:
    titulo (str): Título do livro a ser removido.
    """
    global livros  # Indica que vamos modificar a lista global 'livros'
    livros = [livro for livro in livros if livro['titulo'] != titulo]
    print(f'Livro "{titulo}" removido com sucesso!')

def listar_livros():
    """
    Lista todos os livros disponíveis na biblioteca, incluindo seu status.
    """
    if not livros:
        print("Nenhum livro disponível.")
        return
    for livro in livros:
        status = "Disponível" if livro['disponivel'] else "Emprestado"  # Define o status do livro
        print(f'Título: {livro["titulo"]}, Autor: {livro["autor"]}, Gênero: {livro["genero"]}, Status: {status}')

def procurar_livro():
    """
    Permite ao usuário buscar livros por título, autor ou gênero.
    """
    print("Escolha o critério de busca:")
    print("1. Título")
    print("2. Autor")
    print("3. Gênero")
    
    opcao = input("Digite o número da opção desejada: ")

    if opcao == '1':
        titulo = input("Digite o título do livro que deseja procurar: ")
        livros_filtrados = [livro for livro in livros if titulo.lower() in livro['titulo'].lower()]
    elif opcao == '2':
        autor = input("Digite o autor do livro que deseja procurar: ")
        livros_filtrados = [livro for livro in livros if autor.lower() in livro['autor'].lower()]
    elif opcao == '3':
        genero = input("Digite o gênero do livro que deseja procurar: ")
        livros_filtrados = [livro for livro in livros if genero.lower() in livro['genero'].lower()]
    else:
        print("Opção inválida. Tente novamente.")
        return

    if not livros_filtrados:
        print("Nenhum livro encontrado com os critérios fornecidos.")
        return
    
    for livro in livros_filtrados:
        status = "Disponível" if livro['disponivel'] else "Emprestado"  # Atualiza o status
        print(f'Título: {livro["titulo"]}, Autor: {livro["autor"]}, Gênero: {livro["genero"]}, Status: {status}')

def registrar_usuario(nome:str, senha:str):
    """
    Registra um novo usuário.

    Parâmetros:
    nome (str): Nome do usuário.
    senha (str): Senha do usuário.
    """
    if nome in usuarios:  # Verifica se o usuário já está registrado
        print(f'Usuário "{nome}" já está registrado.')
        return

    # Validação da senha
    if not validar_senha(senha):
        print("A senha deve conter pelo menos uma letra maiúscula, uma letra minúscula e um caractere especial.")
        return

    usuarios[nome] = []  # Adiciona o usuário ao dicionário de usuários
    senhas[nome] = senha  # Adiciona a senha ao dicionário de senhas
    print(f'Usuário "{nome}" registrado com sucesso!')

def validar_senha(senha:str):
    """
    Valida se a senha atende aos critérios de segurança.

    Parâmetros:
    senha (str): A senha a ser validada.

    Retorna:
    bool: Verdadeiro se a senha for válida, falso caso contrário.
    """
    # A senha deve conter pelo menos uma letra maiúscula, uma letra minúscula e um caractere especial
    if (re.search(r"[a-z]", senha) and 
        re.search(r"[A-Z]", senha) and 
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha)):
        return True
    return False

def login(nome:str, senha:str):
    """
    Realiza o login de um usuário.

    Parâmetros:
    nome (str): Nome do usuário.
    senha (str): Senha do usuário.

    Retorna:
    bool: Verdadeiro se o login for bem-sucedido, falso caso contrário.
    """
    if nome in senhas and senhas[nome] == senha:  # Verifica se o nome e a senha estão corretos
        print(f'Usuário "{nome}" logado com sucesso!')
        return True
    else:
        print('Nome de usuário ou senha incorretos.')
        return False

def login_administrador(nome, senha):
    """
    Realiza o login de um administrador.

    Parâmetros:
    nome (str): Nome do administrador.
    senha (str): Senha do administrador.

    Retorna:
    bool: Verdadeiro se o login for bem-sucedido, falso caso contrário.
    """
    if nome == ADMIN_NOME and senha == ADMIN_SENHA:  # Verifica se o nome e a senha do administrador estão corretos
        print(f'Administrador "{nome}" logado com sucesso!')
        return True
    else:
        print('Nome de administrador ou senha incorretos.')
        return False

def emprestar_livro(titulo, nome_usuario):
    """
    Permite que um usuário empreste um livro.

    Parâmetros:
    titulo (str): Título do livro a ser emprestado.
    nome_usuario (str): Nome do usuário que está emprestando o livro.
    """
    if nome_usuario not in usuarios:  # Verifica se o usuário está registrado
        print(f'Usuário "{nome_usuario}" não está registrado.')
        return
    for livro in livros:  # Itera sobre a lista de livros para encontrar o livro desejado
        if livro['titulo'].lower() == titulo.lower():  # Compara títulos de forma insensível a maiúsculas
            if livro['disponivel']:  # Verifica se o livro está disponível
                livro['disponivel'] = False  # Marca o livro como não disponível
                usuarios[nome_usuario].append(titulo)  # Adiciona o livro à lista de livros emprestados do usuário
                # Registra a atividade
                registrar_atividade("Empréstimo", titulo, nome_usuario)
                print(f'Livro "{titulo}" emprestado para {nome_usuario} com sucesso!')
                return
            else:
                print(f'Livro "{titulo}" já está emprestado.')
                return
    print(f'Livro "{titulo}" não encontrado na biblioteca.')

def registrar_atividade(tipo, titulo, usuario):
    """
    Registra uma atividade no sistema.

    Parâmetros:
    tipo (str): Tipo de atividade (ex: "Empréstimo").
    titulo (str): Título do livro.
    usuario (str): Nome do usuário.
    """
    hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Obtém a hora atual
    atividade = f"{hora} - {tipo}: '{titulo}' por '{usuario}'"
    registro_atividades.append(atividade)  # Adiciona a atividade à lista de registros

def salvar_registro_atividades():
    """
    Salva o registro de atividades em um arquivo .txt ao encerrar o sistema.
    """
    with open('registro_atividades.txt', 'w', encoding='utf-8') as f:
        for atividade in registro_atividades:
            f.write(atividade + '\n')
    print("Registro de atividades salvo em 'registro_atividades.txt'.")

def menu_administrador():
    """
    Exibe o menu de opções para administradores.
    """
    while True:
        print("\n---- MENU DO ADMINISTRADOR ----")
        print("1. Adicionar Livro")
        print("2. Remover Livro")
        print("3. Listar Livros")
        print("4. Sair")
        opcao_admin = input("Escolha uma opção: ")

        if opcao_admin == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            genero = input("Digite o gênero do livro: ")
            adicionar_livro(titulo, autor, genero)  
        elif opcao_admin == '2':
            titulo = input("Digite o título do livro a ser removido: ")
            remover_livro(titulo)  
        elif opcao_admin == '3':
            listar_livros() 
        elif opcao_admin == '4':
            print("Saindo do menu do administrador.")
            break  
        else:
            print("Opção inválida. Tente novamente.")

def menu_usuario(nome_usuario):
    """
    Exibe o menu de opções para usuários.

    Parâmetros:
    nome_usuario (str): Nome do usuário logado.
    """
    while True:
        print("\n---- MENU DE USUÁRIO ----")
        print("1. Listar Livros")
        print("2. Procurar Livro (Título, Autor ou Gênero)")  # Melhoria feita pela Natalia
        print("3. Emprestar Livro")
        print("4. Sair")
        opcao_usuario = input("Escolha uma opção: ")

        if opcao_usuario == '1':
            listar_livros() 
        elif opcao_usuario == '2':
            procurar_livro()  # Chama a nova função unificada
        elif opcao_usuario == '3':
            titulo = input("Digite o título do livro a ser emprestado: ")
            emprestar_livro(titulo, nome_usuario)  
        elif opcao_usuario == '4':
            print("Saindo do menu de usuário.")
            break  
        else:
            print("Opção inválida. Tente novamente.")

def menu():
    """
    Exibe o menu principal do sistema, permitindo registro e login.
    """
    while True:
        print("\n**** MENU ****")
        print("1. Registrar Usuário")
        print("2. Login de Usuário")
        print("3. Login de Administrador")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do usuário: ")
            senha = input("Digite a senha do usuário: ")
            registrar_usuario(nome, senha)  
        elif opcao == '2':
            nome = input("Digite o nome do usuário: ")
            senha = input("Digite a senha do usuário: ")
            if login(nome, senha):  
                menu_usuario(nome)  # Chama o menu do usuário após login
        elif opcao == '3':
            nome = input("Digite o nome do administrador: ")
            senha = input("Digite a senha do administrador: ")
            if login_administrador(nome, senha):  
                menu_administrador()  # Chama o menu do administrador após login
        elif opcao == '4':
            salvar_registro_atividades()  # Salva o registro de atividades ao sair
            print("Saindo do sistema.")
            break  
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o programa chamando a função menu
menu()