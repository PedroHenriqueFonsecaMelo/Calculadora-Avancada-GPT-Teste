import pandas as pd
import numpy as np

class Biblioteca:
    def __init__(self):
        # Usando pandas para criar um DataFrame de livros
        self.livros = pd.DataFrame(columns=["ID", "Título", "Autor", "Ano", "Disponível"])
        
        # Usando numpy para gerar IDs de clientes
        self.clientes = pd.DataFrame(columns=["ID", "Nome", "Empréstimos"])

    def adicionar_livro(self, titulo, autor, ano):
        id_livro = len(self.livros) + 1
        novo_livro = pd.DataFrame([[id_livro, titulo, autor, ano, True]], columns=self.livros.columns)
        self.livros = pd.concat([self.livros, novo_livro], ignore_index=True)
        print(f'Livro "{titulo}" adicionado com sucesso!')

    def registrar_cliente(self, nome):
        id_cliente = np.random.randint(1000, 9999)
        novo_cliente = pd.DataFrame([[id_cliente, nome, []]], columns=self.clientes.columns)
        self.clientes = pd.concat([self.clientes, novo_cliente], ignore_index=True)
        print(f'Cliente "{nome}" registrado com sucesso!')

    def listar_livros(self):
        print("\nLivros disponíveis para empréstimo:")
        livros_disponiveis = self.livros[self.livros["Disponível"] == True]
        if livros_disponiveis.empty:
            print("Nenhum livro disponível.")
        else:
            print(livros_disponiveis[["ID", "Título", "Autor", "Ano"]])

    def listar_clientes(self):
        print("\nClientes registrados:")
        print(self.clientes[["ID", "Nome"]])

    def pegar_emprestado(self, id_cliente, id_livro):
        livro = self.livros[self.livros["ID"] == id_livro]
        cliente = self.clientes[self.clientes["ID"] == id_cliente]

        if livro.empty:
            print("Livro não encontrado!")
            return

        if cliente.empty:
            print("Cliente não encontrado!")
            return

        if livro["Disponível"].values[0] == False:
            print("O livro não está disponível para empréstimo.")
            return

        # Atualizando a disponibilidade do livro e adicionando ao histórico do cliente
        self.livros.loc[self.livros["ID"] == id_livro, "Disponível"] = False
        self.clientes.loc[self.clientes["ID"] == id_cliente, "Empréstimos"].values[0].append(id_livro)

        print(f'O livro "{livro["Título"].values[0]}" foi emprestado para {cliente["Nome"].values[0]}.')

    def devolver_livro(self, id_cliente, id_livro):
        livro = self.livros[self.livros["ID"] == id_livro]
        cliente = self.clientes[self.clientes["ID"] == id_cliente]

        if livro.empty:
            print("Livro não encontrado!")
            return

        if cliente.empty:
            print("Cliente não encontrado!")
            return

        if id_livro not in cliente["Empréstimos"].values[0]:
            print(f'O cliente {cliente["Nome"].values[0]} não tem este livro emprestado.')
            return

        # Devolvendo o livro
        self.livros.loc[self.livros["ID"] == id_livro, "Disponível"] = True
        self.clientes.loc[self.clientes["ID"] == id_cliente, "Empréstimos"].values[0].remove(id_livro)

        print(f'O livro "{livro["Título"].values[0]}" foi devolvido por {cliente["Nome"].values[0]}.')

    def menu(self):
        while True:
            print("\n--- Menu da Biblioteca ---")
            print("1. Adicionar Livro")
            print("2. Registrar Cliente")
            print("3. Listar Livros Disponíveis")
            print("4. Listar Clientes")
            print("5. Emprestar Livro")
            print("6. Devolver Livro")
            print("7. Sair")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                titulo = input("Título do livro: ")
                autor = input("Autor do livro: ")
                ano = input("Ano de publicação: ")
                self.adicionar_livro(titulo, autor, int(ano))

            elif escolha == "2":
                nome = input("Nome do cliente: ")
                self.registrar_cliente(nome)

            elif escolha == "3":
                self.listar_livros()

            elif escolha == "4":
                self.listar_clientes()

            elif escolha == "5":
                id_cliente = int(input("ID do cliente: "))
                id_livro = int(input("ID do livro: "))
                self.pegar_emprestado(id_cliente, id_livro)

            elif escolha == "6":
                id_cliente = int(input("ID do cliente: "))
                id_livro = int(input("ID do livro: "))
                self.devolver_livro(id_cliente, id_livro)

            elif escolha == "7":
                print("Saindo do sistema...")
                break

            else:
                print("Opção inválida! Tente novamente.")


# Criando uma instância da biblioteca e iniciando o menu
biblioteca = Biblioteca()
biblioteca.menu()
