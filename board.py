#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: 
# email:
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                self.tiles[r][c] = digitstr[3*r + c]
                if digitstr[3*r + c] == '0':
                    self.blank_r = r
                    self.blank_c = c
        
    ### Add your other method definitions below. ###
    def __repr__(self):
        ''' returns string representation of Board object
        '''
        s = ''
        for row in range(len(self.tiles)):
            for col in range(len(self.tiles[0])):
                if self.tiles[row][col] == '0':
                    s  += '_ '
                else:
                    s += self.tiles[row][col] + ' '                   
            s += '\n'
        return s
    
    def move_blank(self, direction):
        ''' takes input string direction and attempts to modify
            the Board object to move the blank accordingly. If 
            direction not possible, return False, return True otherwise.
        '''
        r = self.blank_r
        c = self.blank_c
        if direction not in 'updownrightleft':
            return False
        elif direction == 'up':
            r = self.blank_r - 1
        elif direction == 'down':
            r = self.blank_r + 1
        elif direction == 'left':
            c = self.blank_c - 1
        elif direction == 'right':
            c = self.blank_c + 1
        if r in range(len(self.tiles)) and c in range(len(self.tiles[0])):
            oldblankr = self.blank_r
            oldblankc = self.blank_c
            self.tiles[oldblankr][oldblankc] = self.tiles[r][c]
            self.tiles[r][c]= '0'
            self.blank_c = c
            self.blank_r = r
            return True
        else:
            return False
        
    def digit_string(self):
        ''' creates and returns a string of digits that corresponds
            to the current contents of the Board's tiles
        '''
        s = ''
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles)):
                s += self.tiles[x][y]
        return s
    
    def copy(self):
        ''' create deep copy of called object
        '''
        return Board(self.digit_string())
    
    def num_misplaced(self):
        ''' counts and returns number of tiles in called
            object that are not where they should be in the goal state
        '''
        count = 0
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[0])):
                if self.tiles[x][y] == '0':
                    count = count
                else:
                    if self.tiles[x][y] != GOAL_TILES[x][y]:
                        count += 1
                    else:
                        count = count
        return count
        
    def __eq__(self, other):
        ''' return True if called object and argument have the same
            values for the tiels attribute, False otherwise
        '''
        if self.tiles == other.tiles:
            return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

