# AutomataChecker
AutomataChecker is, as the name suggest, a tool used to check automata. In particular, it can be used to check the correctness of a Deterministic Finite Automaton (DFA) against a set of input words or a regular expression. This tool was developed whilst attending the course Automata, Language Theory and Complexity at Eindhoven University of Technology, and is hence designed to be used in a learning environment.

# Definition of Automata
In this project, the definiton of a DFA as described by Michael Sipser in _Introduction to the Theory of Computation_ was followed. A finite automaton is a 5-tuple, (_Q_, _Σ_, _δ_, _q0_, _F_), where
* _Q_ is a finite set of states,
* _Σ_ is a finite set called the alphabet,
* _δ_ : _Q_ × _Σ_ → _Q_ is the transition function, 
* _q0_ ∈ _Q_ is the initial state, and
* _F_ ⊆ _Q_ is the set of final states.

# Installation
In order to run AutomataChecker, 4 modules must be installed. These modules are, `tkinter`, `regex`, `unittest` and `pyperclip`. All of these modules can be installed using pip. Afterwards, `main.py` can be run to launch AutomataChecker. 

# Usage
When AutomataChecker is running, the user will be greated by a UI containing three buttons, a text field and a blank canvas. In order to design the DFA, the user has the following options
* Define a state by pressing the right-mouse button. The first state defined will be the initial state of the DFA.
* Define a transition by pressing the left-mouse button on the state to be the origin of the transition, and pressing the left-mouse button on the state to be the destination of the transition. When both origin and destination have been chosen, the user is greeted by a pop-up window where he/she can enter the input on which the transition is taken.
* Define a final state by pressing both shift and the left-mouse button on the state to be a final state. 
<a /> 
<br >
When the DFA is designed, the user has two options. The DFA can be checked against a set of input words, or against a regular expression. If a single input is given, AutomataChecker will assume this is a regular expression and will generate a set of input words from said RegEx, which will be used to check the correctness of the DFA. If a set of input words are given by the user, AutomataChecker will instead use these to determine the correctness of the DFA.
