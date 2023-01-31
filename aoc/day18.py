cubes = {tuple(map(int, line.strip().split(','))) for line in open('day18.txt').readlines()}

# yields every neighbour sides
sides = lambda x,y,z: {(x+1,y,z), (x-1,y,z), (x,y+1,z), (x,y-1,z), (x,y,z+1), (x,y,z-1)}


# for cube in cubes -> check every side of cube if side is in not cube, i.e. for every not connected side add up
print("Part1", pt1:= sum((side not in cubes) for cube in cubes for side in sides(*cube)))
#assert(pt1==4504)

max_coord = 0
for coord in cubes:
    m = max(coord)
    if m > max_coord:
        max_coord = m

#BFS
queue = [(-1,-1,-1)]
seen = set()

while queue:
    c = queue.pop()

    # FOR every neighbour (side in sides) AND not in cubes AND not already visited
    for s in (sides(*c) - cubes - seen):
        # check if every side is within range of highest point
        if all( -1 <= c <= max_coord+2 for c in s ):
            # Outside air found
            queue.append(s)

    seen.add(c)

# for cube in cubes -> check every side of cube if a path exist to an outside air side
print("Part2", pt2:=sum((s in seen) for c in cubes for s in sides(*c)))
#assert(pt2==2556)
