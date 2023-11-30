from collections import defaultdict
def is_consistent(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def select_unassigned_variable(assignment, graph):
    unassigned_variables = [node for node in graph if node not in assignment]
    return min(unassigned_variables, key=lambda node: len(graph[node]))

def backtracking_search(graph, colors):
    return backtrack({}, graph, colors)

def backtrack(assignment, graph, colors):
    if len(assignment) == len(graph):
        return assignment 

    node = select_unassigned_variable(assignment, graph)

    for color in colors:
        if is_consistent(node, color, assignment, graph):
            assignment[node] = color
            result = backtrack(assignment, graph, colors)
            if result is not None:
                return result
            del assignment[node]

    return None 

def get_user_input():
    graph = defaultdict(list)
    
    while True:
        node = input("Enter a region name (or 'done' to finish): ")
        if node.lower() == 'done':
            break
        neighbors = input(f"Enter neighboring regions for {node} (comma-separated): ").split(',')
        graph[node] = [neighbor.strip() for neighbor in neighbors]

    colors = input("Enter available colors (comma-separated): ").split(',')
    colors = [color.strip() for color in colors]

    return graph, colors

user_map, user_colors = get_user_input()

coloring = backtracking_search(user_map, user_colors)

if coloring:
    print("\nMap Coloring Result:")
    for node, color in coloring.items():
        print(f"{node}: {color}")
else:
    print("No valid coloring found.")

