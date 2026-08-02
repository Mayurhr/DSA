class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(pattern) != len(words):
            return False
        patternMap = {}
        wordMap = {}
        for p, w in zip(pattern, words):
            if p in patternMap:
                if patternMap[p] != w:
                    return False
            else:
                patternMap[p] = w
            if w in wordMap:
                if wordMap[w] != p:
                    return False
            else:
                wordMap[w] = p
        return True