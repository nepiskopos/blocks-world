# Blocks World problem ( awesome... -_- )

from search import *	# This file imports utils.py , so it should be in the same folder
import sys				# System-specific parameters and functions

class BlocksWorldProblem(Problem):
	"""Subclass of search.Problem"""
	
	def __init__(self, initial, goal) :
		# Sets initial state and goal state.
		# States are representated as a tuple of tuples ( (), ... , () )
		# where the base tuple is the "table" ( stacks of one or more
		# blocks sitting on the table ) when all the internal tuples are
		# the stacks of blocks, from the higher block (left) to the
		# lower block (right).
		
		self.total = sum(len(i) for i in goal)
		
		super(BlocksWorldProblem, self).__init__(initial, goal)

#_______________________________________________________________________

	def actions(self, state) :
		# Returns the actions that can be executed in the state
		# Invalid actions are those that move a block from a single-block
		# stack to another empty place on the table and create a new
		# single-block stack (that's basically the same state as before)
		# and the actions that "ruin" a properly formed stack ( a stack
		# that exists in the goal state ).
		# Actions are tuples in the form of ( from , to ) or to be
		# exact ( source_stack , destination_stack )
		
		validActions = []
		available = []
		
		for i in range(len(state)):
			
			flag = False
			
			for j in range(len(self.goal)):
				
				if state[i] == self.goal[j]:
					flag = True
					break
			
			if flag == False and i not in available:
				available.append(i)
		
		for i in available:
			for j in available:
				if (i != j) and ((i,j) not in validActions) and ((j,i) not in validActions):
					validActions.append((i,j))
					validActions.append((j,i))
			if len(state[i]) > 1:
				validActions.append((i,len(state)))
		
		return tuple(validActions)

#_______________________________________________________________________

	def result(self, state, action) :
		# Returns the new state which is the result of
		# applying the given action
		
		tstate = [list(i) for i in state]
		
		block = tstate[action[0]].pop(0)
		
		if action[1] == len(tstate):
			# Out of bounds
			tstate.append([block])
		else:
			tstate[action[1]].insert(0, block)
			#tstate[action[1]].append(block)
		
		if not tstate[action[0]]:
			# Empty stack
			tstate.pop(action[0])
		
		nstate = [tuple(i) for i in tstate]
		
		return tuple(nstate)

#_______________________________________________________________________

	def goal_test(self, state) :
		# Checks wether the current state matches the goal state.
		# The order of stacks on the table does not play any role in
		# the comparison, so we do not mind the order.
		
		ident = 0
		
		if len(state) != len(self.goal):
			return False
		
		for ss in state:
			for gs in self.goal:
				
				if ss == gs:
					ident = ident + 1
		
		return ident == len(self.goal)

#_______________________________________________________________________

	def h(self, node) :
		# Heuristic function h1 that finds an approach of the "distance"
		# ( number of actions ) between the current state and the goal
		# state.
		# The distance here is calculated by comparing the current state
		# to the goal state block-by-block. The distance is given by the
		# total number of blocks that are not in the right place ( right
		# stack and right position in the stack , in relation to the
		# rest of the blocks lower in the stack).
		
		right = 0
		
		for gs in self.goal:
			for ss in node.state:
				m = min(len(ss) , len(gs))
				for k in range(m):
					if ss[len(ss) - 1 - k] == gs[len(gs) - 1 - k]:
						right += 1
					else:
						break
		
		return self.total - right
