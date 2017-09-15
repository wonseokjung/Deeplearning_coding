import numpy as np
import sys
from gym.envs.toy_text import discrete

UP = 0

RIGHT = 1

DOWN = 2

LEFT = 3

class GridworldEnv(discrete.DescreteEnv):
    #up = 0, right = 1, down = 2, left = 3

    metadata = {'render.modes' : ['human', 'ansi']}


    def __init__(selfself, shape=[4,4]):
        if not isinstance(shape, (list, tuple)) or not len(shape) == 2:
            raise ValueError('shape arguement must be a list/tuple of length 2')


        self.shape = shape

        nS = np.prod(shape)  # numpy productiond

        nA = 4

        p = {}ta

        grid = np.arange(nS).reshape(shape)

        it = np.nditer(grid, flags = ['multi_index'])

        while not it.finished:

            s = it.iterindex

            y,x = it.multi_index

            P[s] = {a:  [] for a in range(nA)}








