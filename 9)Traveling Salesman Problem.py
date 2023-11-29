from itertools import permutations

def calculate_total_distance(order, graph):
    total_distance = 0
    for i in range(len(order) - 1):
        total_distance += graph[order[i]][order[i + 1]]
    total_distance += graph[order[-1]][order[0]]  
    return total_distance

def traveling_salesman_bruteforce(graph):
    nodes = list(graph.keys())
    best_order = None
    best_distance = float('inf')

    for perm in permutations(nodes):
        current_distance = calculate_total_distance(perm, graph)
        if current_distance < best_distance:
            best_distance = current_distance
            best_order = perm

    return best_order, best_distance

graph = {
    'A': {'B': 2, 'C': 3, 'D': 1},
    'B': {'A': 2, 'C': 2, 'D': 4},
    'C': {'A': 3, 'B': 2, 'D': 5},
    'D': {'A': 1, 'B': 4, 'C': 5}
}

best_order, best_distance = traveling_salesman_bruteforce(graph)
print("Best Order->", best_order)
print("Best Distance:", best_distance)
