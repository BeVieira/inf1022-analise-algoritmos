import os

def knapsack_10(B, weights, values):
  n = len(weights)

  # dp[i][b] = OPT(i, b): usando itens 1..i e capacidade b
  dp = [[0] * (B + 1) for _ in range(n + 1)]

  # choice[i][b] = número de unidades do item i escolhidas na solução ótima de (i, b)
  choice = [[0] * (B + 1) for _ in range(n + 1)]

  for i in range(1, n + 1):
    w_i = weights[i - 1]
    v_i = values[i - 1]
    for b in range(B + 1):
      best_value = 0
      best_k = 0
      for k in range(0, 11):
        total_weight = k * w_i
        if total_weight > b:
          break
        value_candidate = dp[i - 1][b - total_weight] + k * v_i
        if value_candidate > best_value:
          best_value = value_candidate
          best_k = k
      dp[i][b] = best_value
      choice[i][b] = best_k

  optimal_value = dp[n][B]

  quantities = [0] * n
  remaining_capacity = B

  for i in range(n, 0, -1):
    k = choice[i][remaining_capacity]
    quantities[i - 1] = k
    remaining_capacity -= k * weights[i - 1]

  return optimal_value, quantities


def solve_instance(file_path):
  with open(file_path, "r") as f:
    first_line = f.readline().split()
    n = int(first_line[0])
    B = int(first_line[1])

    values = []
    weights = []

    for _ in range(n):
      line = f.readline().split()
      if not line:
        break
      v_i = int(line[0])
      w_i = int(line[1])
      values.append(v_i)
      weights.append(w_i)

  optimal_value, quantities = knapsack_10(B, weights, values)
  return n, B, values, weights, optimal_value, quantities


def main():
  base_dir = "instancias"

  for i in range(1, 9):
    filename = f"inst{i}"
    file_path = os.path.join(base_dir, filename)

    if not os.path.isfile(file_path):
      print(f"[Atenção] Arquivo {file_path} não encontrado, pulando.\n")
      continue

    n, B, values, weights, optimal_value, quantities = solve_instance(file_path)

    print(f"=== Instância {filename} ===")
    print(f"n = {n}, B = {B}")
    print(f"Valor ótimo: {optimal_value}")

    print("Itens usados (item: quantidade, valor, peso):")
    for idx, q in enumerate(quantities, start=1):
      if q > 0:
        print(f"  Item {idx}: {q} unidades (v={values[idx-1]}, w={weights[idx-1]})")
    print()


if __name__ == "__main__":
  main()
