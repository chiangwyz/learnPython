"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

1. 比较巧妙的是defaultdict的使用与d[''.join(sorted(s))].append(s)使用，
2. 当执行 sorted(s) 时，每个字符串都会被分解为字符，并且这些字符会被排序，所以结果都会是相同的字符列表 ['a', 'e', 't']。
3. 然后 ''.join(sorted(s)) 会将排序后的字符列表连接成一个字符串，即 "aet"。
4. 此时，d["aet"].append(s) 将原始的字符串 s 添加到字典 d 中键为 "aet" 的列表中。
5. 因此，所有这些字符串经过排序后都会映射到同一个键 "aet"，并且它们原始的形式会被存储在与这个键关联的列表中。
6. 这样一来，"eat", "tea", "ate" 由于是彼此的字母异位词，它们就会被分组到一起。
    最终 groupAnagrams 函数返回的列表中，会包含一个子列表 ["eat", "tea", "ate"]，其中包含了所有彼此为字母异位词的字符串。

d = defaultdict(list) 这行代码并不是创建一个空的普通字典，而是创建了一个特殊类型的字典，称为“默认字典”（defaultdict），其来自于 Python 的 collections 模块。
在 defaultdict 中，当尝试访问一个还不存在的键时，它会自动为该键创建一个默认值。
在这个例子中，list 被传递给 defaultdict 作为默认工厂函数，意味着如果你尝试访问 defaultdict 中还不存在的键，它将自动为该键创建一个新的空列表作为默认值。
"""
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 使用 defaultdict 创建一个字典，字典的值是列表
        d = defaultdict(list)
        # 遍历字符串列表中的每个字符串
        for s in strs:
            # 对字符串的字符进行排序，并将排序后的字符串作为键
            # 将原始字符串添加到对应的列表中
            d[''.join(sorted(s))].append(s)
        # 返回字典中所有列表的集合，这些列表就是分组好的字谜
        return list(d.values())

# test
solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(solution.groupAnagrams(strs))
