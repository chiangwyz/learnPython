"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

比较巧妙的是defaultdict的使用与d[''.join(sorted(s))].append(s)使用，
当执行 sorted(s) 时，每个字符串都会被分解为字符，并且这些字符会被排序，所以结果都会是相同的字符列表 ['a', 'e', 't']。
然后 ''.join(sorted(s)) 会将排序后的字符列表连接成一个字符串，即 "aet"。
此时，d["aet"].append(s) 将原始的字符串 s 添加到字典 d 中键为 "aet" 的列表中。
因此，所有这些字符串经过排序后都会映射到同一个键 "aet"，并且它们原始的形式会被存储在与这个键关联的列表中。
这样一来，"eat", "tea", "ate" 由于是彼此的字母异位词，它们就会被分组到一起。最终 groupAnagrams 函数返回的列表中，会包含一个子列表 ["eat", "tea", "ate"]，
其中包含了所有彼此为字母异位词的字符串。
"""

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Create a default dictionary to hold lists for each sorted string
        d = defaultdict(list)
        # Iterate over each string
        for s in strs:
            # Sort the characters of the string and use the sorted string as the key
            # Add the original string to the corresponding list
            d[''.join(sorted(s))].append(s)
        # Return a collection of all the lists in the dictionary, which are the grouped anagrams
        return list(d.values())
