import math
import numpy as np
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import print
from rich import box


class CalculadoraAvancada:
    def __init__(self):
        self.histórico = []  # Histórico de operações realizadas
        self.console = Console()  # Console para exibir as informações formatadas

    # Funções de operações com números
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Erro: Divisão por zero!"
        return a / b

    def exponenciar(self, a, b):
        return a ** b

    def raiz(self, a):
        if a < 0:
            return "Erro: Não é possível calcular a raiz quadrada de um número negativo!"
        return a ** 0.5

    def fatorial(self, a):
        if a < 0:
            return "Erro: Não é possível calcular fatorial de número negativo!"
        return math.factorial(int(a))

    # Funções de operações com vetores
    def somar_vetores(self, a, b):
        if len(a) != len(b):
            return "Erro: Os vetores precisam ter o mesmo tamanho!"
        return np.add(a, b)

    def subtrair_vetores(self, a, b):
        if len(a) != len(b):
            return "Erro: Os vetores precisam ter o mesmo tamanho!"
        return np.subtract(a, b)

    def multiplicar_vetor_escalar(self, vetor, escalar):
        return np.multiply(vetor, escalar)

    def produto_escalar(self, a, b):
        if len(a) != len(b):
            return "Erro: Os vetores precisam ter o mesmo tamanho!"
        return np.dot(a, b)

    # Função para resolver equação do 2º grau
    def resolver_equacao_2_grau(self, a, b, c):
        delta = b**2 - 4*a*c
        if delta < 0:
            return "Erro: A equação não possui raízes reais."
        elif delta == 0:
            x = -b / (2*a)
            return f"Raiz única: x = {x}"
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return f"Raízes: x1 = {x1} e x2 = {x2}"

    # Funções para resolver progressões
    def progressao_aritmetica(self, a1, r, n):
        pa = [a1 + (i * r) for i in range(n)]
        return pa

    def progressao_geometrica(self, a1, r, n):
        pg = [a1 * (r ** i) for i in range(n)]
        return pg

    # Função para salvar histórico
    def salvar_histórico(self, operação, entrada, resultado):
        self.histórico.append({"Operação": operação, "Entrada": entrada, "Resultado": resultado})

    # Função para mostrar o histórico
    def mostrar_histórico(self):
        table = Table(title="Histórico de Operações")
        table.add_column("Operação", style="cyan", justify="center")
        table.add_column("Entrada", style="magenta", justify="center")
        table.add_column("Resultado", style="green", justify="center")

        for item in self.histórico:
            table.add_row(item["Operação"], item["Entrada"], str(item["Resultado"]))
        
        self.console.print(table)
    def exibir_menu(self):
        
        # Criando a tabela para o menu com 4 colunas
        table = Table(title="Calculadora Avançada", box=box.ROUNDED)
        table.add_column("Opção", justify="center", style="bold cyan")
        table.add_column("Operação", justify="center", style="bold magenta")
        table.add_column("Opção", justify="center", style="bold cyan")
        table.add_column("Operação", justify="center", style="bold magenta")

        # Adicionando as operações à tabela, divididas em 4 colunas
        operacoes = [
            ("1", "Somar", "2", "Subtrair"),
            ("3", "Multiplicar", "4", "Dividir"),
            ("5", "Exponenciar", "6", "Raiz quadrada"),
            ("7", "Fatorial", "8", "Somar vetores"),
            ("9", "Subtrair vetores", "10", "Multiplicar vetor por escalar"),
            ("11", "Produto escalar de vetores", "12", "Resolver equação do 2º grau"),
            ("13", "Progressão Aritmética", "14", "Progressão Geométrica"),
            ("15", "Mostrar histórico", "16", "Sair")
        ]
        for row in operacoes:
            table.add_row(*row)

        # Exibindo a tabela
        self.console.print(table)

    # Função de menu interativo
    def menu(self):
        while True:
            self.exibir_menu()
            escolha = Prompt.ask("Escolha uma operação (1-16)", show_choices=False)


            if escolha == "1":
                a = float(Prompt.ask("Digite o primeiro número"))
                b = float(Prompt.ask("Digite o segundo número"))
                resultado = self.somar(a, b)
                self.console.print(f"[green]{a} + {b} = {resultado}[/green]")
                self.salvar_histórico("Soma", f"{a} + {b}", resultado)

            elif escolha == "2":
                a = float(Prompt.ask("Digite o primeiro número"))
                b = float(Prompt.ask("Digite o segundo número"))
                resultado = self.subtrair(a, b)
                self.console.print(f"[green]{a} - {b} = {resultado}[/green]")
                self.salvar_histórico("Subtração", f"{a} - {b}", resultado)

            elif escolha == "3":
                a = float(Prompt.ask("Digite o primeiro número"))
                b = float(Prompt.ask("Digite o segundo número"))
                resultado = self.multiplicar(a, b)
                self.console.print(f"[green]{a} * {b} = {resultado}[/green]")
                self.salvar_histórico("Multiplicação", f"{a} * {b}", resultado)

            elif escolha == "4":
                a = float(Prompt.ask("Digite o primeiro número"))
                b = float(Prompt.ask("Digite o segundo número"))
                resultado = self.dividir(a, b)
                self.console.print(f"[green]{a} / {b} = {resultado}[/green]")
                self.salvar_histórico("Divisão", f"{a} / {b}", resultado)

            elif escolha == "5":
                a = float(Prompt.ask("Digite a base"))
                b = float(Prompt.ask("Digite o expoente"))
                resultado = self.exponenciar(a, b)
                self.console.print(f"[green]{a} ^ {b} = {resultado}[/green]")
                self.salvar_histórico("Exponenciação", f"{a} ^ {b}", resultado)

            elif escolha == "6":
                a = float(Prompt.ask("Digite o número"))
                resultado = self.raiz(a)
                self.console.print(f"[green]Raiz quadrada de {a} = {resultado}[/green]")
                self.salvar_histórico("Raiz quadrada", f"√{a}", resultado)

            elif escolha == "7":
                a = float(Prompt.ask("Digite o número para o fatorial"))
                resultado = self.fatorial(a)
                self.console.print(f"[green]Fatorial de {a} = {resultado}[/green]")
                self.salvar_histórico("Fatorial", f"{a}!", resultado)

            elif escolha == "8":
                a = list(map(float, Prompt.ask("Digite os elementos do primeiro vetor separados por espaço").split()))
                b = list(map(float, Prompt.ask("Digite os elementos do segundo vetor separados por espaço").split()))
                resultado = self.somar_vetores(a, b)
                self.console.print(f"[green]Resultado da soma dos vetores: {resultado}[/green]")
                self.salvar_histórico("Soma de vetores", f"{a} + {b}", resultado)

            elif escolha == "9":
                a = list(map(float, Prompt.ask("Digite os elementos do primeiro vetor separados por espaço").split()))
                b = list(map(float, Prompt.ask("Digite os elementos do segundo vetor separados por espaço").split()))
                resultado = self.subtrair_vetores(a, b)
                self.console.print(f"[green]Resultado da subtração dos vetores: {resultado}[/green]")
                self.salvar_histórico("Subtração de vetores", f"{a} - {b}", resultado)

            elif escolha == "10":
                vetor = list(map(float, Prompt.ask("Digite os elementos do vetor separados por espaço").split()))
                escalar = float(Prompt.ask("Digite o valor do escalar"))
                resultado = self.multiplicar_vetor_escalar(vetor, escalar)
                self.console.print(f"[green]Resultado da multiplicação do vetor por escalar: {resultado}[/green]")
                self.salvar_histórico("Multiplicação de vetor por escalar", f"{vetor} * {escalar}", resultado)

            elif escolha == "11":
                a = list(map(float, Prompt.ask("Digite os elementos do primeiro vetor separados por espaço").split()))
                b = list(map(float, Prompt.ask("Digite os elementos do segundo vetor separados por espaço").split()))
                resultado = self.produto_escalar(a, b)
                self.console.print(f"[green]Resultado do produto escalar: {resultado}[/green]")
                self.salvar_histórico("Produto escalar", f"{a} . {b}", resultado)

            elif escolha == "12":
                a = float(Prompt.ask("Digite o valor de a"))
                b = float(Prompt.ask("Digite o valor de b"))
                c = float(Prompt.ask("Digite o valor de c"))
                resultado = self.resolver_equacao_2_grau(a, b, c)
                self.console.print(f"[green]Resultado da equação do 2º grau: {resultado}[/green]")
                self.salvar_histórico("Equação do 2º grau", f"{a}x² + {b}x + {c}", resultado)

            elif escolha == "13":
                a1 = float(Prompt.ask("Digite o primeiro termo da PA"))
                r = float(Prompt.ask("Digite a razão da PA"))
                n = int(Prompt.ask("Digite o número de termos"))
                resultado = self.progressao_aritmetica(a1, r, n)
                self.console.print(f"[green]Progressão Aritmética: {resultado}[/green]")
                self.salvar_histórico("Progressão Aritmética", f"PA({a1}, {r}, {n})", resultado)

            elif escolha == "14":
                a1 = float(Prompt.ask("Digite o primeiro termo da PG"))
                r = float(Prompt.ask("Digite a razão da PG"))
                n = int(Prompt.ask("Digite o número de termos"))
                resultado = self.progressao_geometrica(a1, r, n)
                self.console.print(f"[green]Progressão Geométrica: {resultado}[/green]")
                self.salvar_histórico("Progressão Geométrica", f"PG({a1}, {r}, {n})", resultado)

            elif escolha == "15":
                self.mostrar_histórico()

            elif escolha == "16":
                self.console.print("[bold red]Saindo da calculadora...[/bold red]")
                break
            else:
                self.console.print("[bold red]Opção inválida! Tente novamente.[/bold red]")

# Criando a instância da calculadora e iniciando o menu
calculadora = CalculadoraAvancada()
calculadora.menu()
