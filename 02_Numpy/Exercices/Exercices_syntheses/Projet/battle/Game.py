import numpy as np
import os 
import random
from Card import Card

class Game:

    def __init__(self, fileName):
        self.turns = 0
        self.data = launchCards(fileName).reshape(52, )
        self.package = []
        self.player1 = []
        self.player2 = []
        self.player = True
        self.scores = {'player1' : 0, 'player2' : 0}

        for data in self.data:
            self.package.append( Card( data ) )

        random.shuffle(self.package)
            
        # distribution
        for i in range(26):
            self.player1.append( self.package[i] )
            self.player2.append( self.package[i+1] )

    def run(self):
        
        while  not ( not self.player1 or not self.player2 )  :
            if self.player1[0].value > self.player2[0].value:
                self.player1.append(self.player2[0])
                del self.player1[0]
            elif self.player1[0].value == self.player2[0].value:
                del self.player1[0]
                del self.player2[0]
            else:
                self.player2.append(self.player1[0])
                del self.player2[0]

            self.turns += 1

def launchCards(fileName):
    directory = os.path.dirname(__file__) # we get the right path.
    path_to_file = os.path.join(directory, "data", fileName) # with this path, we go inside the folder `data` and get the file.
    cards = None
    with open(path_to_file,"r") as f:
        cards = np.loadtxt(f, dtype = np.dtype('U3'))

    return cards
