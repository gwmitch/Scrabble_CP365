import os
import string
import numpy as np
import random
import time
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2
import twl
from ScrabbleBoard import *
from scrabble_globals import *


class Visualizer:
    
    # Re-read the current game state image every 50ms to refresh the view
    # This should make the visualization behavior a bit nicer
    def runVisualizer(self):
        while True:
            try:
                self.board_im = cv2.imread(BOARD_STATE_IMAGE)
                cv2.imshow('image', self.board_im)
                cv2.waitKey(50) # Don't close the window
            except cv2.error as e:
                # Board image file wasn't ready...
                pass
