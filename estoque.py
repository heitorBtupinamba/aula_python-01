estoque = {
    "Camisa": 50,
    "Calça": 15,
    "Boné": 25,
    "Tênis Nike": 35
}

print("ESTOQUE ATUAL:")
for produto, quantidade in estoque.items():
    print(f"{produto} : {quantidade}")


nome_produto = input("\nInforme o nome do produto vendido: ")
quantidade_vendida = int(input("Informe a quantidade vendida: "))

if nome_produto in estoque:
    if quantidade_vendida <= estoque[nome_produto]:
        estoque[nome_produto] = estoque[nome_produto]
        estoque[nome_produto] = estoque[nome_produto] - quantidade_vendida
        print("Venda realizada com sucesso!")
else:
    print("Produto não encontrado")

for produto, quantidade in estoque.items():
    print(f"{produto} | {quantidade}")