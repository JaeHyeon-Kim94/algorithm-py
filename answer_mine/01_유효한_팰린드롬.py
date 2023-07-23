# 주어진 문자열이 팰린드롬인지 확인하라.
#  팰린드롬은 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어, 문장을 말함.


# 조건 1. 대소문자 구분하지 않는다.
# 조건 2. 영문자, 숫자만을 대상으로 한다.

class Solution(object):
    # 리스트로 변환
    def is_valid_palindrome1(self, s:str) -> bool:
        target_s = [chr.lower() for chr in s if chr.isalnum()]


        # idx 이용
        # target_s_last_idx = len(target_s) - 1
        # for i in range(target_s_last_idx):
        #     if target_s[i] != target_s[target_s_last_idx - i]:
        #         return False

        # pop()
        while len(target_s) > 1:
            if target_s.pop(0) != target_s.pop():
                return False
        return True

    # deque 이용
    def is_valid_palindrome2(self, s:str) -> bool:
        import collections
        from typing import Deque

        target_s: Deque = collections.deque()

        [target_s.append(chr) for chr in s if chr.isalnum()]

        # 첫 번째 함수에서 target_s.pop(0)은 시간복잡도가 O(n)이나,
        #  deque의 popleft는 시간복잡도 O(1)
        while len(target_s) > 1:
            if target_s.popleft() != target_s.pop():
                return False

        return True

    # 슬라이싱 사용
    def is_valid_palindrome3(self, s:str) -> bool:
        import re
        # 알파벳 혹은 숫자가 아닌 것들은 replace
        s = re.sub('[^a-zA-Z0-9]', '', s)
        s = s.lower()

        return s == s[::-1]






