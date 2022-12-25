m# It's the last day of AoC so let us have some fun

# A unnecessary way to convert SNAFU to integers
def SNAFU_to_int(sym : chr) -> int:
    match(sym):
        case '2':
            return 2
        case '1':
            return 1
        case '0':
            return 0
        case '-':
            return -1
        case '=':
            return -2

# And the same reversed ( sure a mapping and it's reverse would also be valid )
def int_to_SNAFU(int : int) -> chr:
    match(int):
        case 2:
            return '2'
        case 1:
            return '1'
        case 0:
            return '0'
        case -1:
            return '-'
        case -2:
            return '='

def SNAFU_dec(sym_line : str) -> int:
    # 5^2 .. 5^1 .. 5^0 : 3 positions/ length of string
    snafu_dec = lambda x,y : x * ( 5 ** (y) )  # Lets use lambda to compute power of 5 for pos and num
    res = 0

    for i, char in enumerate(sym_line):
        res += snafu_dec(SNAFU_to_int(char), (len(sym_line)-i-1))  # I need the first position as being the last

    return res

def dec_SNAFU(num : int) -> str:
    value = []

    while num > 0:
        remainder = num % 5
        value.append(int_to_SNAFU(remainder - 5) if remainder > 2 else str(remainder))
        num = (num + remainder) // 5

    return ''.join(reversed(value))


with open("day25.txt") as f:
    data = f.read().splitlines()

print("Part 1", result := sum(SNAFU_dec(line) for line in data))
print("Part 2", dec_SNAFU(result))
