with open('day23.txt') as f:
    elves = { complex(x,y) for y,row in enumerate(f.readlines()) for x,c in enumerate(row) if c=='#' }

directions = [ -1j, 1j, -1, 1 ]  #(0,-1), (0,1), (-1,0), (1,0)
directions_around = [1,1+1j,1j,1j-1,-1,-1-1j,-1j,1-1j]  # (1, 0), (1, 1), (0, 1), (-1.0, 1.0), (-1, 0), (-1, -1), (-0, -1), (1, -1)

iteration = 0
while True:
    iteration += 1
    proposals = {}
    
    # For every elf
    for xy in elves:
        tiles_around = [ xy+d for d in directions_around ]
        x,y = xy.real, xy.imag

        # Check each tile around (first half)
        for pxy in tiles_around:
            # if there is another elf (else do nothing)
            if pxy in elves:
                # Try all four directions, but ..
                for dxy in directions:
                    dx,dy = dxy.real, dxy.imag
                    propose_move = True

                    # Test for valid direction if there is no elf (i.e. for N -> N, NE, NW)
                    for pxy in tiles_around:
                        px,py = pxy.real, pxy.imag

                        if (dx == 0 and py - y == dy) or (dy == 0 and px - x == dx):
                            # Found an elf so cannot move there
                            if pxy in elves:
                                propose_move = False
                                break  # next tile

                    # Only move there if no other elf already proposed that move, else nobody will move
                    if propose_move:
                        if xy+dxy in proposals:
                            proposals[xy+dxy] = None  # prune move suggesting
                        else:
                            proposals[xy+dxy] = (x,y)
                        break

                # .. elf can move only in one direction (first valid one)
                break

    # No movement proposals
    if not proposals:
        break
    # Move elf
    for pxy, elf in proposals.items():
        if elf:
            elves.remove(complex(elf[0], elf[1]))
            elves.add(pxy)
    
    xs = [elf.real for elf in elves]  # All elf x positions
    ys = [elf.imag for elf in elves]  # All elf y positions

    # First direction considered is moved to end of list
    # [-1j, 1j, -1, 1] -> [1j, -1, 1, -1j] -> [-1, 1, -1j, 1j] -> [1, -1j, 1j, -1]
    directions = directions[1:] + directions[:1]

    # empty tiles in smallest rectangle after 10 rounds
    if iteration == 10:
        print("Part1", pt1:=(max(xs) - min(xs)+1) * (max(ys)-min(ys)+1) - len(elves))
        #assert(pt1 == 3684)

# last iteration step
print('Part2', pt2:=iteration)
#assert(pt2==862)
