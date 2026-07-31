class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_to_strings = {}
        for i in strs:
            count = [0] * 26
            for j in i:
                count[ord(j)-ord('a')] += 1
            count = tuple(count)
            if count in count_to_strings:
                count_to_strings[count].append(i)
            else:
                count_to_strings[count] = [i]
        return list(count_to_strings.values())
        