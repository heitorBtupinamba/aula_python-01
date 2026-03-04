A = 10
B = 11

if A > B:
    print("A é maior")
else:
    print("B é maior")


idade = 17

if idade >= 18:
    print("Você é de maior e pode ser preso!")
else:
    print("Você é de menor, deu sorte seu trombadinha!")

print()


aluno = {}

aluno["Nome"] = input("Digite o nome do aluno: ")
aluno["Curso"] = input("Digite o curso do aluno: ")
aluno["Nota"] = float(input("Digite a nota do aluno: "))

print(f"O nome do aluno é: {aluno['Nome']}")
print(f"O curso do aluno é: {aluno['Curso']}")
print("Aprovado!" if aluno["Nota"] >= 18 else "Reprovado")

