from utils import imprimir_lento, cabecalho
from modulos import modulo_1, modulo_2, modulo_3, modulo_4
from quiz import quiz
import time
from datetime import datetime
from modulos import acessos_modulos

def verificar_senha():
    """
    Solicita uma senha do usuário antes de iniciar o programa.
    A senha correta é: "idoso123"
    """
    tentativas = 3
    while tentativas > 0:
        senha = input("Digite a senha para acessar o programa: ")
        if senha == "idoso123":
            print("Acesso permitido. Bem-vindo!")
            return True
        else:
            print("Senha incorreta. Tente novamente.")
            tentativas -= 1
    print("Número de tentativas excedido. Encerrando o programa.")
    return False

# Função principal que exibe o menu de opções para o usuário
def menu_principal():
    
    for k, v in acessos_modulos.items():
        print(f"{k}: {v} vez(es)")

    while True:
        cabecalho("PROGRAMA DE INCLUSÃO DIGITAL PARA IDOSOS")
        print("1 - Módulo 1: Primeiros passos com o computador")
        print("2 - Módulo 2: Navegação e segurança na internet")
        print("3 - Módulo 3: Instalando e usando o Python")
        print("4 - Módulo 4: Conceitos de programação")
        print("5 - Módulo 5: Quiz interativo")
        print("6 - Sair")
        escolha = input("\nEscolha uma opção: ").strip()

        if escolha == "1":
            modulo_1()
        elif escolha == "2":
            modulo_2()
        elif escolha == "3":
            modulo_3()
        elif escolha == "4":
            modulo_4()
        elif escolha == "5":
            quiz()
        elif escolha == "6":
            imprimir_lento("\nObrigado por participar! Até logo.")
            break
        else:
            imprimir_lento("Opção inválida. Tente novamente.")
            
# Início do programa - chama o menu principal
if __name__ == "__main__":
    if verificar_senha():
        menu_principal()
