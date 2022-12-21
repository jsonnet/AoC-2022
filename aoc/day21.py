def eval_expr(e):
    actions = monkeys[e]
    # Leaf case -> return number
    if len(actions) == 1:
        return actions[0]

    # Split expression and solve recursively
    left_expr, op, right_expr = actions
    return "(" + eval_expr(left_expr) + op + eval_expr(right_expr) + ")"


# Parse monkeys into dict
monkeys = { monkey: actions.split() for line in open("day21.txt").readlines()
      for monkey, actions in [line.strip().split(": ")]
}

# eval to root
print("Part1", pt1:=eval(eval_expr("root")))
assert(pt1==66174565793494)


### Source for real/imag computation at https://www.reddit.com/r/adventofcode/comments/zrav4h/comment/j133ko6/ on Dec 21th 2022
# Give humn complex number i to reduce expression automatically
monkeys["humn"] = ["-1j"]
# use schema round((b - a.real) / a.imag)
monkeys["root"][1] = "-("
c = eval(eval_expr("root") + ")")

# evaluate 
print("Part2", pt2:=round(c.real / c.imag))
assert(pt2==3327575724809)
