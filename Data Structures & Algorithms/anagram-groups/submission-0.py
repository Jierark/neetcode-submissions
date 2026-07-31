class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A = {} # anagram -> string
        for i in strs:
            j = str(sorted(i))
            print(j)
            if j in A.keys():
                A[j].append(i)
            else:
                A[j] = [i]
        return list(A.values())