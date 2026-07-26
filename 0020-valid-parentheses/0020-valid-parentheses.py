class Solution(object):
    def isValid(self, s):
        stack=[]
        d={'(':')', '{':'}', '[':']'}
        for char in s:
            if char in d:
                stack.append(d[char])
            else:
                if not stack or stack.pop()!=char:
                    return False
        return not stack
        