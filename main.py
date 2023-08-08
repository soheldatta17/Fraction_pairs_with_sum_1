from collections import defaultdict
from math import gcd
class Solution:
    def countFractions(self, n, numerator, denominator):
        # Your code here
        d=defaultdict(int)
        ans=0
        for i in range(n):
            x=numerator[i]
            y=denominator[i]
            g=gcd(x,y)
            x=int(x/g)
            y=int(y/g)
            a=y-x
            b=y
            if (a,b) in d:
                ans+=d[(a,b)]
            d[(x,y)]+=1
        return ans