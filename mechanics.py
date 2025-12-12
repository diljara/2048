# in this file will be the basic logic of the game
# creating board and basic moves of the game as well as a random number appearing after each move

import numpy as np

class Game:
    def __init__(self, size, board=None):

        """
        initialize a 2d array of (size, size) shape with N "2"s in random places, other elements are 0
        where N = size // 2

        Args:
            size (int): The length and width of the square field.
            board (np.array or None): the game field.

        Returns:
        """

        if not isinstance(size, int) or size < 2 or size >= 20:
            raise ValueError('invalid board size')
        self.size = size
        if board is None:
            array = np.zeros((self.size, self.size), dtype=int)
            indices = np.random.choice(self.size*self.size, size=(self.size//2), replace=False)
            rows, cols = indices // self.size, indices % self.size
            array[rows, cols] = [2] * (self.size//2)
            self._board = array
        else:
            self._board = board
        self._score = 0
        self.over = False

    @property
    def board(self):
        return self._board

    # Getter for score
    @property
    def score(self):
        return self._score

    def add_score(self, points):
        """
        Internal method to update score
        """
        self._score += points

    def add_number(self):
        """
        add one "2" in random place on the board instead of "0"
        """

        if 0 not in self.board:
            self.over = True
            return self.board

        not_zero = True
        while not_zero:
            # assuming array is square
            random_index = tuple(np.random.randint(self.size, size=(2, 1)))
            if self.board[random_index] == 0:
                not_zero = False
        self.board[random_index] = 2
        return self.board

    def right(self, transpose=False):

        """
        swipes every number to the right
        if the same numbers colide, adds them up
        """

        delta_score = 0
        if transpose:
            self._board = self.board.T
        for row in self._board:
            # check if there are nonzero numbers in the row

            if np.count_nonzero(row):
                # let's try to do the sorting with 2 pointers
                vacant = len(row) - 1
                ex_vacant = len(row) - 1 # last filled position
                for i in range(len(row)-1, -1, -1):
                    if row[i] != 0:

                        # added them up if equal numbers
                        if (i != len(row) - 1) and (row[ex_vacant] == row[i]):

                            row[ex_vacant] += row[i]
                            delta_score += 2 * row[i]

                        # moved to a vacant position if not equal
                        else:

                            row[vacant] = row[i]
                            ex_vacant = vacant
                            vacant = vacant - 1
                row[0:(vacant+1)] = np.zeros(vacant + 1, dtype=int)

        self.add_score(delta_score)

        if transpose:
            self._board = self.board.T

        return

    def down(self):

        """
        swipe every number down
        and add them up if equal
        """

        self.right(transpose=True)
        return

    def left(self, transpose=False):

        """
        swipes every number to the left
        if the same numbers colide, adds them up
        """

        delta_score = 0
        if transpose:
            self._board = self.board.T
        for row in self._board:
            # check if there are nonzero numbers in the row

            if np.count_nonzero(row):
                # let's try to do the sorting with 2 pointers
                vacant = 0
                ex_vacant = 0 # last filled position
                for i in range(0, len(row)):
                    if row[i] != 0:

                        # added them up if equal numbers
                        if (i != 0) and (row[ex_vacant] == row[i]):

                            row[ex_vacant] += row[i]
                            delta_score += 2 * row[i]

                        # moved to a vacant position if not equal
                        else:

                            row[vacant] = row[i]
                            ex_vacant = vacant
                            vacant = vacant + 1
                row[vacant:] = np.zeros(len(row) - vacant , dtype=int)
        self.add_score(delta_score)

        if transpose:
            self._board = self.board.T

        return

    def up(self):

        """
        swipe every number up
        and add them up if equal
        """

        self.left(transpose=True)
        return
