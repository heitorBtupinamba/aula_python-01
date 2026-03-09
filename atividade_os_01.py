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

def infos_windows():
    executar_comando(f"systeminfo")

def mostrar_processos():
    executar_comando(f"tasklist")

def repara_arquivos_sistema():
    executar_comando(f"sfc /scannow")

def repara_arquivos_disco():
    executar_comando(f"chkdsk /f /r /x")

def exbir_usuario():
    executar_comando(f"whoami")

def desligar_reiniciar():
    executar_comando(f"shutdown /s")

def menu():
    while True: 
        print("\n------------- FERRAMENTA DE SUPORTE----------")
        print("1 - Mostrar IP")
        print("2 - Renovar IP")
        print("3 - Mostrar todas as informações de rede")
        print("4 - Ping")
        print("5 - Exibir informações de configurações do Windows")
        print("6 - Mostrar todos os processos em execução")
        print("7 - Verificar e reparar arquivos corrompidos do sistema")
        print("8 - Verificar e reparar erros no disco")
        print("9 - Exibir o usuário atual")
        print("10 - Desligar computador")
        print("11 - Sair")
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
            case "5": 
                infos_windows()
            case "6": 
                mostrar_processos()
            case "7": 
                repara_arquivos_sistema()
            case "8": 
                repara_arquivos_disco()
            case "9": 
                exbir_usuario()
            case "10":
                desligar_reiniciar()
            case "11": 
                print("Saindo...")
                break
            case _: ("Essa opção não Existe.")
if __name__ == "__main__":
    menu()

