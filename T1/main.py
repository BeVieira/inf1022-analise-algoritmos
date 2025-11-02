import random
import time
from kselection import linearSelection
from sortselection import sortSelection


def tarefa1(A, k):
  return linearSelection(A, k)

def tarefa2():
  nList = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

  for n in nList:
    k = n // 2
    linearTime = []
    sortTime = []
    isEqual = True

    for i in range(10):
      A = [random.randint(1, 100000) for _ in range(n)]

      inicio = time.time()
      resultado_linear = linearSelection(A.copy(), k)
      fim = time.time()
      linearTime.append(fim - inicio)

      inicio = time.time()
      resultado_sort = sortSelection(A.copy(), k)
      fim = time.time()
      sortTime.append(fim - inicio)

      if resultado_linear != resultado_sort:
        isEqual = False

    media_linear = sum(linearTime) / len(linearTime)
    media_sort = sum(sortTime) / len(sortTime)

    print(f"\nTamanho n = {n}")
    print(f"  k = {k}")
    print(f"  Tempo médio LinearSelection: {media_linear:.6f} s")
    print(f"  Tempo médio SortSelection:   {media_sort:.6f} s")
    print(f"  Resultados iguais em todas as instâncias? {'Sim' if isEqual else 'Não'}")

def main():
  while True:
    print("\n=== MENU DE SELEÇÃO ===")
    print("1 - Tarefa 1: Linear Selection")
    print("2 - Tarefa 2: Experimentos")
    print("0 - Sair")

    try:
      escolha = int(input("\nEscolha uma opção: "))
    except ValueError:
      print("Entrada inválida! Digite um número.")
      continue

    if escolha == 0:
      print("Encerrando o programa...")
      break

    elif escolha in (1, 2):
      if escolha == 1:
          try:
              A = list(map(int, input("\nDigite os números da lista A, separados por espaço: ").split()))
              k = int(input("Digite o valor de k: "))
              print(f"\nResultado (Seleção Linear): {tarefa1(A, k)}")
          except ValueError:
            print("Erro: digite apenas números inteiros!")
          except Exception as e:
            print(f"Ocorreu um erro: {e}")
      else:
          print(f"\nResultado (Experimentos): {tarefa2()}")
    else:
      print("Opção inválida! Escolha 1, 2 ou 0.")

if __name__ == '__main__':
    main()
