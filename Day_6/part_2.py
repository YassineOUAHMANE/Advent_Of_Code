# Read the input file content
with open("Day_6/input_day_6.txt", "r") as file:
    map_input = file.readlines()

# Clean up the map input
map_input = [line.strip() for line in map_input]

# Parse the map input into a grid
def parse_map(map_lines):
    grid = [list(line) for line in map_lines]
    directions = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
    return grid, directions

# Simulate guard movement
def simulate(grid, start_pos, start_dir, obstruction=None):
    rows, cols = len(grid), len(grid[0])
    x, y = start_pos
    dx, dy = start_dir
    visited_states = set()
    path = set()

    while 0 <= x < rows and 0 <= y < cols:
        # Detect infinite loop
        state = (x, y, dx, dy)
        if state in visited_states:
            return True, path  # Loop detected
        visited_states.add(state)
        path.add((x, y))

        # Check next position
        nx, ny = x + dx, y + dy
        if obstruction and (nx, ny) == obstruction:
            break  # Obstruction blocks movement
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '.':
            x, y = nx, ny
        else:
            # Turn right
            dx, dy = dy, -dx

    return False, path  # No loop detected

# Find obstruction positions that cause a loop
def find_obstruction_positions(grid, start_pos, start_dir):
    rows, cols = len(grid), len(grid[0])
    _, path = simulate(grid, start_pos, start_dir)
    obstruction_positions = set()

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == '.' and (x, y) not in path and (x, y) != start_pos:
                grid[x][y] = '#'  # Temporarily place obstruction
                is_loop, _ = simulate(grid, start_pos, start_dir, obstruction=(x, y))
                grid[x][y] = '.'  # Remove obstruction
                if is_loop:
                    obstruction_positions.add((x, y))
    return obstruction_positions

# Parse the input map and identify the guard's starting position and direction
grid, directions = parse_map(map_input)

for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell in directions:
            start_pos = (i, j)
            start_dir = directions[cell]
            grid[i][j] = '.'

# Determine valid obstruction positions
obstruction_positions = find_obstruction_positions(grid, start_pos, start_dir)

# Output the number of obstruction positions
print("Number of valid obstruction positions:", len(obstruction_positions))
