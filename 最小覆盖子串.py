"""
这个问题可以用滑动窗口算法来解决。以下是解决这个问题的步骤：

1. 维护两个字典，一个用于记录字符串t中的字符及其出现的次数，一个用于记录当前窗口中字符的出现次数。
2. 维护一个滑动窗口，用两个指针left和right表示窗口的左右边界。初始时，两个指针都指向s的起始位置。
3. 扩大right指针，直到窗口包含了所有t中的字符。
4. 一旦窗口包含了所有t中的字符，就可以开始收缩left指针，直到窗口不再包含t的所有字符为止。在收缩的过程中，记录可能的最小覆盖子串。
5. 重复步骤3和步骤4，直到right到达字符串s的末尾。
"""
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        # 字典t_dict记录字符串t中的字符及其出现的次数
        t_dict = Counter(t)
        # 字典window_counts记录当前窗口中字符的出现次数
        window_counts = {}
        
        # required用于记录需要包含的字符种类数
        required = len(t_dict)
        # formed用于记录当前窗口已经包含的字符种类数
        formed = 0
        
        # ans用于记录结果，格式为(窗口长度, 左指针, 右指针)
        ans = tuple([float("inf"), None, None])
        
        # left和right初始化为0
        left, right = 0, 0
        
        # 开始扩大窗口
        while right < len(s):
            # 增加当前字符的计数
            character = s[right]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            # 如果当前字符的数量满足了t中的数量，formed增加
            if character in t_dict and window_counts[character] == t_dict[character]:
                formed += 1
                
            # 开始收缩窗口
            while left <= right and formed == required:
                character = s[left]
                
                # 更新答案
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                    
                # 减少窗口左侧字符的计数
                window_counts[character] -= 1
                if character in t_dict and window_counts[character] < t_dict[character]:
                    formed -= 1
                    
                # 移动左指针
                left += 1    
            
            # 移动右指针
            right += 1
            
    if ans[0] == float("inf"):
        return ""
    else:
        return s[ans[1]:ans[2] + 1]



