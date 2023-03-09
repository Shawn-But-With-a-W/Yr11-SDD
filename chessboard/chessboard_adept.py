'''Given the location of two knights, find the amount of moves required for each for the two to meet.'''

LETTER_TO_NUM = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}

class Knight:
    def __init__(self, x, y):
        self.x = x
        self.y = LETTER_TO_NUM[y]

    def move(self, x_change, y_change):
        '''Moves the knight by the given x and y values.'''
        self.x += x_change
        self.y += y_change

    def determine_heading(other_knight):
        '''
            Determines what direction the knight should be moved in.
            Possible values (1, 2), (-1, 2), (-1, -2), (1, -2), (2, 1), (-2, 1), (-2, -1), (2, -1)
        '''
        goal_x = other_knight.x
        goal_y = other_knight.y

        x_diff = other_knight.x - self.x
        y_diff = other_knight.y - self.y
        gradient = y_diff / x_diff

        # 3 moves for 2 spaces between
        # 2 moves for 1 space between
        # 3 moves for no space between


knight1 = Knight(2, 'H')