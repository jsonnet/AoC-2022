def buildCrates(lines):
	crates = {}

	for i, c in enumerate(lines[8]):
		if c.isnumeric():
			for n in range(0,8):
				if lines[n][i].isalpha():
					if c in crates:
						crates[c].append(lines[n][i])
					else:
						crates[c] = [lines[n][i]]

	return crates

def task1_move(lines, crates):
	for line in lines[10:]:
		move = line.strip().split(' ')
		for i in range(int(move[1])):
			crates[move[5]].insert(0,crates[move[3]].pop(0))

	return crates  # Return for ease of use 

def task2_move(lines, crates):
	for line in lines[10:]:
		move = line.strip().split(' ')
		tmp = []
		for i in range(int(move[1])):
			tmp.append(crates[move[3]].pop(0))
		crates[move[5]] = tmp + crates[move[5]]

	return crates  # Return for ease of use 

with open('day05.txt') as f:

	lines = f.readlines()
	crates = buildCrates(lines)

	# Use deepcopy to run both at the same time, as crates will only shallow copy (i.e not nested list when passed as reference)

	#print("Task1", "".join([crates[c][0] for c in task1_move(lines, crates)]))
	print("Task2", "".join([crates[c][0] for c in task2_move(lines, crates)]))