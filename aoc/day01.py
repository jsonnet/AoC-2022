
elfCalories = []

with open('day01.txt') as f:

	lines = f.readlines()

	elf = 0
	calories = 0

	for line in lines:
		if line == '\n':
			elfCalories.insert(elf, calories)
			elf += 1
			calories = 0
		else:
			calories += int(line.strip())

elfCalories = sorted(elfCalories, reverse=True)

print("Max calories:", elfCalories[0])
print("Top3 calories:", sum(elfCalories[i] for i in range(0,3) ))
