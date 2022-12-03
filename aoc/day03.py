from itertools import islice


def readIntersection() -> str: 
	with open('day03.txt') as f:
		for line in f:
			com1 = line[:len(line)//2]
			com2 = line[len(line)//2:]

			inter = ''.join(set(com1).intersection(com2))

			yield inter

def task1():
	items = [ord(i)-96 if i.islower() else ord(i) - 38 for i in readIntersection()]

	print("common item prio:", sum(items))



def readinThree():
	with open("day03.txt") as f:
		group = []

		for line in f:
			group.append(line.strip())
			if len(group) >= 3:
				yield group
				group = []

def intersectThree() -> str:
	for group in readinThree():
		yield list(set(group[0]) & set(group[1]) & set(group[2]))[0]

def task2():
	items = [ord(i)-96 if i.islower() else ord(i) - 38 for i in intersectThree()]
	print("common badge prio:", sum(items))


task1()
task2()