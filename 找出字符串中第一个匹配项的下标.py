"""
要解决这个问题，我们可以使用KMP（Knuth-Morris-Pratt）算法。
KMP算法是一种用于字符串搜索的有效算法，其核心思想是当在主字符串haystack中发现不匹配时，通过部分匹配表（也称为前缀函数或失败函数）跳过尽可能多的不必要的比较。

KMP算法分为两个主要步骤：

构建部分匹配表：这个表存储了在模式字符串needle中，每个子串的前缀和后缀的最长公共元素长度。这个表用于决定在发生不匹配时，模式字符串应该向右移动多远。
字符串搜索：使用部分匹配表，我们可以在主字符串中高效地搜索模式字符串。
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 如果needle为空字符串，则返回0
        if not needle:
            return 0

        # 构建部分匹配表
        def build_lps(needle):
            lps = [0] * len(needle)  # 初始化部分匹配表
            length = 0  # length用于追踪前缀的长度
            i = 1
            while i < len(needle):
                if needle[i] == needle[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        # 实现KMP算法
        def KMP_search(haystack, needle):
            lps = build_lps(needle)
            i = j = 0  # i是haystack的索引，j是needle的索引

            while i < len(haystack):
                if needle[j] == haystack[i]:
                    i += 1
                    j += 1
                if j == len(needle):
                    return i - j  # 找到匹配项
                elif i < len(haystack) and needle[j] != haystack[i]:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return -1  # 未找到匹配项

        return KMP_search(haystack, needle)

