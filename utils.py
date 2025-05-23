import time

# Função que imprime texto lentamente, simulando digitação
def imprimir_lento(texto, atraso=0.04):
    for c in texto:
        print(c, end='', flush=True)
        time.sleep(atraso)
    print()

# Função que imprime um cabeçalho formatado
def cabecalho(titulo):
    print("\n" + "="*60)
    imprimir_lento(f"{titulo}".center(60))
    print("="*60)
