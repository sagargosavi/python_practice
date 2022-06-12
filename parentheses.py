class Solution(object):
    def Isvalid1(self,s):
        stack = []
        match = {'{':'}','[':']','(':')'}

        i = 0
        while i<=len(s)-1: 
            
            if s[i] in match:
                stack.append(s[i])
            else:
                if not stack or match[stack.pop()] != s[i]:
                    return False
            i +=1

        return not stack

a = Solution()
print(a.Isvalid1('[()()]'))