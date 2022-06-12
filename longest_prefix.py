# strs = ["flower","flow","flight"]
# Output: "fl"

# Input: strs = ["dog","racecar","car"]
# Output: ""

class Solution(object):
    def prefix(self,strs):
        if not strs:
            return ''
        strs.sort()
        start,end = strs[0],strs[-1]
        i = 0
        while i<len(start) and i<len(end) and start[i] == end[i]:
            i +=1
        return start[:i]


a = Solution()
op = a.prefix(["flower","fliw","floight"])
print(op)