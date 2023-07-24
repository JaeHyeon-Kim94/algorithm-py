# 문자열을 받아 애너그램 단위로 그루핑
import collections


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        str_dict = collections.defaultdict(list)
        for st in strs:
            str_dict[''.join(sorted(st))].append(st)

        return list(str_dict.values())


