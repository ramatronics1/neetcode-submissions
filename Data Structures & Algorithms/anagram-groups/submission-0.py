from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_arr =   defaultdict(list)
        res = []

        for i in strs:
            sort_str = tuple(sorted(i))
            ana_arr[sort_str].append(i)
        for value in ana_arr.values():
            res.append(value)
        return res   

        