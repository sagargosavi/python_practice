# Return indices of two numbers

from colorsys import TWO_THIRD


class Solution(object):
    def twosum(self,l,n):
        mydict = {}
        for i,v in enumerate(l):
            if n-v in mydict:
                return [mydict[n-v],i]

            mydict[v] = i

        return []

l = [10,20,10,40,50,60,70,80,90]
n = 50
x = Solution()
a = x.twosum(l,n)
print(a)