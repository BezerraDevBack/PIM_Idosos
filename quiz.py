from utils import imprimir_lento, cabecalho
from statistics import mean, median, mode
resultados_quiz = []


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
    
    resultados_quiz.append(pontuacao)  # <<-- Mover para dentro da função!
    
    input("\nPressione ENTER para voltar ao menu.")

# A parte abaixo fica fora da função, para mostrar as estatísticas após várias execuções do quiz

if len(resultados_quiz) > 1:
    print("\nEstatísticas do Quiz:")
    print(f"Média: {mean(resultados_quiz):.2f}")
    print(f"Mediana: {median(resultados_quiz)}")
    try:
        print(f"Moda: {mode(resultados_quiz)}")
    except:
        print("Moda: múltiplos valores")


