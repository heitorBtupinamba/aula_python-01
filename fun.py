def mostrar_menu():
    print("---------- MENU DE RESTAURANTE ----------")
    print("\n1 - Ver Cardápio")
    print("2 - Fazer Pedido")
    print("3 - Ver Conta")
    print("4 - Sair")
    print("-----------------------------------------")

while True: 
    mostrar_menu()
    opcao = input("Escolha uma opção: ")
    match opcao:
        case "1":
            print("======== Cardápio ========")
            print("Pizza - $35")
            print("Hamburguer - $20")
            print("Refrigerante - $10")
        case "2":
            print("\nO que Deseja Pedir? ")
            print("1 - Pizza: $35")
            print("2 - Hamburguer: $20")
            print("3 - Refrigerante: $10")
            pedido = input("Escolha: ")
            
            match pedido:
                case "1":
                    conta = 0
                    conta += 35
                    print("Pedido selecionado: Pizza")
                case 2:
                    conta = 0
                    conta =+ 20
                    print("Pedido escolhido: Hamburguer")
                case 3:
                    conta = 0
                    conta += 10
                    print("Pedido Escolhido: Refrigerante")
                case _:
                    print("Opcção Inválida.")

        case "3":
            print(f"\nO valor final da conta: R${conta}")
        case "4":
            print("Obrigado!")
            break
        case _:
            print("Opção Inválida, tente novamente.")
