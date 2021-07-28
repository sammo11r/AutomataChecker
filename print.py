import math as mth
import pyperclip

def printDFA(D, Q, F):
	# Gather the alphabet Sigma
	Sigma = []

	for d in D:
		if d[2] in Sigma:
			continue
		Sigma.append(d[2])

	sigma = '{'

	for label in Sigma:
		sigma += label + ', '

	sigma = sigma[:-2]
	sigma += '}'

	# Gather the states
	states = '{'
	for q in Q:
		states = states + q[0] + ', '

	states = states[:-2]
	states = states + '}'

	# Gather all the transitions in delta
	delta = '{'
	for d in D:
		delta += '(' + d[0] + ', ' + d[1] + ', ' + d[2] + '), '

	delta = delta[:-2]
	delta = delta + '}'

	# Gather the final states
	final = '{'
	for f in F:
		final = final + f + ', '

	final = final[:-2]
	final = final + '}'

	# Append to 5-tuple <Q, Sigma, Delta, Q0, F>
	string = '(' + states + ', ' + sigma + ', ' + delta + ', ' + Q[0][0] 
	+ ', ' + final + ')'

	pyperclip.copy(string)
	pyperclip.paste()
	return string