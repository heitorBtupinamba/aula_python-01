import subprocess
import os

def executar_comando(comando):
    try: 
        resultado = subprocess.run(comando, shell=True)
    except Exception as e: 
        print("Erro ao exexutar comando: ", e)

def mostrar_ip():
    executar_comando("ipconfig")

def renovar_ip():
    executar_comando("ipconfig /renew")

def mostrar_ip_completo():
    executar_comando("ipconfig /all")

def ping_host():
    host = input("Digite o IP ou HOSTNAME: ")
    executar_comando(f"ping {host}")

def menu():
    while True: 
        print("\n------------- FERRAMENTA DE REDE -------------")
        print("1 - Mostrar IP")
        print("2 - Renovar IP")
        print("3 - Mostrar IP Completo")
        print("4 - Ping")
        print("0 - Sair")
        print("------------- Heitor ------------------------")
        opcao = str(input("Escolha uma opçao: "))

        match(opcao):
            case "1": 
                mostrar_ip()
            case "2": 
                renovar_ip()
            case "3": 
                mostrar_ip_completo()
            case "4": 
                ping_host()
            case "0": 
                print("Saindo...")
                break
            case _: ("Essa opção não Existe.")
if __name__ == "__main__":
    menu()

