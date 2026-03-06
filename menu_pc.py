print()
print("Olá, seja bem vindo à HB TI! De acordo com seu uso, selecione o número da opção que deseja:")
print("1-Uso Empresarial")
print("2-Uso comum do dia a dia")
print("3-Uso Gamer")
print("4-Servidor")
print()
escolha=int(input("Qual opção deseja?: "))

match escolha:
    case 1:
        print()
        print("Especificações adequadadas: I5 7ª geração - 8 GB RAM - SSD 256 GB")
        print()
    case 2:
        print()
        print("Especificações adequadadas: I5 5ª geração - 8 GB RAM - SSD 500 GB")
        print()
    case 3:
        print()
        print("Especificações adequadadas: I9 11ª geração - 16 GB RAM - SSD 500 GB - RTX 5090")
        print()
    case 4:
        print()
        print("Especificações adequadadas: XEON 6 - 32 GB RAM - SSD 256 GB + HD 1 TB")
        print()
    