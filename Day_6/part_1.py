class DirectionNode:
    """Represents a node in a cyclic linked list for directions."""
    def __init__(self, name, delta):
        self.name = name  # Direction name: 'up', 'right', 'down', 'left'
        self.delta = delta  # (row change, col change)
        self.next = None  # Pointer to the next node

# Create nodes for each direction
up = DirectionNode("up", (-1, 0))
right = DirectionNode("right", (0, 1))
down = DirectionNode("down", (1, 0))
left = DirectionNode("left", (0, -1))

# Link the nodes cyclically
up.next = right
right.next = down
down.next = left
left.next = up

def move_guard(grid, row, col, direction_node, visited_count):
    """Move the guard in the specified direction until an obstacle or boundary is hit."""
    dr, dc = direction_node.delta
    while 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]) and grid[row + dr][col + dc] != "#":
        row += dr
        col += dc
        if grid[row][col] != "X":
            visited_count += 1
            grid[row][col] = "X"
    return row, col, visited_count

# Read input map
with open("Day_6/input_day_6.txt", "r") as file:
    lines = [list(line.strip()) for line in file.readlines()]
    row, col = 0, 0
    count_unique_visited_places = 1

    # Find the initial position of the guard
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "^":
                row, col = i, j
                lines[i][j] = "X"  # Mark starting position as visited
                break

# Navigation
current_direction = up  # Start with 'up' direction
while True:
    # Move guard in the current direction
    row, col, count_unique_visited_places = move_guard(
        lines, row, col, current_direction, count_unique_visited_places
    )
    dr , dc = current_direction.delta
    if row+dr < 0 or row+dr >= len(lines) or col+dc < 0 or col+dc >= len(lines[0]):
         break
    # Change direction to the next in the cycle
    current_direction = current_direction.next
    

# Write output map with the patrol path
with open("Day_6/output.txt", "w") as file:
    for line in lines:
        file.write("".join(line) + "\n")

# Print the number of unique positions visited
print(count_unique_visited_places)
