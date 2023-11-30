from itertools import permutations

def calculate_distance(tour, distances):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distances[tour[i]][tour[i + 1]]
    total_distance += distances[tour[-1]][tour[0]]
    return total_distance

def traveling_salesman_bruteforce(distances):
    num_cities = len(distances)
    cities = list(range(num_cities))
    min_distance = float('inf')
    best_tour = None

    for tour in permutations(cities):
        current_distance = calculate_distance(tour, distances)
        if current_distance < min_distance:
            min_distance = current_distance
            best_tour = tour

    return best_tour, min_distance

distances = [
    [0, 1, 2, 3],
    [1, 0, 6, 4],
    [2, 6, 0, 5],
    [3, 4, 5, 0]
]

best_tour, min_distance = traveling_salesman_bruteforce(distances)

print("Best Tour:", best_tour)
print("Minimum Distance:", min_distance)
