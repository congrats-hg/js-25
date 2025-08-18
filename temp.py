class Solution:
    def firstUniqChar(self, s: str) -> int:
        answer = -1
        set_alphabet = set()
        for i in range(len(s)):
            if s[i] not in s[i+1:] and s[i] not in set_alphabet:
                return i
            else:
                set_alphabet.add(s[i])
        return answer

c = Solution()
print(c.firstUniqChar("aabb"))