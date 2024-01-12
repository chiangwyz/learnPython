"""
给定两个字符串 s 和 t ，判断它们是否是同构的。
如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。
不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

zip 是一个非常有用的内置函数，它将两个（或更多）迭代器（如列表、元组、字符串等）"压缩"在一起，并返回一个元组的迭代器。
每个元组包含来自每个输入迭代器的元素，这些元素在它们各自的迭代器中具有相同的索引。
在 isIsomorphic 函数中，zip 被用来同时迭代两个字符串 s 和 t。它每次从两个字符串中各取出一个字符，然后将这两个字符作为一对返回。

举个例子，如果 s = "abc" 和 t = "xyz"，zip(s, t) 会生成一个迭代器，这个迭代器依次产生元组 ('a', 'x')、('b', 'y') 和 ('c', 'z')。
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 建立两个映射，一个是s到t的映射，一个是t到s的映射
        s_to_t = {}
        t_to_s = {}

        for char_s, char_t in zip(s, t):
            # 如果s到t的映射已经存在并且不等于char_t，或者
            # t到s的映射已经存在并且不等于char_s，则不是同构的
            if (char_s in s_to_t and s_to_t[char_s] != char_t) or \
               (char_t in t_to_s and t_to_s[char_t] != char_s):
                return False

            # 建立新的映射
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True

# 示例测试
# 使用示例
sol = Solution()
print(sol.isIsomorphic("egg", "add"))  # 输出：True
print(sol.isIsomorphic("foo", "bar"))  # 输出：False
print(sol.isIsomorphic("paper", "title"))  # 输出：True
