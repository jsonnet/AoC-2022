
def sign(n):
	return -1 if n < 0 else (1 if n > 0 else 0)

moves = [(x.split(' ')[0], int(x.split(' ')[1])) for x in open("day09.txt").readlines()]

DIRECTIONS = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}  # x,y
kts = [[0, 0] for _ in range(10)]

visited_kts1, visited_kts9 = set(), set()

# For each move
for move in moves:
	# Repeat specified amount of times
	for _ in range(move[1]):
		# Programmatically move into specified direction (head/rest)
		kts[0] = [kts[0][0]+DIRECTIONS[move[0]][0], kts[0][1]+DIRECTIONS[move[0]][1]]
		# Integrated part 2, as kts[1] is part 1
		for i in range(1, 10):
			# maximum norm
			if max(abs(kts[i][0] - kts[i-1][0]), abs(kts[i][1] - kts[i-1][1])) > 1:
				# tail swing
				kts[i][0] += sign(kts[i-1][0] - kts[i][0])
				kts[i][1] += sign(kts[i-1][1] - kts[i][1])

		visited_kts1.add(tuple(kts[1])) # Part1: tail length only 1
		visited_kts9.add(tuple(kts[9])) # Part2: tail length 9

print("Task 1:", len(visited_kts1))
print("Task 2:", len(visited_kts9))
