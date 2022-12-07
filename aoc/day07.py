
class DirTree:
    def __init__(self, name: str, parent=None):
        self.name = name  # Dir name
        self.parent = parent  # Upper dir (tree node)
        self.sub_dirs = {}  # Lower dirs (tree nodes)
        self.files = {}  # Mapping between files and size in this dir

    def __repr__(self):
        return "&" + self.name

    def __iter__(self):
        # this yields every dir and sub dir recursively
        for sub_dir in self.sub_dirs.values():
            yield sub_dir
            for sd in sub_dir: 
                yield sd

    def set_size(self, size: int, name: str) -> None:
        self.files[name] = size

    def set_sub_dir(self, name: str):
        if name in self.sub_dirs:
            pass  # This should not happen unless, 'cd' is called twice in the same dir with the same dir (could simply also return without adding)
        else:
            self.sub_dirs[name] = DirTree(name, parent=self)
            return self.sub_dirs[name]

    @property
    def size(self) -> int:
        # recursively go tree down and sum up file sizes
        return sum(self.files.values()) + sum(sub_dir.size for sub_dir in self.sub_dirs.values())


def parseDirs(data, curr_dir):
    for line in data:
        line = line.split()

        # Do not care about those two, they do nothing for us
        if line[0] == "dir" or line[1] == "ls":
            continue
        elif line[1] == "cd":
            # Go back up
            if line[2] == "..":
                curr_dir = curr_dir.parent
            # Go into dir
            else:
                curr_dir = curr_dir.set_sub_dir(name=line[2])
        else: # Must be size output for file
            curr_dir.set_size(size=int(line[0]), name=line[1])


data = open("day07.txt").readlines()[1:]
root_dir = DirTree("/")  # Root noode i.e. root directory

parseDirs(data, root_dir)

print("Task 1:", sum(c.size for c in root_dir if c.size <= 100000))
print("Task 2:", min(c.size for c in root_dir if (70000000 - 30000000) + c.size >= root_dir.size))
