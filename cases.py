print()
escolha = int(input("Digite um número de 1 a 7 para escolher um dia da semana: "))
print()

match escolha:
    case 1:
        print("O dia selecionado foi Segunda-feiera")
    case 2:
        print("O dia selecionado foi Terça-feiera")
    case 3:
        print("O dia selecionado foi Quarta-feiera")
    case 4:
        print("O dia selecionado foi Quinta-feiera")
    case 5:
        print("O dia selecionado foi Sexta-feiera")
    case 6:
        print("O dia selecionado foi Sábado")
    case 7:
        print("O dia selecionado foi Domingo")
    case _:
        print("Número inválido.")
    