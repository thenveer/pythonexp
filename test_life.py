from game_of_life import display

def test_neighbour():

    grid = [[False, False, False],
            [False, False, False],
            [False, False, False]]


    assert display(grid) == [[0, 0, 0],
                                           [0, 0, 0],
                                           [0, 0, 0]]


