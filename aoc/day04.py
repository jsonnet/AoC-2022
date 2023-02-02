with open('day04.txt') as f:

	overlap, partover = 0, 0

	for line in f:

		# Creating actual python ranges from input
		r = line.strip().split(',')
		r1, r2 = [int(i) for i in r[0].split("-")], [int(i) for i in r[1].split("-")]
		r1, r2 = range(r1[0], r1[1]+1), range(r2[0], r2[1]+1)

		if (r1.start in r2 and (r1.stop-1 in r2)) or (r2.start in r1 and (r2.stop-1 in r1)):
			overlap += 1

		if r1.start in r2 or (r2.start in r1):
			partover += 1

	print("Part1", overlap, "\nPart2", partover)
	#assert(overlap == 490)
	#assert(partover == 921)
