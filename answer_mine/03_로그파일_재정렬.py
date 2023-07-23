# 로그파일을 재정렬한다.

# 조건 1. 로그의 가장 앞 부분은 식별자
#     2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
#     3. 식별자는 순서에 영향을 끼치지 않지만 문자가 동일할 경우 식별자 순으로 한다.
#     4. 숫자 로그는 입력 순서대로 한다.

class Solution(object):
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        digits = []
        letters = []

        for log in logs:
            arr = log.split(' ')

            if arr[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

            letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits