import string
from collections import deque

CHAR_SCORE_MAP = {c: i for i, c in enumerate(string.ascii_lowercase)}

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_valid_neighbour(grid, dest_row, dest_col, current_value):
	if ( dest_row < 0 or dest_col < 0 or dest_row >= len(grid) 
		or dest_col >= len(grid[0]) ):
		return False

	if current_value == "S":
		current_value = "a"

	dest_value = grid[dest_row][dest_col]

	if dest_value == "E":
		dest_value = "z"

	return CHAR_SCORE_MAP[dest_value] <= CHAR_SCORE_MAP[current_value] + 1

def find_start_position(grid: list[str]) -> tuple[int, int]:
	for row_idx, l in enumerate(grid):
		for col_idx, c in enumerate(l):
			if c == "S":
				return (row_idx, col_idx)

def find_all_low_positions(grid: list[str]) -> tuple[int, int]:
	for row_idx, l in enumerate(grid):
		for col_idx, c in enumerate(l):
			if c == "S" or c == "a":
				yield (row_idx, col_idx)

# Breadth-first search
def find_shortest_path(grid: list[str], start_positions: list[tuple[int, int]]) -> int:
	visited: set[tuple[int, int]] = set(start_positions)
	queue: deque[tuple[tuple[int, int], int]] = deque((p, 0) for p in start_positions)

	while queue:
		(current_row, current_col), current_step_count = queue.popleft()

		current_value = grid[current_row][current_col]

		if current_value == "E":
			return current_step_count

		# for neighbour in graph[current]
		for offset_row, offset_col in MOVES:
			new_coord = (current_row + offset_row, current_col + offset_col)

			if new_coord not in visited and is_valid_neighbour( 
				grid, new_coord[0], new_coord[1], current_value ):
				visited.add(new_coord)
				queue.append((new_coord, current_step_count + 1))

	print("No path to destination")



grid = [l.strip() for l in open("day12.txt").readlines()]

start_positions = [find_start_position(grid)]
print("Task 1", find_shortest_path(grid, start_positions) )

start_positions = list(find_all_low_positions(grid))
print("Task 2", find_shortest_path(grid, start_positions) )
