'''Given the location of two knights, find the amount of moves required for each for the two to meet.'''

LETTER_TO_NUM = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}

class Knight:
    def __init__(self, x, y):
        self.x = LETTER_TO_NUM[x]
        self.y = y
        self.moves = 0

    def count_moves(self, num_moves=1):
        '''Adds num_moves (defaults to 1) to the amount of self.moves'''
        self.moves += num_moves

    def move(self, heading: tuple):
        '''Moves the knight by the given x and y values.'''
        self.x += heading[0]
        self.y += heading[1]
        self.count_moves()

    def determine_heading(self, other_knight):
        '''
            Determines what direction the knight should be moved in, or returns amount of moves to take if certain cases hold true.
            Possible values: (1, 2), (-1, 2), (-1, -2), (1, -2), (2, 1), (-2, 1), (-2, -1), (2, -1), (3,3), (2, 2), None
        '''
        goal_x = other_knight.x
        goal_y = other_knight.y

        x_diff = other_knight.x - self.x
        y_diff = other_knight.y - self.y

        # Check special cases
        # 2 spaces in between
        if (abs(x_diff) == 3 and y_diff == 0) or (x_diff == 0 and abs(y_diff) == 3):
            self.count_moves(2)
            other_knight.count_moves(1)
            return None
        # 1 space in between
        elif (abs(x_diff) == 2 and y_diff == 0) or (x_diff == 0 and abs(y_diff) == 2):
            self.count_moves(1)
            other_knight.count_moves(1)
            return None
        # No space in between
        elif (abs(x_diff) == 1 and y_diff == 0) or (x_diff == 0 and abs(y_diff) == 1):
            self.count_moves(2)
            other_knight.count_moves(1)
            return None
        elif abs(x_diff) == 1 and abs(y_diff) == 1:
            self.count_moves(1)
            other_knight.count_moves(1)
            return None

        else:
            # Determine angle
            if abs(x_diff) >= abs(y_diff):
                x_heading = 2
                y_heading = 1
            elif abs(x_diff) < abs(y_diff):
                x_heading = 1
                y_heading = 2

            # Determine general direction (+-x, +-y)
            if x_diff < 0:
                x_heading *= -1
            if y_diff < 0:
                y_heading *= -1

            return x_heading, y_heading



x, y = input('Knight 1 location: (put space in between x and y coord) ').split()
knight1 = Knight(x.upper(), int(y))
x, y = input('Knight 2 location: (put space in between x and y coord) ').split()
knight2 = Knight(x.upper(), int(y))

while True:
    knight1_heading = knight1.determine_heading(knight2)
    if knight1_heading:
        knight1.move(knight1_heading)
    else:
        break

    knight2_heading = knight2.determine_heading(knight1)
    if knight2_heading:
        knight2.move(knight2_heading)
    else:
        break

print(f'It takes {knight1.moves} moves for knight 1')
print(f'It takes {knight2.moves} moves for knight 2')