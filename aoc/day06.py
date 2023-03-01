def find_marker(input_str, length) -> int:
	marker = []

	# start=1 as chars start with counting 1
	for i, c in enumerate(input_str, start=1):
		# makeshift FIFO of length length
		if len(marker) == length:
			marker.pop(0)
		marker.append(c)

		# check if marker has only unique chars
		if len(set(marker)) == length:
			print(i, ''.join(set(marker)))
			return i


with open("day06.txt") as f:

	input_str = f.read()

	find_marker(input_str, 4)
	find_marker(input_str, 14)

	
