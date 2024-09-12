class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        string_set = set(allowed)  
        sum = 0

        for word in words:
            if all(char in string_set for char in word):
                sum += 1

        return sum