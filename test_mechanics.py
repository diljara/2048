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

def test_board_property_returns_array():
    game = Game(size=3)
    assert isinstance(game.board, np.ndarray)
    assert game.board.dtype == int

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

def test_score_property_is_readonly_safe():
    game = Game(size=3)
    initial_score = game.score

    with pytest.raises(AttributeError):
        game.score = 100

    game.add_score(50)
    assert game.score == initial_score + 50

def test_initial_score_is_zero():
    game = Game(size=4)
    assert game.score == 0

def test_score_after_single_merge_left():

    game = Game(size=3, board=np.array([[2, 2, 0], [0, 0, 0], [0, 0, 0]]))
    game.left()
    assert game.score == 4

def test_score_multiple_merges_same_row():
    # [2, 2, 4, 4] -> [4, 8] -> +4 +8 = +12
    game = Game(size=4, board=np.array([[2, 2, 4, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))
    game.left()
    assert game.score == 12

def test_score_multiple_rows():
    game = Game(size=3, board=np.array([[2, 2, 0], [4, 4, 0], [0, 0, 0]]))
    game.left()
    assert game.score == 12

def test_score_accumulates():
    game = Game(size=3, board=np.array([[2, 2, 0], [0, 0, 0], [0, 0, 0]]))
    game.left()  # +4
    assert game.score == 4

    game._board = np.array([[4, 4, 0], [0, 0, 0], [0, 0, 0]])
    game.left()  # +8
    assert game.score == 12

    game._board = np.array([[8, 8, 0], [0, 0, 0], [0, 0, 0]])
    game.left()  # +16
    assert game.score == 28

def test_no_score_without_merge():
    game = Game(size=3, board=np.array([[2, 0, 0], [4, 0, 0], [8, 0, 0]]))
    game.left()
    assert game.score == 0

def test_game_not_over_initially():
    game = Game(size=4)
    assert game.over is False

def test_game_not_over_with_empty_spaces():
    game = Game(size=3, board=np.array([[2, 4, 0], [8, 16, 0], [32, 64, 0]]))
    assert game.over is False

def test_game_over_when_board_full():

    full_board = np.array([[2, 4, 8], [16, 32, 64], [128, 256, 512]])
    game = Game(size=3, board=full_board)

    result = game.add_number()
    assert game.over is True
    assert np.array_equal(result, full_board)

def test_game_over_state_persists():
    full_board = np.array([[2, 4], [8, 16]])
    game = Game(size=2, board=full_board)

    game.add_number()
    assert game.over is True

    game.add_number()
    assert game.over is True

def test_four_tiles_double_merge():
    # [2, 2, 2, 2] -> [4, 4, 0, 0]
    game = Game(size=4, board=np.array([[2, 2, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))
    game.left()
    expected = np.array([[4, 4, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    assert np.array_equal(game.board, expected)
