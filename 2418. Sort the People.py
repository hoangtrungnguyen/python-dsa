from typing import Optional
from typing import List

# https://leetcode.com/problems/sort-the-people/description/

class Solution:
    """
    map: int -> str
    sort height
    result = []
    for h in heights:
        result.insert(map[h])
    """
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_to_height = dict()
        for i in range(len(heights)):
            name_to_height.setdefault(heights[i], names[i])

        return []

    # def merge_sort(self, data: list[int]):
    #
    #     if data
