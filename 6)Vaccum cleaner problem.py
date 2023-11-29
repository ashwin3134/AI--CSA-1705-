class VacuumCleaner:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0] * cols for _ in range(rows)]
        self.current_position = (0, 0)

    def set_dirty_cells(self, dirty_cells):
        for cell in dirty_cells:
            row, col = cell
            if 0 <= row < self.rows and 0 <= col < self.cols:
                self.grid[row][col] = 1

    def print_grid(self):
        for row in self.grid:
            print(row)

    def clean(self):
        while any(1 in row for row in self.grid):
            self.print_grid()
            print(f"Current position: {self.current_position}")

            if self.grid[self.current_position[0]][self.current_position[1]] == 1:
                print("Cleaning...")
                self.grid[self.current_position[0]][self.current_position[1]] = 0
            else:
                print("No dirt to clean.")

            self.move()

    def move(self):
        if self.current_position[0] % 2 == 0:
            self.current_position = (self.current_position[0], min(self.current_position[1] + 1, self.cols - 1))
        else:
            self.current_position = (self.current_position[0], max(self.current_position[1] - 1, 0))


        if self.current_position[0] < self.rows - 1:
            self.current_position = (self.current_position[0] + 1, self.current_position[1])
        else:

            self.current_position = (self.current_position[0] + 2, self.current_position[1])

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

vacuum = VacuumCleaner(rows, cols)

dirty_cells = []
while True:
    cell_input = input("Enter the coordinates of a dirty cell (row col), or type 'done' to finish: ")
    if cell_input.lower() == 'done':
        break
    else:
        dirty_cells.append(tuple(map(int, cell_input.split())))

vacuum.set_dirty_cells(dirty_cells)
vacuum.clean()
