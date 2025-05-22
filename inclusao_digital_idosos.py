import time

def imprimir_lento(texto, atraso=0.04):
    for c in texto:
        print(c, end='', flush=True)
        time.sleep(atraso)
    print()

def cabecalho(titulo):
    print("\n" + "="*60)
    imprimir_lento(f"{titulo}".center(60))
    print("="*60)

def modulo_1():
    cabecalho("MÓDULO 1 - PRIMEIROS PASSOS COM O COMPUTADOR")
    imprimir_lento("1. Para ligar o computador, pressione o botão 'Power'.")
    imprimir_lento("2. Use o mouse para mover o cursor e clique para interagir.")
    imprimir_lento("3. O teclado serve para digitar textos e comandos.")
    imprimir_lento("4. Clique duas vezes para abrir programas e no X para fechar.")
    imprimir_lento("5. Explore pastas com o botão direito e clique em 'Nova Pasta'.")
    input("\nPressione ENTER para voltar ao menu.")

def modulo_2():
    cabecalho("MÓDULO 2 - NAVEGAÇÃO E SEGURANÇA NA INTERNET")
    imprimir_lento("1. Navegadores como Chrome permitem acessar sites.")
    imprimir_lento("2. Para pesquisar, digite no Google e pressione ENTER.")
    imprimir_lento("3. Nunca clique em links suspeitos.")
    imprimir_lento("4. Sites seguros começam com 'https://' e têm um cadeado.")
    imprimir_lento("5. Nunca compartilhe sua senha com ninguém.")
    input("\nPressione ENTER para voltar ao menu.")

def modulo_3():
    cabecalho("MÓDULO 3 - INSTALANDO E USANDO O PYTHON")
    imprimir_lento("1. Acesse https://python.org e clique em 'Download'.")
    imprimir_lento("2. Instale com ajuda de um responsável ou orientador.")
    imprimir_lento("3. Abra o 'IDLE' (ambiente do Python).")
    imprimir_lento('4. Digite: print("Olá, mundo!") e pressione ENTER.')
    input("\nPressione ENTER para voltar ao menu.")

def modulo_4():
    cabecalho("MÓDULO 4 - CONCEITOS DE PROGRAMAÇÃO")
    imprimir_lento('1. Variável é um nome para guardar algo. Ex: nome = "Ana"')
    imprimir_lento('2. print() mostra algo na tela. Ex: print("Boa noite!")')
    imprimir_lento('3. Laços for/while repetem ações. Ex: for i in range(3):')
    imprimir_lento('4. Condições if/else tomam decisões. Ex: if idade >= 60:')
    input("\nPressione ENTER para voltar ao menu.")

def quiz():
    cabecalho("MÓDULO 5 - QUIZ INTERATIVO")
    perguntas = [
        ("O que usamos para mostrar algo na tela em Python?\nA) escrever\nB) print()\nC) mostrar()", "B"),
        ("Qual comando repete ações em Python?\nA) for/while\nB) repetir\nC) ciclo", "A"),
        ("Como chamamos um nome que guarda um valor?\nA) Texto\nB) Número\nC) Variável", "C"),
        ("O que significa https:// em um site?\nA) Site divertido\nB) Site seguro\nC) Site falso", "B"),
        ("O que você deve evitar na internet?\nA) Vídeos\nB) Links desconhecidos\nC) Sites confiáveis", "B"),
    ]

    pontuacao = 0
    for i, (pergunta, resposta) in enumerate(perguntas, 1):
        print(f"\nPergunta {i}:\n")
        imprimir_lento(pergunta)
        escolha = input("Sua resposta: ").strip().upper()
        if escolha == resposta:
            imprimir_lento("✅ Correto! Muito bem!")
            pontuacao += 1
        else:
            imprimir_lento(f"❌ Errado. A resposta correta era: {resposta}")
    imprimir_lento(f"\nVocê acertou {pontuacao} de {len(perguntas)} perguntas.")
    input("\nPressione ENTER para voltar ao menu.")

def menu_principal():
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

if __name__ == "__main__":
    menu_principal()
