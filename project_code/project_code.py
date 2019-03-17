# Thompson's Construction in Python

 # represents a state with two arrows, labelled by label
 # use 'None' for a label representing 'e' arrows
class state:
    label = None
    edge1 = None
    edge2 = None

# an NFA is represented by its initial and accepts states
class nfa:    
    initial = None
    accept = None

    # manatory to have 'self' args in constructor
    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept

# Algorithm
# function has a stack of NFAs
# pofix allows to loop one character at a time 
# until the regular expression is complete
def compiletom(pofix):
    nfastack = []
 
    for c in pofix:
        if c == '.':
        # stack works as last in first out
        # method to go to stack 
         # pop 2 NFAs off the stack.
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            # merges them together
            # connect 1st NFAs accept state to the 2nd's initial
            nfa1.accept.edge1 = nfa2.initial
            
            # push NFA to stack
            # one way to do it ¬ nfastack.append(nfa(initial, accept))
            # second way 'easier way'
            newnfa = nfa(nfa1.initial, nfa2.accept)
            # pushes newnfa 
            nfastack.append(newnfa)

        elif c == '|':
            # pop 2 NFAs off the stack.
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            # create a new initial state, connect it to 
            # initial states of the two NFAs popped from the stack
            initial = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial
            # create new accept state, connecting the accept states 
            # of the the 2 NFAs popped from the stack, to the new state
            accept = state()
            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept

            # push NFA to stack
            # one way to do it ¬ nfastack.append(nfa(initial, accept))
            # second way 'easier way'
            newnfa = nfa(initial, accept)
            # pushes newnfa 
            nfastack.append(newnfa)

        elif c == '*':
            # pop a single NFA from the stack
            nfa1 = nfastack.pop()
            # create a new initial and accept states
            initial = state()
            accept = state()
            # join the new initial stse to nfa1's initial state and the new accept state.
            initial.edge1 = nfa1.initial
            initial.edge2 = accept
            # join the old accept state to the new accept state and nfa1's initial state.
            nfa1.accept.edge1 =  nfa.initial
            nfa1.accept.edge2 = accept

            # push new NFA to the stack
            # one way to do it ¬ nfastack.append(nfa(initial, accept))
            # second way 'easier way'
            newnfa = nfa(initial, accept)
            # pushes newnfa 
            nfastack.append(newnfa)

        else:
            # create new initial and accept states
            # creates new nfa
            accept = state()
            # creates new nfa
            initial = state()
            # string character
            # join the initial statesvto the accept state
            # using an arrow labelled c.
            initial.label = c
            initial.edge1 = accept
            # going to create a new instance of the NFA class. 
            # set its initial state to the 
            # initial state here that I've just created   

            # push new NFA to the stack # ¬ returns an instance of the nfa class ¬
            # one way to do it ¬ nfastack.append(nfa(initial, accept))
            # second way 'easier way'
            newnfa = nfa(initial, accept)
            # pushes newnfa 
            nfastack.append(newnfa)

    # nfastack  should onlt have a single nfa on it at the point.      
    return nfastack.pop()

infixes = ["a.b.c*, a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c"]
strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]

print(compiletom("ab.cd.|"))
print(compiletom("aa.*"))
print(compiletom("(0|(1(01*(00)*0)*1)*)*"))