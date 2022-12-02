
score = 0

# A Rock, B Paper, C Scissors # op
# X Rock, Y Paper, Z Scissors # me
# 1 Rock, 2 Paper, 3 Scissors, 6 win, 3 draw

with open('day02.txt') as f:

	for line in f:
		if line[0] == 'A':
			if line[2] == 'X':
				score += (1+3)

			elif line[2] == 'Y':
				score += (2+6)

			elif line[2] == 'Z':
				score += (3+0)

		if line[0] == 'B':
			if line[2] == 'X':
				score += (1+0)

			elif line[2] == 'Y':
				score += (2+3)

			elif line[2] == 'Z':
				score += (3+6)

		if line[0] == 'C':
			if line[2] == 'X':
				score += (1+6)

			elif line[2] == 'Y':
				score += (2+0)

			elif line[2] == 'Z':
				score += (3+3)

	f.seek(0)
	print("first score:", score)
	score = 0


	for line in f:
		if line[0] == 'A':
			if line[2] == 'X':
				score += (3+0)

			elif line[2] == 'Y':
				score += (1+3)

			elif line[2] == 'Z':
				score += (2+6)

		if line[0] == 'B':
			if line[2] == 'X':
				score += (1+0)

			elif line[2] == 'Y':
				score += (2+3)

			elif line[2] == 'Z':
				score += (3+6)

		if line[0] == 'C':
			if line[2] == 'X':
				score += (2+0)

			elif line[2] == 'Y':
				score += (3+3)

			elif line[2] == 'Z':
				score += (1+6)

	print("second score:", score)