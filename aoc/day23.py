with open('day23.txt') as f:
    elves = { complex(x,y) for y,row in enumerate(f.readlines()) for x,c in enumerate(row) if c=='#' }

directions = [ -1j, 1j, -1, 1 ]  #(0,-1), (0,1), (-1,0), (1,0)
directions_around = [1,1+1j,1j,1j-1,-1,-1-1j,-1j,1-1j]  # (1, 0), (1.0, 1.0), (0.0, 1.0), (-1.0, 1.0), (-1, 0), (-1.0, -1.0), (-0.0, -1.0), (1.0, -1.0)

iteration = 0
while True:
    iteration += 1
    proposals = {}
    # For every elf
    for xy in elves:
        tiles_around = [ xy+d for d in directions_around ]
        x,y = xy.real, xy.imag

        elf_can_move = False
        # Check each tile around
        for pxy in tiles_around:
            # if there is another elf
            if pxy in elves:
                # Try all four directions, but ..
                for dxy in directions:
                    dx,dy = dxy.real, dxy.imag
                    pos_to_check = []
                    propose_move = True

                    # Test for valid direction
                    for pxy in tiles_around:
                        px,py = pxy.real, pxy.imag
                        if (dx == 0 and py - y == dy) or (dy == 0 and px - x == dx):
                            if pxy in elves:
                                propose_move = False
                                break
                    if propose_move:
                        if xy+dxy in proposals:
                            proposals[xy+dxy] = None
                        else:
                            proposals[xy+dxy] = (x,y)
                        break

                # .. elf can move only in one direction
                break

    # No movements left
    if not proposals:
        break
    for pxy, elf in proposals.items():
        if elf:
            elves.remove(complex(elf[0], elf[1]))
            elves.add(pxy)
    
    xs = [elf.real for elf in elves]
    ys = [elf.imag for elf in elves]

    directions = directions[1:] + directions[:1]

    # empty tiles in smallest rectangle after 10 rounds
    if iteration == 10:
        print("Part1", pt1:=(max(xs) - min(xs)+1) * (max(ys)-min(ys)+1) - len(elves))
        assert(pt1 == 3684)

# last iteration step
print('Part2', pt2:=iteration)
assert(pt2==862)
