#Printando vários nomes
a,b,c,d,e,f,g,h,i,j = "Heitor", "Rafael", "João", "Paulo", "Marco", "Túlio", "Luiz", "Kleber", "Matheus", "Antônio"
print(a,b,c,d,e,f,g,h,i,j)
print()

#Printando vários nomes de poições ímpares de uma lista
lista_nomes = ["Heitor", "Rafael", "João", "Paulo", "Marco", "Túlio", "Luiz", "Kleber", "Matheus", "Antônio"]
print("\n".join([lista_nomes[1],lista_nomes[3],lista_nomes[5],lista_nomes[7],lista_nomes[9]]))
print()

#Verificando se um elemento está entro da lista
lista_supermercado = ["Arroz","Feijão","Sal","Óleo","Vinagre","Peito de Frango","Pão","Queijo","Iogurte","Maçã"]
if "Sal" in lista_supermercado:
    print("Sim, este item está disponível")
else:
    print("Não, este item não está disponível")

print()


lista_nomes2 = ["Heitor", "Rafael", "João", "Paulo", "Marco", "Túlio", "Luiz", "Kleber", "Matheus", "Antônio"]
lista_nomes2[0:5] = "Jão", "Cleitu", "Robsu", "Inhegas", "Dilera", "Diguinho"
print(lista_nomes2)
print()

lista_nomes3 = ["Heitor", "Rafael", "João", "Paulo", "Marco", "Túlio", "Luiz", "Kleber", "Matheus", "Antônio"]
lista_nomes3.insert(1,"Bruce")
lista_nomes3.insert(2,"Barry")
lista_nomes3.insert(3,"Peter")
print(lista_nomes3)
print()

