from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich import box
import math

class CalculadoraAvancada:
    def __init__(self):
        self.console = Console()

    def exibir_menu(self):
        # Criando a tabela para o menu com 3 colunas
        table = Table(title="Calculadora Avançada", box=box.ROUNDED)
        
        # Adicionando as colunas para as opções
        table.add_column("Opções Básicas", justify="center", style="bold cyan")
        table.add_column("Opções Básicas", justify="center", style="white")

        table.add_column("Opções Avançadas", justify="center", style="bold magenta")
        table.add_column("Opções Avançadas", justify="center", style="white")

        table.add_column("Opções Geométricas", justify="center", style="bold yellow")
        table.add_column("Opções Geométricas", justify="center", style="white")

        
        # Adicionando as operações organizadas verticalmente em 3 seções
        operacoes = [
            # Seção 1: Operações Básicas
            ("1", "Somar", "7", "Fatorial", "13", "Área do círculo"),
            ("2", "Subtrair", "8", "Somar vetores", "14", "Área do triângulo"),
            ("3", "Multiplicar", "9", "Subtrair vetores", "15", "Área do retângulo"),
            ("4", "Dividir", "10", "Multiplicar vetor por escalar", "16", "Perímetro do círculo"),
            ("5", "Exponenciar", "11", "Produto escalar de vetores", ""),
            ("6", "Raiz quadrada", "12", "Equação 2º grau", ""),
            
            # Linha para "Sair"
            ("", "", "", "", "17", "Sair")
        ]

        for row in operacoes:
            table.add_row(*row)

        # Exibindo a tabela
        self.console.print(table)

    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        return a / b if b != 0 else "Erro: Divisão por zero"

    def exponenciar(self, a, b):
        return a ** b

    def raiz_quadrada(self, a):
        return math.sqrt(a)

    def fatorial(self, a):
        return math.factorial(a)

    def somar_vetores(self, a, b):
        return [x + y for x, y in zip(a, b)]

    def subtrair_vetores(self, a, b):
        return [x - y for x, y in zip(a, b)]

    def multiplicar_vetor_escalar(self, vetor, escalar):
        return [x * escalar for x in vetor]

    def produto_escalar(self, a, b):
        return sum(x * y for x, y in zip(a, b))

    def resolver_equacao_2_grau(self, a, b, c):
        discriminante = b**2 - 4*a*c
        if discriminante < 0:
            return "Não há raízes reais"
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return (raiz1, raiz2)

    def area_circulo(self, raio):
        return math.pi * raio**2

    def area_triangulo(self, base, altura):
        return 0.5 * base * altura

    def area_retangulo(self, largura, altura):
        return largura * altura

    def perimetro_circulo(self, raio):
        return 2 * math.pi * raio

    def menu(self):
        while True:
            self.exibir_menu()
            escolha = Prompt.ask("Escolha uma operação (1-17):", show_choices=False)

            if escolha == "1":
                self.somar_e_exibir_resultado()
            elif escolha == "2":
                self.subtrair_e_exibir_resultado()
            elif escolha == "3":
                self.multiplicar_e_exibir_resultado()
            elif escolha == "4":
                self.dividir_e_exibir_resultado()
            elif escolha == "5":
                self.exponenciar_e_exibir_resultado()
            elif escolha == "6":
                self.raiz_quadrada_e_exibir_resultado()
            elif escolha == "7":
                self.fatorial_e_exibir_resultado()
            elif escolha == "8":
                self.somar_vetores_e_exibir_resultado()
            elif escolha == "9":
                self.subtrair_vetores_e_exibir_resultado()
            elif escolha == "10":
                self.multiplicar_vetor_escalar_e_exibir_resultado()
            elif escolha == "11":
                self.produto_escalar_e_exibir_resultado()
            elif escolha == "12":
                self.resolver_equacao_2_grau_e_exibir_resultado()
            elif escolha == "13":
                self.area_circulo_e_exibir_resultado()
            elif escolha == "14":
                self.area_triangulo_e_exibir_resultado()
            elif escolha == "15":
                self.area_retangulo_e_exibir_resultado()
            elif escolha == "16":
                self.perimetro_circulo_e_exibir_resultado()
            elif escolha == "17":
                self.console.print("[bold red]Saindo da calculadora...[/bold red]")
                break
            else:
                self.console.print("[bold red]Opção inválida! Tente novamente.[/bold red]")

    def somar_e_exibir_resultado(self):
        a = float(Prompt.ask("Digite o primeiro número:"))
        b = float(Prompt.ask("Digite o segundo número:"))
        resultado = self.somar(a, b)
        self.console.print(f"Resultado: {resultado}")

    def subtrair_e_exibir_resultado(self):
        a = float(Prompt.ask("Digite o primeiro número:"))
        b = float(Prompt.ask("Digite o segundo número:"))
        resultado = self.subtrair(a, b)
        self.console.print(f"Resultado: {resultado}")

    def multiplicar_e_exibir_resultado(self):
        a = float(Prompt.ask("Digite o primeiro número:"))
        b = float(Prompt.ask("Digite o segundo número:"))
        resultado = self.multiplicar(a, b)
        self.console.print(f"Resultado: {resultado}")

    def dividir_e_exibir_resultado(self):
        a = float(Prompt.ask("Digite o numerador:"))
        b = float(Prompt.ask("Digite o denominador:"))
        resultado = self.dividir(a, b)
        self.console.print(f"Resultado: {resultado}")

    def exponenciar_e_exibir_resultado(self):
        a = float(Prompt.ask("Digite a base:"))
        b = float(Prompt.ask("Digite o expoente:"))
        resultado = self.exponenciar(a, b)
        self.console.print(f"Resultado: {resultado}")

    def raiz_quadrada_e_exibir_resultado(self):
        a = float(Prompt.ask("Digite o número:"))
        resultado = self.raiz_quadrada(a)
        self.console.print(f"Resultado: {resultado}")

    def fatorial_e_exibir_resultado(self):
        a = int(Prompt.ask("Digite o número para calcular o fatorial:"))
        resultado = self.fatorial(a)
        self.console.print(f"Resultado: {resultado}")

    def somar_vetores_e_exibir_resultado(self):
        a = list(map(int, Prompt.ask("Digite os elementos do primeiro vetor separados por espaço:").split()))
        b = list(map(int, Prompt.ask("Digite os elementos do segundo vetor separados por espaço:").split()))
        resultado = self.somar_vetores(a, b)
        self.console.print(f"Resultado: {resultado}")

    def subtrair_vetores_e_exibir_resultado(self):
        a = list(map(int, Prompt.ask("Digite os elementos do primeiro vetor separados por espaço:").split()))
        b = list(map(int, Prompt.ask("Digite os elementos do segundo vetor separados por espaço:").split()))
        resultado = self.subtrair_vetores(a, b)
        self.console.print(f"Resultado: {resultado}")

    def multiplicar_vetor_escalar_e_exibir_resultado(self):
        a = list(map(int, Prompt.ask("Digite os elementos do vetor separados por espaço:").split()))
        escalar = float(Prompt.ask("Digite o valor do escalar:"))
        resultado = self.multiplicar_vetor_escalar(a, escalar)
        self.console.print(f"Resultado: {resultado}")

    def produto_escalar_e_exibir_resultado(self):
        a = list(map(int, Prompt.ask("Digite os elementos do primeiro vetor separados por espaço:").split()))
        b = list(map(int, Prompt.ask("Digite os elementos do segundo vetor separados por espaço:").split()))
        resultado = self.produto_escalar(a, b)
        self.console.print(f"Resultado: {resultado}")

    def resolver_equacao_2_grau_e_exibir_resultado(self):
        a = float(Prompt.ask("Digite o coeficiente a:"))
        b = float(Prompt.ask("Digite o coeficiente b:"))
        c = float(Prompt.ask("Digite o coeficiente c:"))
        resultado = self.resolver_equacao_2_grau(a, b, c)
        self.console.print(f"Resultado: {resultado}")

    def area_circulo_e_exibir_resultado(self):
        raio = float(Prompt.ask("Digite o raio do círculo:"))
        resultado = self.area_circulo(raio)
        self.console.print(f"Resultado: {resultado}")

    def area_triangulo_e_exibir_resultado(self):
        base = float(Prompt.ask("Digite a base do triângulo:"))
        altura = float(Prompt.ask("Digite a altura do triângulo:"))
        resultado = self.area_triangulo(base, altura)
        self.console.print(f"Resultado: {resultado}")

    def area_retangulo_e_exibir_resultado(self):
        largura = float(Prompt.ask("Digite a largura do retângulo:"))
        altura = float(Prompt.ask("Digite a altura do retângulo:"))
        resultado = self.area_retangulo(largura, altura)
        self.console.print(f"Resultado: {resultado}")

    def perimetro_circulo_e_exibir_resultado(self):
        raio = float(Prompt.ask("Digite o raio do círculo:"))
        resultado = self.perimetro_circulo(raio)
        self.console.print(f"Resultado: {resultado}")

# Criando a instância da calculadora e iniciando o menu
calculadora = CalculadoraAvancada()
calculadora.menu()
