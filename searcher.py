#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    def __init__(self, depth_limit):
        self.depth_limit = depth_limit
        self.states = []
        self.num_tested = 0
        
    def add_state(self, new_state):
        ''' takes single State object called new_state and adds it 
            to the Searcher's list of untested states.
        '''
        self.states += [new_state]

    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s

    def should_add(self, state):
        ''' takes a State object called state and returns True
            if called Searcher should add state to its list
            of untested states, False otherwise.
        '''
        if state.num_moves > self.depth_limit and self.depth_limit != -1:
            return False
        elif state.creates_cycle():
            return False
        return True

    def add_states(self, new_states):
        ''' takes a list of State objects called new_states
            and process the elements of new_states one at a time
            to be added to the Searcher's list of states
        '''
        for x in new_states:
            if self.should_add(x):
                self.add_state(x)
    
    def next_state(self):
        """ chooses the next state to be tested from the list of 
            untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    def find_solution(self, init_state):
        ''' performs a full state-space search that begins at specified
            initial state and ends when goal state is found or when
            the Searcher runs our of untested states.
        '''
        self.add_state(init_state)
        while self.states != []:
            s = self.next_state()
            self.num_tested += 1
            if s.is_goal():
                return s
            else:
                self.add_states(s.generate_successors())
        return None
            
### Add your BFSeacher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
    ''' A class for objects that perform breadth-first search
    '''
    def next_state(self):
        ''' Chooses next state based on FIFO ordering - choosing
            the state that has been in the list the longest.
        '''
        s = self.states[0]
        self.states.remove(s)
        return s
        
class DFSearcher(Searcher):
    ''' A searcher object that perform depth-first search - 
        choosing untested state that has the largest depth
    '''
    def next_state(self):
        ''' Chooses next state based on LIFO ordering - choosing
            the state that has been in the list the longest.
        '''
        s = self.states[-1]
        self.states.remove(s)
        return s


def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###
def h1(state):
    ''' returns estimate of how many additional moves
        are needed to get from state to goal state
    '''
    return state.board.num_misplaced()
            
def h2(state):
    ''' sum of the distance of each tile from their goal state
    '''
    d = 0
    for r in range(3):
        for c in range(3):
                if state.board.tiles[r][c] == '1':
                    d += abs(r)
                    d += abs(c-1)
                elif state.board.tiles[r][c] == '2':
                    d += abs(r)
                    d += abs(c-2)
                elif state.board.tiles[r][c] == '3':
                    d += abs(r-1)
                    d += abs(c)
                elif state.board.tiles[r][c] == '4':
                    d += abs(r-1)
                    d += abs(c-1)
                elif state.board.tiles[r][c] == '5':
                    d += abs(r - 1)
                    d += abs(c - 2)
                elif state.board.tiles[r][c] == '6':
                    d += abs(r - 2)
                    d += abs(c) 
                elif state.board.tiles[r][c] == '7':
                    d += abs(r - 2)
                    d += abs(c - 1)
                elif state.board.tiles[r][c] == '8':
                    d += abs(r - 2)
                    d += abs(c - 2)
    return d
                    

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    def __init__(self, heuristic):
        ''' Constructor for new GreedySearcher objetc
        '''
        super().__init__(-1)
        self.heuristic = heuristic
        
    def priority(self, state):
        """ computes and returns the priority of the specified state,
            based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
    
    def add_state(self, state):
        ''' add a sublist that is [priority, state] pair
        '''
        self.states += [[self.priority(state), state]]
    
    def next_state(self):
        ''' choose one of the states with the highest priority
        '''
        s = max(self.states)
        self.states.remove(s)
        return s[1]
        
        
    
    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s


### Add your AStarSeacher class definition below. ###

class AStarSearcher(GreedySearcher):
    ''' class for objects that perform A* search
    '''
    def __init__(self, heuristic):
        ''' Constructor for new GreedySearcher objetc
        '''
        super().__init__(-1)
        self.heuristic = heuristic
    
    def priority(self, state):
        ''' assigns priority to state while taking into account 
            the cost that has been expended to get to that state
        '''
        return -1 * (self.heuristic(state) + state.num_moves)

        
        
        
        
        
        
        
        
        
        
        
    