from queue import Queue

class Puzzle:
    def __init__(self, state):
        self.state = state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    def __eq__(self, other):
        return self.state == other.state
    def __hash__(self):
        return hash(tuple(map(tuple, self.state)))
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.state])
    def find_blank(self):
        for i, row in enumerate(self.state):
            for j, val in enumerate(row):
                if val == 0:
                    return i, j

    def is_goal(self):
        return self.state == self.goal_state
    def get_neighbors(self):
        i, j = self.find_blank()
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbors = []

        for move in moves:
            ni, nj = i + move[0], j + move[1]
            if 0 <= ni < 3 and 0 <= nj < 3:
                new_state = [row[:] for row in self.state]
                new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]
                neighbors.append(Puzzle(new_state))

        return neighbors

def solve_puzzle(initial_state):
    initial_puzzle = Puzzle(initial_state)

    if initial_puzzle.is_goal():
        return [initial_state]

    visited = set()
    queue = Queue()
    queue.put([initial_puzzle])

    while not queue.empty():
        path = queue.get()
        current_puzzle = path[-1]

        if current_puzzle.is_goal():
            return [p.state for p in path]

        visited.add(current_puzzle)

        neighbors = current_puzzle.get_neighbors()
        for neighbor in neighbors:
            if neighbor not in visited:
                new_path = path + [neighbor]
                queue.put(new_path)

    return None

if __name__ == "__main__":

    initial_state = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]

    solution_path = solve_puzzle(initial_state)

    if solution_path:
        for step, state in enumerate(solution_path):
            print(f"Step {step + 1}:\n{Puzzle(state)}\n")
    else:
        print("No solution found.")
