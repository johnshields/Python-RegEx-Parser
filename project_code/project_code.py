# Regular expression matcher
# John Shields

# Shunting Yard Algorithm
def shunt(infix):

   # specials dictionary
   specials = {'*': 50, '.': 40, '|': 30}

   pofix = ""
   stack = ""

   for c in infix:
      if c == '(':
         stack = stack + c
      elif c == ')':
         while stack[-1] != '(':
            # puting statements together
            pofix, stack = pofix + stack [-1], stack[:-1]
         stack = stack[:-1]
      elif c in specials:
         # looks for c in specials dictionary, if not found, give value 0
         # looks for top of stack in specials dictionary,  if not found, give value 0
         # n/ compares 1 against the other
         while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
            pofix, stack = pofix + stack [-1], stack[:-1]
         stack = stack + c

      else:
         pofix = pofix + c

   while stack:
      # puting statements together
      pofix, stack = pofix + stack [-1], stack[:-1]
 
   return pofix

 # Thompson's Construction
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

# Return the set of states that can be reached from state following e arrows
def followes(state):
# create a new set, with state as its only member
    states = set()
    states.add(state)

# check if state has arrows labeeled e from it
    if state.label is None:
        # Check if edge1 is a state
        if state.edge1 is not None:
            # if theres an edge1, follow it
            states |= followes(state.edge1)
        # check if edge2 is a state
        if state.edge2 is not None:
            # if theres an edge2, follow it
            states |= followes(state.edge2)


    return states

# matching
def match(infix, string):
    # Shunt and compile  the regular expression
    postfix = shunt(infix)
    nfa = compiletom(postfix)

    # current set of states and the next set of the states
    current = set()
    upcomin = set()

    # add the initial state to the current set
    current |= followes(nfa.initial)

    # Loop through each character in the string
    for s in string:
        # Loop through the current set of states
        for c in current:
            # check of that state is labelled s
          if c.label == s:
            # Add edge1 state to the upcomin set
            upcomin |= followes(c.edge1)
            # set current to upcomin, and clear out next
        current = upcomin
        upcomin = set()

        # check if the accept state is in the set of current states
        return (nfa.accept in current)

# tests
infixes = ["a.b.c*, a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c"]
strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]

for i in infixes:
    for s in strings:
        print(match(i, s), i, s)
