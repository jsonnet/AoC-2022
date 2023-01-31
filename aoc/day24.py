from collections import deque, namedtuple

# values inside tuple can be called similar to a class object
Blizzards = namedtuple('Blizzards', ['rows', 'cols', 'left', 'right', 'up', 'down'])

def parse(data):
    lines = [line[1:-1] for line in data.splitlines()[1:-1]] # Cut off walls
    rows, cols = len(lines), len(lines[0])

    # Parse each blizzard going its direction into own set
    left = { (x, y) for x in range(rows) for y in range(cols) if lines[x][y] == '<' }
    right = { (x, y) for x in range(rows) for y in range(cols) if lines[x][y] == '>' }
    up = { (x, y) for x in range(rows) for y in range(cols) if lines[x][y] == '^' }
    down = { (x, y) for x in range(rows) for y in range(cols) if lines[x][y] == 'v' }

    return Blizzards(rows, cols, left, right, up, down)

def shortest_path(blizzard, start, end, start_time):
    # BFS
    visited = set()
    queue = deque()
    while True:

        while not queue:
            start_time += 1  # To enter the board it takes one timestep
            if is_free(blizzard, start[0], start[1], start_time):
                queue.append((start[0], start[1], start_time))

        x, y, time = queue.popleft()
        if (x, y, time) in visited:
            continue
        visited.add((x, y, time))

        # Exit reached
        if (x, y) == end:
            return time + 1

        # Check each position
        for dxy in [ 1j, -1j, 1, -1, 0 ]:
            nx, ny = x + dxy.real, y + dxy.imag
            # If there is no blizzard -> add to queue as possible path
            if 0 <= nx < blizzard.rows and 0 <= ny < blizzard.cols and is_free(blizzard, nx, ny, time + 1):
                queue.append((nx, ny, time + 1))

def is_free(blizzard, x, y, time):
    # Check if there is a blizzard at timestep time and pos x,y going LRUD
    return not any((
        (x, (y + time) % blizzard.cols) in blizzard.left,
        (x, (y - time) % blizzard.cols) in blizzard.right,
        ((x + time) % blizzard.rows, y) in blizzard.up,
        ((x - time) % blizzard.rows, y) in blizzard.down,
    ))  # time moves the coord


blizzard = parse(open("day24.txt").read())
start = (0, 0)
end = (blizzard.rows - 1, blizzard.cols - 1)

# First run through
t1 = shortest_path(blizzard, start, end, 0)
# Going back to entrance
t2 = shortest_path(blizzard, end, start, t1)
# And second run through
t3 = shortest_path(blizzard, start, end, t2)

print("Part1", pt1:=t1)
#assert(pt1==245)

print("Part2", pt2:=t3)
#assert(pt2:=798)
