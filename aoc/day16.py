# [Source] online https://www.reddit.com/r/adventofcode/comments/zn6k1l/comment/j0fti6c/?utm_source=share&utm_medium=web2x&context=3
# on 16th Dec 2022.
# for the use of @functools.cache in combination with the function search ..instead of a custom dict to store *args in 
# correlation to a result and checking against in the next operation

from collections import defaultdict
import itertools, functools, re

Vertices = set()
Flow = dict()
Dist = defaultdict(lambda: 99)  # big value for keys not present (i.e. not valid tunnel)

# parse input
for vertex, flow, tunnels in re.findall(r'Valve (\w+) has flow rate=(\d*); tunnels? leads? to valves? (.*)', open('day16.txt').read()):
    # store valve node
    Vertices.add(vertex)
    if flow != '0': 
        # store flow
        Flow[vertex] = int(flow)
    for tunnel in tunnels.split(', '): 
        # store edges
        Dist[tunnel, vertex] = 1

# for k in Vertices:
#     for i in Vertices:
#         for j in Vertices:
#             Dist[i,j] = min(Dist[i,j], Dist[i,k] + Dist[k,j])

# floyd (-warshall) algorithm to compute shortest distance between i,j
for k, i, j in itertools.product(Vertices, repeat=3):
    Dist[i,j] = min(Dist[i,j], Dist[i,k] + Dist[k,j])

@functools.cache
def search(time, curr='AA', vs=frozenset(Flow), elephant=False):  # valveset needs to be hashable for - operation
    # -1 for opening the valve
    press = [Flow[valve] * (time - Dist[curr,valve]-1) + search(time - Dist[curr,valve]-1, valve, vs-{valve}, elephant) 
            for valve in vs if Dist[curr,valve] < time]
    press_e = [search(26, vs=vs) if elephant else 0]

    return max(press + press_e)

print("Part 1", pt1:=search(30))
#assert(pt1==1828)

print("Part 2", pt2:=search(26, elephant=True))
#assert(pt2==2292)