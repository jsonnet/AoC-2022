import collections
import math
import re


def get_blueprints():
	with open("day19.txt") as file:
		for line in file:
			# bp_id, ore_cost, clay_cost, obs_cost_ore, obs_cost_clay, geo_cost_ore, geo_cost_obs
			yield [int(x) for x in re.findall(r"\d+", line)]


def get_max_geodes(blueprint, total_time):
	blueprint_id, ore_robot_ore_cost, clay_robot_ore_cost, obsidian_robot_ore_cost, obsidian_robot_clay_cost, geode_robot_ore_cost, geode_robot_obsidian_cost = blueprint
	max_ore_cost = max(ore_robot_ore_cost, clay_robot_ore_cost, obsidian_robot_ore_cost, geode_robot_ore_cost)

	# (ore_robots, clay_robots, obsidian_robots, geode_robots, ore, clay, obsidian, geode, remaining time)
	queue = collections.deque([(1, 0, 0, 0, 0, 0, 0, 0, total_time)])
	seen = set()
	max_geodes = 0

	while queue:
		ore_robots, clay_robots, obsidian_robots, geode_robots, ore, clay, obsidian, geode, time = queue.popleft()

		max_geodes = max(max_geodes, geode)

		if time == 0:
			continue

		# Prune resources to reduce state space -> accelerate bfs
		# For clay, if we have c_r clay robots and more than ob_r_c_cost + (ob_r_c_cost - c_r) * (t - 1) clay, we can buy a obsidian robot next. 
		# c_r + (ob_r_c_cost - c_r) * (t - 1) = (ob_r_c_cost - c_r) * (t - 2) + ob_r_c_cost, so we can keep affording to buy obsidian robots with still left over with clay.
		ore = min(ore, max_ore_cost + (max_ore_cost - ore_robots) * (time - 1))
		clay = min(clay, obsidian_robot_clay_cost + (obsidian_robot_clay_cost - clay_robots) * (time - 1))
		obsidian = min(obsidian, geode_robot_obsidian_cost + (geode_robot_obsidian_cost - obsidian_robots) * (time - 1))

		state = (ore_robots, clay_robots, obsidian_robots, geode_robots, ore, clay, obsidian, geode, time)

		if state in seen:
			continue

		seen.add(state)

		# The no of robots should only be the max amount of each resource cost to make a robot.
		# e.g. we have enough ore for an ore robot and less ore robots than the max ore cost.
		if ore >= ore_robot_ore_cost and ore_robots < max_ore_cost:
			queue.append(( ore_robots + 1, clay_robots, obsidian_robots, geode_robots, ore - ore_robot_ore_cost + ore_robots, clay + clay_robots, obsidian + obsidian_robots, geode + geode_robots, time - 1 ))
		
		if ore >= clay_robot_ore_cost and clay_robots < obsidian_robot_clay_cost:
			queue.append(( ore_robots, clay_robots + 1, obsidian_robots, geode_robots, ore - clay_robot_ore_cost + ore_robots, clay + clay_robots, obsidian + obsidian_robots, geode + geode_robots, time - 1 ))
		
		if ore >= obsidian_robot_ore_cost and clay >= obsidian_robot_clay_cost and obsidian_robots < geode_robot_obsidian_cost:
			queue.append(( ore_robots, clay_robots, obsidian_robots + 1, geode_robots, ore - obsidian_robot_ore_cost + ore_robots, clay - obsidian_robot_clay_cost + clay_robots, obsidian + obsidian_robots, geode + geode_robots, time - 1 ))
		
		if ore >= geode_robot_ore_cost and obsidian >= geode_robot_obsidian_cost:
			queue.append(( ore_robots, clay_robots, obsidian_robots, geode_robots + 1, ore - geode_robot_ore_cost + ore_robots, clay + clay_robots, obsidian - geode_robot_obsidian_cost + obsidian_robots, geode + geode_robots, time - 1 ))

		# Collect resources during one timestep
		queue.append(( ore_robots, clay_robots, obsidian_robots, geode_robots, ore + ore_robots, clay + clay_robots, obsidian + obsidian_robots, geode + geode_robots, time - 1 ))

	return max_geodes


# Results

blueprints = get_blueprints()
print("Part1", pt1:=sum(blueprint[0] * get_max_geodes(blueprint, 24) for blueprint in blueprints))
#assert(pt1==1650)

from itertools import islice  # Take only first 3 as slice, as blueprint is a generator

blueprints = get_blueprints()
print("Part2", pt2:=math.prod([get_max_geodes(blueprint, 32) for blueprint in islice(blueprints, 3)]))
#assert(pt2==5824)
