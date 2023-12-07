"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

示例 2：
输入：digits = ""
输出：[]

示例 3：
输入：digits = "2"
输出：["a","b","c"]

利用回溯算法逐步构建字母组合，通过递归调用来探索所有可能的路径，从而生成所有符合条件的字母组合。

1. 函数定义:
def backtrack(index, path):
这个函数接受两个参数：index 表示当前正在处理的数字的索引，path 表示到目前为止形成的字母组合的路径。

2. 终止条件:
if index == len(digits):
    combinations.append("".join(path))
    return
当 index 等于输入数字字符串的长度时，意味着已经处理完所有的数字。此时，path 包含了一种完整的字母组合，我们将它加入到结果列表中，并返回。

3. 探索所有可能的字母:
possible_letters = phone_map[digits[index]]
for letter in possible_letters:
    ...
对于每个数字，我们查找它对应的所有可能的字母（例如，对于 '2'，可能的字母是 'a', 'b', 'c'）。然后，我们遍历这些字母。

4. 递归地构建字母组合:
path.append(letter)
backtrack(index + 1, path)
path.pop()
对于当前数字的每个可能字母，我们将其添加到路径中，并递归地调用 backtrack 函数来处理下一个数字。
这就是“深度优先搜索”的部分，我们深入探索每个可能的字母，直到达到字符串的末尾。
一旦返回，我们移除路径中的最后一个字母（这就是“回溯”的部分），以便于探索同一层的其他可能字母。

初始调用
输入 digits = "23"
初始调用 backtrack(0, [])
第一步：处理数字 '2'
index = 0，表示我们现在处理的是输入中的第一个数字，即 '2'。
path = []，开始时没有任何字母被选中。
数字 '2' 对应的字母是 ['a', 'b', 'c']。
循环：遍历 '2' 对应的字母
选择 'a'

调用 backtrack(1, ['a'])
index = 1，现在处理下一个数字 '3'
path = ['a']，路径更新为包含字母 'a'
选择 'b'

调用 backtrack(1, ['b'])
index = 1，继续处理数字 '3'
path = ['b']，路径更新为包含字母 'b'
选择 'c'

调用 backtrack(1, ['c'])
index = 1，继续处理数字 '3'
path = ['c']，路径更新为包含字母 'c'
第二步：处理数字 '3'
重复上述过程对于数字 '3' 的每个字母。数字 '3' 对应的字母是 ['d', 'e', 'f']。

当 path = ['a'] 时
添加 'd'

path = ['a', 'd']，调用 backtrack(2, ['a', 'd'])
index = 2，达到 digits 长度，将 'ad' 添加到结果中，然后回溯
添加 'e'

path = ['a', 'e']，调用 backtrack(2, ['a', 'e'])
index = 2，达到 digits 长度，将 'ae' 添加到结果中，然后回溯
添加 'f'

path = ['a', 'f']，调用 backtrack(2, ['a', 'f'])
index = 2，达到 digits 长度，将 'af' 添加到结果中，然后回溯
当 path = ['b'] 时
对于 'b' 重复上述过程，生成 'bd', 'be', 'bf'
当 path = ['c'] 时
对于 'c' 重复上述过程，生成 'cd', 'ce', 'cf'
结果
最终结果为所有生成的组合：['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 如果输入为空，则直接返回空列表
        if not digits:
            return []

        # 定义数字到字母的映射，类似于电话按键
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # 回溯函数，用于生成字母组合
        def backtrack(index, path):
            # 如果当前路径长度与数字长度相同，将路径加入到结果中
            if index == len(digits):
                combinations.append("".join(path))
                return

            # 获取当前数字对应的所有可能字母
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                # 将当前字母加入路径并进入下一个数字
                path.append(letter)
                backtrack(index + 1, path)
                # 回溯，移除路径中的最后一个字母
                path.pop()

        # 存储所有可能的字母组合
        combinations = []
        backtrack(0, [])
        return combinations

# 创建 Solution 类的实例并测试
sol = Solution()
example1 = sol.letterCombinations("23")
example2 = sol.letterCombinations("")
example3 = sol.letterCombinations("2")


