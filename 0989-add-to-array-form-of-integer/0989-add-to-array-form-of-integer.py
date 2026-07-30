class Solution(object):
    def addToArrayForm(self, num, k):
        num=int("".join(map(str,num)))
        result=num+k
        result=str(result)
        k=list(result)
        m=map(int,k)
        return m

        