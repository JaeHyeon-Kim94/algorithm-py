# 가장 흔하게 등장하는 단어를 출력.
# 조건 1. 금지된 단어 제외
#     2. 대소문자 구분X
#     3. 구두점 무시
import collections
import re

class Solution:
    def most_common_word(self, paragraph: str, banned: list[str]) -> str:
        cond3_str = re.sub(r'[^\w\s]', ' ', paragraph)
        cond2_list = cond3_str.lower().split()
        cond1_list = [word for word in cond2_list if word not in banned]

        cond1_dict = collections.Counter(cond1_list)

        return cond1_dict.most_common(1)[0][0]



