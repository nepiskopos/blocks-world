import random
import argparse
import time
from BlocksWorldProblem import *


def generate_state(n):
	
	# Create n discrete blocks and shuffle them for the initial state
	blocks = list(range(n))
	random.shuffle(blocks)
	
	# Number of stacks on table (at least 1, at most n)
	s = random.randint(1, n)
	
	# Number of placed blocks
	p = 0
	
	# List of stacks of blocks
	state = []
	
	# Randomly fill the s - 1 first stacks
	for i in range(s - 1):
		stack = []
		m = min(n - p, (n - p) - (s - i) + 1)
		b = random.randint(1, m)
		
		for j in range(b):
			let = chr(ord('A') + blocks[p + j])
			stack.append(let)
		
		state.append(stack)
		p = p + b
	
	# Fill the s (last) stack
	stack = []
	for j in range(n - p):
		let = chr(ord('A') + blocks[p + j])
		stack.append(let)
	
	state.append(stack)
	
	
	state = [tuple(i) for i in state]
	state = tuple(state)
	
	return state

#_______________________________________________________________________

def print_state(state):
	maxlen = max(map(len,state))
	stacks = [tuple(reversed(x)) for x in state]
	for i in range(maxlen, 0, -1):
		for stack in stacks:
			if len(stack) >= i:
				print(stack[i-1], end ='\t')
			else:
				print(" ", end ='\t')
		print("")

#_______________________________________________________________________


random.seed()

parser = argparse.ArgumentParser(description='Blocks World Problem')
parser.add_argument("--number", "-n", help="set total number of blocks", type=int)
args = parser.parse_args()

error=False
if args.number:
	if args.number < 1 or args.number > 26:
		print("The number of blocks must be a positive integer in range [1,26]")
		error=True
else:
	print("You must provide the number of blocks (positive integer in range [1,26])")
	error=True

if error:
	sys.exit(1)


initial = generate_state(args.number)
goal = generate_state(args.number)

p = BlocksWorldProblem(initial, goal)

print(" ")
print("Initial State: ", initial)
print_state(initial)
print(" ")
print("Unique Goal State: ", goal)
print_state(goal)
print(" ")

start = time.time()

s = astar_search(p)

end = time.time()

hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("Elapsed time: {:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))
print(" ")

sol = s.solution()		# The sequence of actions to go from the root to this node
path = s.path()			# The nodes that form the path from the root to this node
print("Solution: \n+{0}+\n|Action\t|\t\tState\t\t\t|Path Cost |\n+{0}+".format('-'*58))

for i in range(len(path)) :
	state = path[i].state
	cost = path[i].path_cost
	action = "-"
	if i > 0 :			# The initial state has not an action that results to it
		action = sol[i-1]
	print("|{0}\t|{1}\t|{2}\t|".format(action, state, cost))
print("+{0}+".format('-'*42))
