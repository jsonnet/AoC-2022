with open("day13.txt") as f:
	data = f.read()

packets = [[eval(p) for p in l.split('\n')] for l in data.split("\n\n")]
ordered_packets = 0

def is_ordered(l, r) -> bool:
	maxLen = max(len(l), len(r))
	for index in range(maxLen):
		# Early out if one list is smaller
		if index >= len(l):
			return True
		if index >= len(r):
			return False

		l_val, r_val = l[index], r[index]
		if isinstance(l_val, int) and isinstance(r_val, int):
			if l_val < r_val:  # Left is smaller
				return True
			if l_val > r_val:  # Right is smaller
				return False
		elif isinstance(l_val, list) and isinstance(r_val, list):
			result = is_ordered(l_val, r_val)
			if result is not None:
				return result
		elif isinstance(l_val, int) and isinstance(r_val, list):
			result = is_ordered([l_val], r_val)
			if result is not None:
				return result
		elif isinstance(l_val, list) and isinstance(r_val, int):
			result = is_ordered(l_val, [r_val])
			if result is not None:
				return result
	
	# match case
	return None

ordered_packets = sum(idx for idx, pair in enumerate(packets, start=1) if is_ordered(pair[0], pair[1]) > 0)
print("Task 1", ordered_packets)

## Part 2
from functools import cmp_to_key
from itertools import chain

#packets = [[eval(p) for p in l.split('\n')] for l in data.replace('\n\n', '\n').split('\n')]
packets = list(chain.from_iterable(packets))
packets += [[[2]], [[6]]]

sortedPackets = sorted(packets, key=cmp_to_key(lambda a, b: -1 if is_ordered(a,b) else 1))

print("Task 2", (sortedPackets.index([[2]]) + 1) * (sortedPackets.index([[6]]) + 1))

