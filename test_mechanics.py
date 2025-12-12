# here will be testing of the mechanics.py

import pytest
import numpy as np

from mechanics import Game


def test_init_game():
    with pytest.raises(ValueError):
        Game("cat")
    with pytest.raises(ValueError):
        Game(1)
    with pytest.raises(ValueError):
        Game(2.9)
    with pytest.raises(ValueError):
        Game(20)
    for test_size in [2, 4, 7]:
        test_game = Game(test_size)
        assert test_game.board.shape == (test_size, test_size)
        assert np.count_nonzero((test_game.board - 2) == 0) == test_size // 2


def test_add_number():
    for test_size in [2, 4, 7]:
        test_game = Game(test_size)
        test_game.add_number()
        assert test_game.board.shape == (test_size, test_size)
        test_game.add_number()
        assert np.count_nonzero((test_game.board - 2) == 0) == test_size // 2 + 2


def test_left():

    # testing 4 x 4 board
    test_game_4 = Game(size=4, board=[[0, 2, 0, 2], [0, 0, 0, 0], [0, 0, 0, 2], [0, 0, 2, 2]])
    test_game_4.left()
    assert test_game_4.board == [[4, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0], [4, 0, 0, 0]]

    # testing 6 x 6 board
    test_game_6 = Game(size=6, board=[[0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 2, 0], [2, 0, 0, 0, 0, 0],
                        [2, 0, 0, 0, 0, 0], [0, 0, 2, 2, 0, 0], [0, 0, 2, 0, 2, 0]])
    test_game_6.left()
    assert test_game_6.board == [[2, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0], [
        2, 0, 0, 0, 0, 0], [4, 0, 0, 0, 0, 0], [4, 0, 0, 0, 0, 0]]


def test_right():
    board_4 = [[2, 2, 2, 0],
               [0, 0, 0, 0],
               [2, 0, 0, 2],
               [2, 0, 0, 2]]
    test_game_4 = Game(size=4, board=board_4)
    test_game_4.right()
    assert test_game_4.board == [[0, 0, 2, 4],
                              [0, 0, 0, 0],
                              [0, 0, 0, 4],
                              [0, 0, 0, 4]]
    board_6 = [[0, 0, 0, 0, 0, 2],
               [0, 2, 0, 0, 0, 2],
               [0, 0, 0, 0, 2, 0],
               [2, 0, 2, 0, 0, 0],
               [0, 0, 2, 0, 0, 2],
               [0, 0, 0, 0, 0, 0]]
    test_game_6 = Game(size=6, board=board_6)
    test_game_6.right()
    assert test_game_6.board == [[0, 0, 0, 0, 0, 2],
                              [0, 0, 0, 0, 0, 4],
                              [0, 0, 0, 0, 0, 2],
                              [0, 0, 0, 0, 0, 4],
                              [0, 0, 0, 0, 0, 4],
                              [0, 0, 0, 0, 0, 0]]


def test_up():
    expected = np.array([[4, 4, 4],
                        [2, 0, 0],
                        [0, 0, 0]])
    test_game_3 = Game(size=3, board=np.array([[2, 0, 0], [2, 2, 2], [2, 2, 2]]))
    test_game_3.up()
    result = test_game_3.board
    assert np.array_equal(result, expected)


def test_down():
    test_game_3 = Game(size=3, board=np.array([[0, 2, 2], [2, 0, 2], [2, 0, 2]]))
    test_game_3.down()
    result = test_game_3.board
    expected = np.array([[0, 0, 0], [0, 0, 2], [4, 2, 4]])
    assert np.array_equal(result, expected)
