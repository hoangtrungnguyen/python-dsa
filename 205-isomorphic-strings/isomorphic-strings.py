class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # map: char s -> char t
        charDict = dict()
        # map: char t -> char s
        reverseDict = dict()
        for i, key in enumerate(s):
            if key not in charDict:
                if t[i] in reverseDict:
                    return False
                charDict[key] = t[i]
                reverseDict[t[i]] = key
            elif charDict[key] != t[i]:
                return False
        return True