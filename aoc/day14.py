def parseMap(data):
    # create sufficiently sized grid filled with air pockets
    width, height = 500, 256
    grid = [[ '.' ] * width for _ in range(height)]

    # helper to translate x into our grid offset
    translate_x = lambda x: x - (500 - width // 2)

    # add rocks
    max_y = 0
    for line in data:
        # Split at -> and map to 'Split at comma and map to int' as list, resulting in a list of list tuples 
        steps = list(map(lambda s: list(map(int, s.split(','))), line.split(' -> ')))

        # Each step with the next one (without skipping one, i.e following the original arrows)
        for (x, y), (dest_x, dest_y) in zip(steps, steps[1:]):
            while True:

                # Placing rocks
                grid[y][translate_x(x)] = '#'
               
                if x != dest_x:  # Range for x
                    x += 1 if x < dest_x else -1 
                elif y != dest_y:  # Range for y
                    y += 1 if y < dest_y else -1 
                else:  # no more rocks
                    break

                # keep track of max y position so we know where abyss is 
                max_y = max(y, max_y)

    # create floor 
    for x in range(width):
        grid[max_y+2][x] = '#'
    
    return grid, translate_x, max_y


def solve(grid, translate_x, max_y) -> tuple[int, int]:
    
    resting_sands = 0
    sand_pt1 = 0
    sand_source = (translate_x(500), 0)
    path = [sand_source]

    # Place sand indefinitely
    while path:
        x, y = path.pop()

        # Simulate flowing sand
        while True:
            # Save resting sand value for pt1 when we start to overflow into abyss
            if not sand_pt1 and y > max_y:
                sand_pt1 = resting_sands

            # Store all valid sand positions, i.e. the path
            path.append((x, y))

            # Below is air
            if grid[y+1][x] == '.':
                y += 1 
            # Left is air
            elif grid[y+1][x-1] == '.':
                y += 1
                x -= 1 
            # Right is air
            elif grid[y+1][x+1] == '.':
                y += 1 
                x += 1 
            # No air around
            else:
                break  # sand comes to a rest


        # place resting sand 
        grid[y][x] = 'o'
        resting_sands += 1
        path.pop()  # as we want to further simulate from the previous point
        
        # stop if we blocked source of sand
        if (x, y) == sand_source:
            break
    
    return sand_pt1, resting_sands  # pt1, pt2


with open("day14.txt") as f:
    data = f.read().strip().split('\n')
    grid, translate_x, max_y = parseMap(data)

pt1, pt2 = solve(grid, translate_x, max_y)
print("Part 1:", pt1)
print("Part 2:", pt2)
# assert(pt1 == 1016)
# assert(pt2 == 25402)
