class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence_to_set = set(list(sentence))
        if len(sentence_to_set) == 26:
            return True
        else:
            return False

instance = Solution()
print(instance.checkIfPangram("leetcode"))
print(instance.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))