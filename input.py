nome = input("Digite seu nome: ")

print(f"Bem vindo {nome}!")
print()

nota1 = float(input("Digite sua 1° nota: "))
nota2 = float(input("Digite sua 2° nota: "))

print(f"Sua nota final foi: {nota1 + nota2}")
print()

aluno = {}

aluno["Nome"] = input("Digite o nome do aluno: ")
aluno["Sobrenome"] = input("Digite o sobrenome do aluno: ")
aluno["Idade"] = input("Digite a idade do aluno: ")
aluno["Curso"] = input("Digite o curso do aluno: ")

print("---------------------")
print("FICHA DO ALUNO")
print(f"Nome: {aluno["Nome"]}")
print(f"Sobrenome: {aluno["Sobrenome"]}")
print(f"Idade: {aluno["Idade"]}")
print(f"Curso: {aluno["Curso"]}")
print("---------------------")