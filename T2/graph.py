from typing import List, Tuple, Dict
from collections import deque
from itertools import permutations

Cfg = Tuple[int, ...]

def show_board(cfg: Cfg) -> None:
  for i in range(0, 9, 3):
    line = cfg[i:i+3]
    print(" ".join(str(x) if x != 0 else "_" for x in line))
  print()

def precompute_moves() -> List[List[int]]:
  moves: List[List[int]] = [[] for _ in range(9)]

  for pos in range(9):
    row = pos // 3
    col = pos % 3
    neighbors = []

    if row > 0:
      neighbors.append(pos - 3)  # cima
    if row < 2:
      neighbors.append(pos + 3)  # baixo
    if col > 0:
      neighbors.append(pos - 1)  # esquerda
    if col < 2:
      neighbors.append(pos + 1)  # direita

    moves[pos] = neighbors

  return moves

def generate_neighbors(cfg: Cfg, moves: List[List[int]]) -> List[Cfg]:
  idx_zero = cfg.index(0)
  neighbors_cfgs = []

  for swap in moves[idx_zero]:
    new_cfg = list(cfg)
    new_cfg[idx_zero], new_cfg[swap] = new_cfg[swap], new_cfg[idx_zero]
    neighbors_cfgs.append(tuple(new_cfg))

  return neighbors_cfgs


def build_state_graph() -> Tuple[List[Cfg], Dict[int, List[int]], Dict[Cfg, int]]:
  moves = precompute_moves()
  all_cfgs = list(permutations(range(9)))
  hash_cfg: Dict[Cfg, int] = {cfg: i for i, cfg in enumerate(all_cfgs)}
  graph: Dict[int, List[int]] = {i: [] for i in range(len(all_cfgs))}

  for i, cfg in enumerate(all_cfgs):
    for neigh in generate_neighbors(cfg, moves):
      j = hash_cfg[neigh]
      graph[i].append(j)
  
  return all_cfgs, graph, hash_cfg

def bfs(graph: Dict[int, List[int]], start: int) -> Dict[int, int]:
  visited = set([start])
  distance = {start: 0}
  queue = deque([start])

  while queue:
    current = queue.popleft()
    for neigh in graph[current]:
      if neigh not in visited:
        visited.add(neigh)
        distance[neigh] = distance[current] + 1
        queue.append(neigh)

  return distance

def count_connected_components(graph: Dict[int, List[int]]) -> int:
  visited = set()
  components = 0

  for node in graph:
    if node not in visited:
      components += 1
      distance = bfs(graph, node)
      visited.update(distance.keys())

  return components

def hardest_configuration(graph: Dict[int, List[int]], cfgs: List[Cfg], hash_cfg: Dict[Cfg, int], goal_cfg: Cfg):
  start = hash_cfg[goal_cfg]
  distance = bfs(graph, start)

  farthest_node = max(distance, key=distance.get)
  max_dist = distance[farthest_node]

  return cfgs[farthest_node], max_dist

if __name__ == "__main__":
  configs, graph, hash_cfg = build_state_graph()

  num_nodes = len(configs)
  num_edges = sum(len(vs) for vs in graph.values()) // 2

  print("================================ Tarefa 1 ================================")
  print(f"Nós totais no grafo: {num_nodes}")
  print(f"Arestas totais no grafo: {num_edges}\n")

  u = 0
  v = graph[u][0]
  print("Exemplo de dois nós conectados (u, v):")
  print(f"Nó {u}:")
  show_board(configs[u])
  print(f"Nó {v}:")
  show_board(configs[v])

  u2, v2 = 0, 10 if num_nodes > 10 else 1
  while v2 in graph[u2]:
    v2 += 1
    if v2 >= num_nodes:
      v2 = 1

  print("Exemplo de dois nós NÃO conectados por uma aresta (u2, v2):")
  print(f"Node {u2}:")
  show_board(configs[u2])
  print(f"Node {v2}:")
  show_board(configs[v2])

  components = count_connected_components(graph)
  print("================================ Tarefa 2 ================================")
  print(f"Número de componentes conexos: {components}")
  
  goal_cfg = (1, 2, 3, 4, 5, 6, 7, 8, 0)
  hardest_cfg, moves_needed = hardest_configuration(graph, configs, hash_cfg, goal_cfg)

  print("================================ Tarefa 3 ================================")
  print("1. Configuração mais difícil (mais movimentos para alcançar o objetivo):")
  show_board(hardest_cfg)
  print(f"2. Número de movimentos necessários para alcançar o objetivo: {moves_needed}")