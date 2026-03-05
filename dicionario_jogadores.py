jogadores = {
    "Pedro" : 30,

    "Kaiki" : 40,

    "Rafael" : 35,

    "Jorge" : 50,

    "Felipe" : 45
}

print()
print("TABELA INICIAL")
for nome, pontos in jogadores.items():
    print(f"{nome} : {pontos}")

print()
nome_jogador = str(input("Digite o nome do jogador desejado: "))
print()

if nome_jogador in jogadores:
    pontuacao_adicionada = int(input("Digite a pontuação que deseja adicionar ao jogador: "))
    jogadores[nome_jogador] = jogadores[nome_jogador] + pontuacao_adicionada
    print("TABELA ATUALIZADA")
    for nome, pontos in jogadores.items():
        print(f"{nome} : {pontos}")

else:
    print("Este nome não existe na tabela de jogadores!")
    print()

print()
    


