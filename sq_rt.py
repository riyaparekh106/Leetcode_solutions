class Solution(object):
    def mySqrt(self, x):
        y = 1
        while True:
            if x < y*y:
                return y-1
            else:
                y +=1
