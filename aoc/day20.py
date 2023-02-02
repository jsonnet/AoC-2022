def mix(number_list, mix_iterations=1, dec_multiplier=1):
    list_size = len(number_list)

    number_list = [(i, n * dec_multiplier) for i, n in number_list]

    # For each mixing
    for _ in range(mix_iterations):
        # For each position in the list
        for i in range(list_size):
            # Find the next item
            for j in range(list_size):
                # if the right next items of the list is found (each item is a tuple with the original position)
                if number_list[j][0] == i:
                    # Save and delete value
                    num = number_list[j]
                    number_list.pop(j)

                    # Reinsert at position (with mod to be circular)
                    number_list.insert((j + num[1]) % (list_size-1), num)
                    break

    # Find 0 index
    zero_index = [x for _, x in number_list].index(0)

    # Sum the 1000th, 2000th and 3000th after that index
    return sum(number_list[(zero_index + i) % len(number_list)][1] for i in range(1000, 4000, 1000))

# Read input as tuple of (position, value)
number_list = list(enumerate(map(int, open("day20.txt").readlines())))

print("Part 1:", pt1:=mix(number_list[:]))
#ssert(pt1==13967)

print("Part 2:", pt2:=mix(number_list[:], 10, 811589153))
#assert(pt2==1790365671518)