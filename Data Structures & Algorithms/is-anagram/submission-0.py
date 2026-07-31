class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = {}
        t_chars = {}
        for i in s:
            if i in s_chars:
                s_chars[i]+=1
            else:
                s_chars[i]=1
        for j in t:
            if j in t_chars:
                t_chars[j]+=1
            else:
                t_chars[j]=1
        return s_chars == t_chars