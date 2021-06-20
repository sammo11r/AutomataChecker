# AutomataChecker
AutomataChecker is, as the name suggest, a tool used to check automata. In particular, it can be used to check the correctness of a Deterministic Finite Automaton (DFA) against a set of input words. This tool was developed whilst following the course Automata, Language Theory and Complexity at Eindhoven University of Technology, and is hence designed to be used in a learning environment.

# Definition of Automata
In this project, the definiton of a DFA as proposed by Michael Sipser in _Introduction to the Theory of Computation_ was followed. A deterministic finite automaton _M_ is a 5-tuple, (_Q_, _Σ_, _δ_, _q0_, _F_), consisting of 
* a finite set of states _Q_,
* a finite set of input symbols called the alphabet _Σ_,
* a transition function _δ_ : _Q_ × _Σ_ → _Q_
* an initial or start state _q0 ∈ _Q_
* a set of accept states _F_ ⊆ _Q_

# Installation
