# 91019

class Solution(object):
    def palindrome1(self,x):
        x = str(x)
        y = x[::-1]
        return True if x==y else False

    def palindrome2(self,x):
        x = str(x)
        end1 = x[-1]
        print(end1)
        start,end =0,len(x)-1
        while start<end:
            if x[start] != x[end]:
                return False
            start = start+1
            end = end-1
        return True


n = Solution()
print(n.palindrome2('aabbcabbaa123'))