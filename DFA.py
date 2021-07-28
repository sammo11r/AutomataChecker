# Returns True if the submitted DFA accepts the set of words W, 
# and False otherwise.
#
# @param dfa - the Deterministic Finite Automaton, represented as a list
# @param W   - the set of words to be checked
#
# @pre dfa[0] == the transition function, dfa[1] == starting state, 
#      dfa[2] == set of final states
# @post \return True if dfa accepts W, \return False if dfa rejects W

def checkDFA(dfa, W):
	# Extract the DFA
	D = dfa[0]
	q0 = dfa[1]
	F = dfa[2]

	# Set the counter for the amount of reached states
	reached = 0

	# For each word in the set of words
	for w in W:
		if w == "":
			reached +=1
		else:
			# Check if the word ends in a final state
			reached = checkWord(D, q0, F, reached, w)

	# If the amount of reached states is equal to |W|, and is not equal to 0,
	if reached == len(W) and reached != 0:
		# The DFA is valid for the words in W
		return True
	else:
		# Else, the DFA rejects at least 1 word in W
		return False


# Returns @code{reached + 1} if the submitted DFA accepts the word w, 
# and @code{reached} otherwise.
#
# @param D       - the transition function
# @param q0      - the starting state
# @param F       - the set of final states
# @param reached - the counter to be incremented
# @param w       - the word to be checked

def checkWord(D, q0, F, reached, w):
	# Set the current state to the starting state
	currentState = q0

	# While w is not the empty string
	while ((not w) == False):
        # Check for a valid transition, and set currentState
		temp = checkTransition(D, w, currentState)
		
		# Check the state of the transition
		if (temp == False):
			return reached

		currentState = temp[0]
		w = temp[1]

		# If w is the empty string
		if not w:
			# Check for each state in the set of final states,
			for f in F:
				# if the current state is a final state,
				if currentState == f:
					# increase the counter
					reached += 1
					break
	return reached

# Returns the tuple @code{(currentState, w)}, if the submitted DFA accepts the word w, 
# and @code{reached} otherwise.
#
# @param D            - the transition function
# @param w            - the string to be checked
# @param currentState - the current state of the DFA

def checkTransition(D, w, currentState):
	# For all transitions in Delta	
	for t in D:
		# If we are in said transitions currentstate, 
		# and the transition label is the specified word
		if (t[0] == currentState and t[2] == w[0]):
			# Set the current state and update w
			currentState = t[1]
			w = w[1:]

			return currentState, w

	# If all transitions have been checked, return false
	return False

# Returns the 3-tuple @code{(False, state, input)}, if the submitted DFA is not a valid DFA, 
# and @code{(True, None, None)} otherwise.
#
# @param D - the transition function

def validDFA(D):
	temp = []
	for d in D:
		if (d[0], d[2]) in temp:
			return False, d[0], d[2]
		temp.append((d[0], d[2]))
	return True, None, None