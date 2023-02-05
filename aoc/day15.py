from dataclasses import dataclass
import re

@dataclass
class Point:
    __slots__ = ("x", "y")
    x: int 
    y: int 

    def manhattan_distance(self, other) -> int: 
        return abs(self.x - other.x) + abs(self.y - other.y)


class Sensor:
    __slots__ = ("x", "y", "size")

    def __init__(self, coords: Point, beacon: Point):
        self.x = coords.x 
        self.y = coords.y 

        # estimate size of sensor area, i.e. sensor area "circle"
        self.size = self.manhattan_distance(beacon.x, beacon.y) 

    def manhattan_distance(self, ox, oy) -> int:
        return abs(self.x - ox) + abs(self.y - oy)

    # if sensor covers point px,py 
    def covers(self, px, py):
        """ Returns either False, if the sensor does not cover x,y else it returns the outer x coordinate"""
        y_diff = abs(py - self.y)
        x_size = self.size - y_diff
        # position is outside of sensor range
        if x_size <= 0:
            return False

        # left bound
        x_start = self.x - x_size
        if x_start > px:
            return False

        # right bound
        x_end = self.x + x_size
        if x_end < px:
            return False

        # returns where the sensor area ends
        return x_end


def parse(input) -> list:
    input = re.findall(r'x=(-?\d+), y=(-?\d+)(?:.*)x=(-?\d+), y=(-?\d+)', input)

    sensors = []
    for sx, sy, bx, by in input:
        sensors.append((Point(int(sx), int(sy)), Point(int(bx), int(by))))  # sensor, beacon

    return sensors

def count_excluded_positions(sensors, search_y=2000000):
    ranges = []
    exclusions = set()
    
    for s, b in sensors:
        dy = -1 if s.y > search_y else 1  # y direction
        top = Point(s.x, search_y)

        # if sensor is not within range, continue with next sensor
        treshold = s.manhattan_distance(b)  # distance sensor -> beacon
        while s.manhattan_distance(top) < treshold:
            top.y += dy

        diff = abs(top.y - search_y)  # Compute vertical distance to search_y row
        if diff == 0:
            continue

        # Create interval
        start = s.x - diff
        end = s.x + diff
        ranges.append([start, end])

        if b.y == search_y:
            exclusions.add(b.x)

    # Compress ranges and compute len of ranges
    ranges = compress_ranges(ranges)
    count = sum(interval[1] - interval[0]+1 for interval in ranges)
    count -= len(exclusions)

    return count

def compress_ranges(intervals: list) -> list:
        """Compress overlapping intervals to minimum number of non-overlapping intervals. """
    
        intervals.sort()
        stack = [intervals[0]]
        
        for interval in intervals[1:]:
            # Check for overlapping interval
            if stack[-1][0] <= interval[0] <= stack[-1][-1]:
                stack[-1][-1] = max(stack[-1][-1], interval[-1])
            else:
                stack.append(interval)
         
        return stack

def find_position(sensors, lim=4000000):
    px, py = 0, 0
    sensors = [Sensor(s, b) for s, b in sensors]

    free_beacon_pos = False
    while not free_beacon_pos:
        free_beacon_pos = True

        # For every sensor
        for s in sensors:
            # Jump to next x position after sensor area, if position is already covered
            next_x = s.covers(px, py)

            if next_x != False:
                px = next_x + 1

                free_beacon_pos = False

                # Coordinates must not be larger than limit, thus we look into next y from x=0
                if px >= lim:
                    px = 0
                    py += 1

                # go to next x, y position
                break

    return px * 4000000 + py


with open("day15.txt") as f:
    input = f.read()

sensors = parse(input) 

# pt1
pt1 = count_excluded_positions(sensors, 2000000) 
print("pt1: ", pt1)
#assert(pt1 == 5125700)

# pt2
pt2 = find_position(sensors, 4000000) 
print("pt2: ", pt2)
#assert(pt2 == 11379394658764)
