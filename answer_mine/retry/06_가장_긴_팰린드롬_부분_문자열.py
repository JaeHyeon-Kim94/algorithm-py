# 가장 긴 팰린드롬 문자열을 출력

class Solution:
    def longestPalindrome(self, s: str) -> str:

        l = 0
        gap = 1
        reslt = ''

        while gap < len(s):
            while (l + gap) < len(s):
                if self.is_palindrome(s[l:(l + gap)]):
                    reslt = s[l:(l + gap)]
                l += 1
            l = 0
            gap += 1

        print(reslt)

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]
