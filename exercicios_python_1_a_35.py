# Lista de Exercícios de Python -(1 a 35)

# Exercício 1
nome = input("Digite seu nome: ")
print(f"Bem-vindo, {nome}!")
print("-" * 40)

# Exercício 2
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")
print("Palavras concatenadas:", palavra1 + " " + palavra2)
print("-" * 40)

# Exercício 3
frase = input("Digite uma frase: ")
quantidade_palavras = len(frase.split())
print("A frase tem", quantidade_palavras, "palavras.")
print("-" * 40)

# Exercício 4
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print("A soma é:", num1 + num2)
print("-" * 40)

# Exercício 5
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
print("A média é:", (n1 + n2 + n3) / 3)
print("-" * 40)

# Exercício 6
nums = [float(input(f"Digite o {i+1}º número: ")) for i in range(3)]
print("Maior número:", max(nums))
print("Menor número:", min(nums))
print("-" * 40)

# Exercício 7
num = float(input("Digite um número: "))
if num > 100:
    print("Maior que 100")
elif num < 100:
    print("Menor que 100")
else:
    print("Igual a 100")
print("-" * 40)

# Exercício 8
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
if a == b:
    print("Os números são iguais.")
else:
    print("O maior número é:", max(a, b))
print("-" * 40)

# Exercício 9
l1 = float(input("Digite o primeiro lado: "))
l2 = float(input("Digite o segundo lado: "))
l3 = float(input("Digite o terceiro lado: "))
if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("Pode formar um triângulo")
else:
    print("Não pode formar um triângulo")
print("-" * 40)

# Exercício 10
num = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
print("-" * 40)

# Exercício 11
n = int(input("Digite um número: "))
print("Divisores de", n, ":")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
print("-" * 40)

# Exercício 12
n = int(input("Digite um número: "))
eh_primo = True
if n < 2:
    eh_primo = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            eh_primo = False
            break
print("É primo." if eh_primo else "Não é primo.")
print("-" * 40)

# Exercício 13
n = int(input("Digite um número: "))
for i in range(n, -1, -1):
    print(i)
print("-" * 40)

# Exercício 14
n = int(input("Digite um número: "))
soma = sum(range(1, n+1))
print("Soma dos números de 1 até", n, ":", soma)
print("-" * 40)

# Exercício 15
n = int(input("Digite um número: "))
fatorial = 1
for i in range(1, n+1):
    fatorial *= i
print("Fatorial de", n, "é:", fatorial)
print("-" * 40)

# Exercício 16
cores = ["vermelho", "azul", "verde", "amarelo", "roxo"]
print("A terceira cor é:", cores[2])
print("-" * 40)

# Exercício 17
numeros = []
for i in range(5):
    n = float(input(f"Digite o {i+1}º número: "))
    numeros.append(n)
numeros.sort()
print("Números em ordem crescente:", numeros)
print("-" * 40)

# Exercício 18
pessoas = {"Ana": 25, "Bruno": 30, "Clara": 22}
nome = input("Digite o nome para consultar a idade: ")
idade = pessoas.get(nome)
if idade:
    print(f"{nome} tem {idade} anos.")
else:
    print("Nome não encontrado.")
print("-" * 40)

# Exercício 19
matriz = [[1, 2], [3, 4]]
for linha in matriz:
    print(linha)
print("-" * 40)

# Exercício 20
matriz = []
print("Digite os elementos da matriz 3x3:")
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Elemento [{i+1},{j+1}]: "))
        linha.append(valor)
    matriz.append(linha)
for linha in matriz:
    print(linha)
print("-" * 40)

# Exercício 21
print("Digite os elementos da primeira matriz 2x2:")
m1 = [[int(input(f"M1[{i+1}][{j+1}]: ")) for j in range(2)] for i in range(2)]
print("Digite os elementos da segunda matriz 2x2:")
m2 = [[int(input(f"M2[{i+1}][{j+1}]: ")) for j in range(2)] for i in range(2)]
soma = [[m1[i][j] + m2[i][j] for j in range(2)] for i in range(2)]
print("Matriz resultante:")
for linha in soma:
    print(linha)
print("-" * 40)

# Exercício 22
def dobro(n):
    return n * 2
n = int(input("Digite um número: "))
print("O dobro é:", dobro(n))
print("-" * 40)

# Exercício 23
def par_ou_impar(n):
    return "Par" if n % 2 == 0 else "Ímpar"
n = int(input("Digite um número: "))
print("O número é:", par_ou_impar(n))
print("-" * 40)

# Exercício 24
def soma_impares(lista):
    return sum([n for n in lista if n % 2 != 0])
lista = [int(input(f"Número {i+1}: ")) for i in range(5)]
print("Soma dos ímpares:", soma_impares(lista))
print("-" * 40)

# Exercício 25
import math
n = float(input("Digite um número: "))
print("Raiz quadrada:", math.sqrt(n))
print("-" * 40)

# Exercício 26
import datetime
entrada = input("Digite a data (dd/mm/aaaa): ")
dia, mes, ano = map(int, entrada.split('/'))
data = datetime.date(ano, mes, dia)
print("Dia da semana:", data.strftime("%A"))
print("-" * 40)

# Exercício 27
import random
n = int(input("Digite um número: "))
print("Número aleatório entre 1 e", n, ":", random.randint(1, n))
print("-" * 40)

# Exercício 28
aleatorios = [random.randint(1, 100) for _ in range(5)]
print("Números aleatórios:", aleatorios)
print("-" * 40)

# Exercício 29
import time
print("Lançando dado...")
time.sleep(2)
print("Resultado:", random.randint(1, 6))
print("-" * 40)

# Exercício 30
with open("texto.txt", "w") as arquivo:
    arquivo.write("Python é incrível!")
print("Arquivo 'texto.txt' criado.")
print("-" * 40)

# Exercício 31
with open("texto.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:", conteudo)
print("-" * 40)

# Exercício 32
nome = input("Digite o nome: ")
telefone = input("Digite o telefone: ")
with open("contatos.txt", "a") as arquivo:
    arquivo.write(f"{nome} - {telefone}\n")
print("Contato salvo!")
print("-" * 40)

# Exercício 33
numero = float(input("Digite um número para dividir 100: "))
if numero != 0:
    resultado = 100 / numero
    print("Resultado da divisão:", resultado)
else:
    print("Não é possível dividir por zero!")


# Exercício 34
numero = input("Digite um número: ")
if numero.isdigit():
    numero = int(numero)
    print("Você digitou o número:", numero)
else:
    print("Isso não é um número válido!")

# Exercício 35
numero = input("Digite um número inteiro: ")
if numero.isdigit():
    numero = int(numero)
    print("O quadrado de", numero, "é", numero ** 2)
else:
    print("Entrada inválida. Por favor, digite um número inteiro.")
