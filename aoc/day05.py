def buildCrates(lines):
	crates = {}

	for i, c in enumerate(lines[8]):
		if c.isnumeric():
			# build stack from bottom up (but limited to 8 high)
			for n in range(0,8):
				# isalpha due to non existent crates
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
	print("Task1", pt1:="".join([crates[c][0] for c in task1_move(lines, crates)]))
	#assert(pt1 == "JDTMRWCQJ")

	crates = buildCrates(lines)
	print("Task2", pt2:="".join([crates[c][0] for c in task2_move(lines, crates)]))
	#assert(pt2 == "VHJDDCWRD")