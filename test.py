# Import the necessary libraries
import unittest
from DFA import checkDFA, checkWord, checkTransition, validDFA

# Test cases for the DFA checker
class DFATest(unittest.TestCase):

	def test_emptyString(self):
		dfa = [[("q0", "q1", "a", 0)], "q0", ["q1"]]
		W = []
		self.assertEqual(checkDFA(dfa, W), False)

	def test_selfTransition(self):
		dfa = [[("q0", "q0", "a", 0)], "q0", ["q0"]]
		W = ["", "a", "aa", "aaa"]
		self.assertEqual(checkDFA(dfa, W), True)

	def test_oneTransition(self):
		dfa = [[("q0", "q1", "a", 0)], "q0", ["q1"]]
		W = ["a"]
		self.assertEqual(checkDFA(dfa, W), True)

	def test_multTransition(self):
		dfa = [[("q0", "q1", "a", 0)], "q0", ["q1"]]
		W = ["a", "a", "a", "a"]
		self.assertEqual(checkDFA(dfa, W), True)

	def test_emptyWord(self):
		D = [("q0", "q1", "a", 0)]
		q0 =  "q0"
		F = ["q1"]
		w = ''
		self.assertEqual(checkWord(D, q0, F, 0, w), 0)

	def test_wrongWord(self):
		D = [("q0", "q1", "a", 0)]
		q0 =  "q0"
		F = ["q1"]
		w = 'b'
		self.assertEqual(checkWord(D, q0, F, 0, w), 0)

	def test_oneWord(self):
		D = [("q0", "q1", "a", 0)]
		q0 =  "q0"
		F = ["q1"]
		w = 'a'
		self.assertEqual(checkWord(D, q0, F, 0, w), 1)

	def test_checkWordCounter(self):
		D = [("q0", "q1", "a", 0)]
		q0 =  "q0"
		F = ["q1"]
		w = 'a'
		self.assertEqual(checkWord(D, q0, F, 25, w), 26)

	def test_checkEmptyTransition(self):
		D = [("q0", "q1", " ", 0)]
		w = " "
		currentState = "q0"
		# Note that the resulting tuple is ("q1", ""), indicating that w is now empty 
		self.assertEqual(checkTransition(D, w, currentState), ("q1", ""))

	def test_checkWrongTransition(self):
		D = [("q0", "q1", "a", 0)]
		w = "ba"
		currentState = "q0"
		self.assertEqual(checkTransition(D, w, currentState), False)

	def test_checkOneTransition(self):
		D = [("q0", "q1", "a", 0)]
		w = "aa"
		currentState = "q0"
		self.assertEqual(checkTransition(D, w, currentState), ("q1", "a"))

	def test_validDFAempty(self):
		D = []
		self.assertEqual(validDFA(D), (True, None, None))

	def test_validDFAdouble(self):
		D = [("q0", "q1", "a", 0), ("q0", "q2", "a", 0)]
		self.assertEqual(validDFA(D), (False, 'q0', 'a'))

        
if __name__ == '__main__':
    unittest.main()