class Solution:
    def isPalindrome(self, s: str) -> bool:
        A = "".join(char for char in s if char.isalnum()).lower()
        print(A)
        i, j = 0, len(A)-1
        while i < len(A)/2:
            if A[i] != A[j]:
                print(A[i], A[j])
                return False
            i += 1
            j -= 1
        return True