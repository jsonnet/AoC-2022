# up, down, left, right
DIRECTIONS = [(-1,0),(1,0),(0,-1),(0,1)]

def look_around(data, x, y) -> bool:  #row,column  #return if visible
	
	# for each direction
	for dx,dy in DIRECTIONS:
		nx, ny = dx+x, dy+y

		hidden = False
		# while row, column in tree grid
		while 0 <= nx < len(data[x]) and 0 <= ny < len(data):  # row, col
			# if tree is smaller than -> be hidden
			if int(data[nx][ny]) >= int(data[x][y]):
				hidden = True
				break

			# look at whole direction towards the edge
			nx += dx
			ny += dy

		if not hidden:
			return True  # tree visible

	return False  # tree invisible

def look_around_view(data, x, y) -> int:  #row,column
	view_score = 1

	# for each direction
	for dx,dy in DIRECTIONS:
		nx,ny = dx+x, dy+y

		visible = 0
		# while row, column in tree grid
		while 0 <= nx < len(data[x]) and 0 <= ny < len(data):  # row, col
			# if tree is smaller than -> add visibility score
			if int(data[nx][ny]) >= int(data[x][y]):
				visible += int(data[nx][ny]) == int(data[x][y])
				break
			
			visible += 1

			# look at whole direction towards the edge
			nx += dx
			ny += dy

		# Multiply for each direction
		view_score *= visible

	return view_score



trees = [line.strip() for line in open("day08.txt").readlines()]

count = 0
best = 0

# for each line
for row, line in enumerate(trees):
	# for each char in line
	for column, char in enumerate(line):
		# look for visible trees
		if look_around(trees, row, column): 
			count +=1

		# get best scenic score
		best = max(best, look_around_view(trees,row,column))
			
			
print("Task1", count)
print("Task2", best)