from utils import imprimir_lento, cabecalho

# Dicionário para contar acessos
acessos_modulos = {"modulo_1": 0, "modulo_2": 0, "modulo_3": 0, "modulo_4": 0}


def modulo_1():
    acessos_modulos["modulo_1"]
    cabecalho("MÓDULO 1 - PRIMEIROS PASSOS COM O COMPUTADOR")

    
    imprimir_lento("1. Para ligar o computador, pressione o botão 'Power'.")
    imprimir_lento("2. Use o mouse para mover o cursor e clique para interagir.")
    imprimir_lento("3. O teclado serve para digitar textos e comandos.")
    imprimir_lento("4. Clique duas vezes para abrir programas e no X para fechar.")
    imprimir_lento("5. Explore pastas com o botão direito e clique em 'Nova Pasta'.")
    input("\nPressione ENTER para voltar ao menu.")


def modulo_2():
    acessos_modulos["modulo_2"]
    cabecalho("MÓDULO 2 - NAVEGAÇÃO E SEGURANÇA NA INTERNET")

    
    imprimir_lento("1. Navegadores como Chrome permitem acessar sites.")
    imprimir_lento("2. Para pesquisar, digite no Google e pressione ENTER.")
    imprimir_lento("3. Nunca clique em links suspeitos.")
    imprimir_lento("4. Sites seguros começam com 'https://' e têm um cadeado.")
    imprimir_lento("5. Nunca compartilhe sua senha com ninguém.")
    input("\nPressione ENTER para voltar ao menu.")


def modulo_3():
    acessos_modulos["modulo_3"]
    cabecalho("MÓDULO 3 - INSTALANDO E USANDO O PYTHON")

    
    imprimir_lento("1. Acesse https://python.org e clique em 'Download'.")
    imprimir_lento("2. Instale com ajuda de um responsável ou orientador.")
    imprimir_lento("3. Abra o 'IDLE' (ambiente do Python).")
    imprimir_lento('4. Digite: print("Olá, mundo!") e pressione ENTER.')
    input("\nPressione ENTER para voltar ao menu.")


def modulo_4():
    acessos_modulos["modulo_4"]
    cabecalho("MÓDULO 4 - CONCEITOS DE PROGRAMAÇÃO")

    
    imprimir_lento('1. Variável é um nome para guardar algo. Ex: nome = "Ana"')
    imprimir_lento('2. print() mostra algo na tela. Ex: print("Boa noite!")')
    imprimir_lento('3. Laços for/while repetem ações. Ex: for i in range(3):')
    imprimir_lento('4. Condições if/else tomam decisões. Ex: if idade >= 60:')
    input("\nPressione ENTER para voltar ao menu.")

