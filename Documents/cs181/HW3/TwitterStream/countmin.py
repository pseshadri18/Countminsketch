import numpy as np
# 3rd party
import mmh3
import math

class CountMin(object):

    def __init__(self, epsilon, delta):
        self.depth = int(math.log(1.0/delta, 2))
        self.width = int(2.0/epsilon)
        self.cm = np.zeros((self.depth,self.width))

    def increment(self, key): # where key is a word, hashtag, phrase
        for i in range(self.depth):
            index = mmh3.hash(key, i) % self.width # apply hash function on key
            self.cm[i][index] += 1
        return self 

    def estimate(self, key):
        minEst = float("inf")
        for i in range(self.depth):
            index = mmh3.hash(key, i) % self.width 
            if (self.cm[i][index] < minEst):
                minEst = self.cm[i][index]
        return minEst

    def merge(self, cm2):
        self.cm = self.cm + cm2.cm
        return self
