"""
要解决这个问题，我们可以使用KMP（Knuth-Morris-Pratt）算法。
KMP算法是一种用于字符串搜索的有效算法，其核心思想是当在主字符串haystack中发现不匹配时，
通过部分匹配表（也称为前缀函数或失败函数）跳过尽可能多的不必要的比较。

拓展知识：
Longest Prefix which is also Suffix
“相同的前后缀”这个概念是理解KMP算法中部分匹配表的关键。
在这里，我们所说的“前缀”和“后缀”指的是一个字符串的开头部分和结尾部分。

前缀：一个字符串的前缀是指从字符串的第一个字符开始，到任意中间位置结束的所有子字符串。例如，字符串"ABC"的前缀有："A", "AB"。
后缀：一个字符串的后缀是指从字符串的最后一个字符开始，到任意中间位置结束的所有子字符串。例如，字符串"ABC"的后缀有："C", "BC"。
当我们说“相同的前后缀”时，我们是指一个字符串的某个前缀和某个后缀完全相同。
但是，这里有一个重要的限制：我们不考虑整个字符串作为其自身的前缀或后缀。也就是说，我们要找的是字符串的非整体部分中相同的前后缀。

以字符串"ABABC"为例：

1 对于子串"ABA"：
前缀有："A", "AB"
后缀有："A", "BA"
这里最长的相同前后缀是"A"。

2 对于子串"ABAB"：
前缀有："A", "AB", "ABA"
后缀有："B", "AB", "BAB"
这里最长的相同前后缀是"AB"。
在构建KMP算法的部分匹配表时，我们对于每个子串都计算这样的最长相同前后缀的长度。
这个信息在实际的字符串搜索过程中用来优化搜索，即当发生不匹配时，可以根据这个长度跳过一些不必要的比较。

KMP算法分为两个主要步骤：
1 构建部分匹配表：这个表存储了在模式字符串needle中，每个子串的前缀和后缀的最长公共元素长度。
    这个表用于决定在发生不匹配时，模式字符串应该向右移动多远。
2 字符串搜索：使用部分匹配表，我们可以在主字符串中高效地搜索模式字符串。
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 如果needle为空字符串，则返回0
        if not needle:
            return 0

        """
        build_lps 方法
        这个方法用于构建所谓的“最长相同前后缀”（Longest Prefix which is also Suffix，简称LPS）数组。
        这个数组是KMP算法的核心，它存储了在needle中每个位置不匹配时我们应该跳转到哪个位置。

        lps数组初始化为和needle一样长的0数组。
        length变量用来追踪当前最长的相同前后缀的长度。
        通过比较needle的字符来更新lps数组。
        """
        # 构建部分匹配表
        def build_lps(needle: str):
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

        """
        这个方法实现了KMP算法的主体。

        i和j分别是haystack和needle的索引。
        如果haystack[i]和needle[j]匹配，那么两个索引都往前移动。
        如果j和needle的长度相同，表示找到了一个匹配项，返回i - j（匹配的起始位置）。
        如果haystack[i]和needle[j]不匹配，那么根据lps[j - 1]来决定j的下一个位置。如果j为0，则i前进。
        如果整个haystack都搜索完毕还没有找到匹配项，则返回-1。
        """
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


