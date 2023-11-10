"""
这个题目非常有意思，以下笔记一是为梳理思路，二来是为了记录一些细节。
通过滑动窗口来匹配p中字符与s中滑动窗口内的字符。
1. 引入Counter计数类，需要了解Counter类的基本用法
2.  p_counter == s_counter，Counter的判等是对比key与value，全部相等则表示相等
3. s_counter[s[i-p_length]] -= 1，是为了处理aab这样的情况，当滑动窗口左侧滑动时，a只需要减去一个1即可
"""
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        # 返回值
        result = list()

        p_length = len(p)
        window_length = 0

        p_counter = Counter(p)
        s_counter = Counter()

        for i in range(len(s)):
            s_counter[s[i]] += 1

            # 滑动窗口长度超过p长度
            if i >= p_length:
                if s_counter[s[i-p_length]] == 1:
                    del s_counter[s[i-p_length]]
                else:
                    s_counter[s[i-p_length]] -= 1

            # 返回去找到相同的起始索引
            if p_counter == s_counter:
                result.append(i - p_length + 1)
        
        return result
