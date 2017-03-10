import math
import time
import random
from turtle import *

class StopWatch:
    def __init__(self):
        self.start = time.time()
    def stop(self):
        return time.time() - self.start

class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{:2d}, {:2d}'.format(self.x, self.y)

class ClosestPair:
    def __init__(self):
        self.pair = []

    #randomly generate list of pairs
    def generate(self, n, w, h):
        for i in range(n):
            x = random.randrange(w)
            y = random.randrange(h)
            self.pair.append(Pair(x, y))

    #O(n^2)
    def findClosestPair(self):
        p1 = None
        p2 = None
        distance = None
        for i in range(len(self.pair)):
            for j in range(i + 1, len(self.pair)):
                tempDistance = self.__findDistance(self.pair[i], self.pair[j])
                if p1 == None:
                    p1 = self.pair[i]
                    p2 = self.pair[j]
                    distance = tempDistance
                elif tempDistance < distance:
                    p1 = self.pair[i]
                    p2 = self.pair[j]
                    distance = tempDistance
        return str(p1), str(p2), distance

    #O(nlg^2n)
    def findClosestPairbyDivideNConquer(self, pairList):
        if len(pairList) == 1:
            return [pairList[0], None, 1000000]
        if len(pairList) == 2:
            return [pairList[0], pairList[1], self.__findDistance(pairList[0], pairList[1])]
        left, right = self.divide(pairList)
        temp = min(self.findClosestPairbyDivideNConquer(left), self.findClosestPairbyDivideNConquer(right), key = self.__getKey)
        p1, p2, delta = self.conquer(left, right, temp[0], temp[1], temp[2])
        return str(p1), str(p2), delta
    
    def divide(self, pairList):
        left = pairList[:math.floor(len(pairList) / 2)]
        right = pairList[-math.ceil(len(pairList) / 2):]
        return left, right

    def conquer(self, left, right, p1, p2, delta):
        temp = self.sortByY(left + right)
        pairList = []
        half = (left[-1].x + right[-1].x) / 2
        for pair in temp:
            if pair.x >= left[-1].x - delta - 1 and pair.x <= right[-1].x + delta - 1:
                pairList.append(pair)
        for i in range(len(pairList)):
            for j in range(i + 1, min(len(pairList), i + 1 + int(delta))):
                tempDistance = self.__findDistance(pairList[i], pairList[j])
                if (tempDistance < delta):
                    p1 = pairList[i]
                    p2 = pairList[j]
                    delta = tempDistance
        return p1, p2, delta

    def __findDistance(self, p1, p2):
        return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

    def sortByX(self):
        self.pair = sorted(self.pair, key = self.__keyX)

    def sortByY(self, pair):
        return sorted(pair, key = self.__keyY)

    def __keyX(self, pair):
        return pair.x

    def __keyY(self, pair):
        return pair.y

    def __getKey(self, item):
        return item[2]

    def printPairList(self, pairList):
        for i in range(len(pairList)):
            print('{:2d}: {}'.format(i + 1, pairList[i]))
        print()

def main():
    for i in range(20):
        cp = ClosestPair()
        cp.generate(5000, 10000, 10000)
        w = StopWatch()
        cp.sortByX()
        c1 = cp.findClosestPairbyDivideNConquer(cp.pair)
        print(c1)
        print('nlg^2n', w.stop())
        w = StopWatch()
        c2 = cp.findClosestPair()
        print(c2)
        print('n^2', w.stop())
        print()

if __name__ == '__main__':
    main()
