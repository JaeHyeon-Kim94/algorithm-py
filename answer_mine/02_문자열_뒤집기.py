# 문자열 뒤집기
# 입력값인 문자 배열을 뒤집는다.

# 조건1. 리턴 없이 문자열 리스트 자체를 조작할 것.

class Solution(object):

    #  전통적인 투포인터 스왑방식
    def reverse_string1(self, s: list[str]) -> None:
        last_idx = len(s) - 1

        for i in range(last_idx // 2):
            tmp = s[i]
            s[i] = s[last_idx - i]
            s[last_idx - i] = tmp

    # 파이썬 다운 방식..
    def reverse_string2(self, s: list[str]) -> None:
        s.reverse()
