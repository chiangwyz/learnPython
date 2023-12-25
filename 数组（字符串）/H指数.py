"""
非常巧妙的思路，直接对数组进行降序排序，排序后，遍历数组，若某个元素 值不大于前h，则遍历结束。
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_citation = sorted(citations, reverse=True)

        i = 0
        h = 0

        while i < len(citations) and sorted_citation[i] > h:
            h += 1
            i += 1

        return h

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_citations = sorted(citations, reverse=True)

        h = 0

        for element in sorted_citations:
            if element > h:
                h += 1
            else:
                break
        
        return h
