ROCKS = (
    (0,1,2,3),  # HLine
    (1,0+1j,1+1j,2+1j,1+2j), # Cross
    (0,1,2,2+1j,2+2j),  # RevL
    (0,0+1j,0+2j,0+3j),  # VLine
    (0,1,0+1j,1+1j)  # Cube
    )

def check_chamber(pos, rock, tower):
    # Check each rock position
    for r in rock:
        npos = pos+r
        # If x is out of bounds of 7 wide chamber or y is below floor or y collides with other rock
        if npos.real not in range(7) or npos.imag <= 0 or npos in tower:
            return False

    return True


def sim_rock_tetris(jets, tower=set(), cache=dict()):
    idx_rock, idx_jet, top_y = 0, 0, 0
    
    for step in range(int(1e12)):
        # left edge is two units away from the left wall and 
        # its bottom edge is three units above the highest rock/floor
        pos = complex(2, (top_y+1) + 3)  # set pos x=2, y=floor+3

        # Part 1
        if step == 2022: 
            print("Part1", top_y)
            assert(top_y == 3071.0)

        key = idx_rock, idx_jet

        if key in cache:
            c_step, c_top_y = cache[key]
            div, mod = divmod(1e12 - step, step - c_step)

            # Part 2
            if mod == 0: 
                print("Part2", pt2:=top_y + (top_y - c_top_y)*div)
                assert(pt2 == 1523615160362.0)
                break
        else: 
            cache[key] = step, top_y

        # Get next rock
        rock = ROCKS[idx_rock]
        idx_rock = (idx_rock+1) % len(ROCKS)

        while True:
            # Get next jet direction
            jet = 1 if jets[idx_jet] == '>' else -1
            idx_jet = (idx_jet+1) % len(jets)

            # First Check being pushed by jet
            if check_chamber(pos + jet, rock, tower): 
                pos += jet
            # Second Check falling down
            if check_chamber(pos + -1j, rock, tower): 
                pos += -1j
            # Rock landed
            else: 
                break

        # List of all positions where a rock is 
        tower.update( {pos+r for r in rock} )
        # Update top with `y + height(rock)`
        top_y = max(top_y, pos.imag+[0,2,2,3,1][idx_rock-1])


jets = open('day17.txt').read().strip()
sim_rock_tetris(jets)