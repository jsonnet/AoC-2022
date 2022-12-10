data = open('day10.txt').readlines()

cycles = []
for line in data:
	# first cycle
	cycles.append(0)  # This has the assumption, there are no empty lines in data
	if 'addx' in line:
		# in case of addx add second cycle
		cycles.append(int(line.strip().split(' ')[1]))


res, x = 0, 1
crtScreen = [' '] * 240  # (40 * 6) screen

for idx, step in enumerate(cycles, start=0):
	# draw pixel
	if x - 1 <= idx % 40 <= x + 1:
		crtScreen[idx] = '#'

	# After 20th and every 40 cycles
	if (idx + 1) % 40 == 20:
		# mult cycle count with register X to signal strength result
		res += (idx + 1) * x

	# add register X
	x += step


print("Task 1:", res)
print("Task 2:")
for r in range(6):
	print(''.join(crtScreen[r * 40: r * 40 + 40]))
