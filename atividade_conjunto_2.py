Heitor = {"Leite","Nescau","Bolacha","Batata","Leite"}
Caio = {"Arroz","Feijão","Batata"}
Thiago = {"Asa de Frango","Pão-de-alho","Sprite"}
Ana = {"Macarrão","Azeite","Feijão"}

comum = Heitor.intersection(Heitor|Caio|Thiago|Ana)
print(f"Estes são os itens em comum nas listas:{comum}")

totais = Heitor.union(Caio|Thiago|Ana)
print(f"Estes são todos os itens da lista: {totais}")
print(f"Este é a quantidade total de itens: {len(totais)}")

nao_repete = set(Heitor)
print(Heitor)
