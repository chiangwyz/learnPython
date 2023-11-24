"""
我们以数组 ["flower","flow","flight"] 为例，逐步解释找到最长公共前缀的过程：
1. 初始化：
将 prefix 设置为数组中的第一个字符串，即 prefix = "flower"。
2. 对数组中的每个字符串进行迭代：
第一个字符串是 "flower"，它与自己比较，自然是以 prefix 开头的，所以 prefix 保持不变。
下一个字符串是 "flow"，我们检查 "flow" 是否以 prefix 即 "flower" 开头。显然，"flow" 不是 以 "flower" 开头的。因此，我们需要更新 prefix。
3. 更新 prefix：
由于 "flow" 不以 "flower" 开头，我们开始逐个字符减少 prefix 的长度。我们先将 prefix 缩短为 "flowe"，但 "flow" 仍然不以 "flowe" 开头。
继续缩短 prefix 为 "flow"，现在 "flow" 是以 "flow" 开头的。所以，我们继续将这个新的 prefix 与下一个字符串比较。
4. 继续迭代：
下一个字符串是 "flight"。我们检查 "flight" 是否以新的 prefix "flow" 开头。显然，它不是。
我们继续缩短 prefix：减少到 "flo"，然后是 "fl"。当 prefix 缩短为 "fl" 时，"flight" 以 "fl" 开头。
5. 完成迭代：
现在，我们已经确定 "fl" 是 "flower"、"flow" 和 "flight" 的公共前缀。因为我们已经迭代完所有的字符串，没有更多的字符串可以比较了。
6. 返回结果：
最终的公共前缀是 "fl"，这是这个字符串数组的最长公共前缀。

通过这个方法，我们可以有效地找到一个字符串数组中的最长公共前缀。在每一步中，我们都确保了 prefix 是当前考虑的所有字符串的公共前缀。
如果在任何时候 prefix 为空，意味着没有公共前缀，我们将立即返回空字符串。在我们的例子中，公共前缀 "fl" 被正确地识别并将被函数返回。
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # 如果字符串数组为空，则直接返回空字符串
        if not strs:
            return ""
        
        # 初始化公共前缀为第一个字符串
        prefix = strs[0]
        
        # 遍历字符串数组中的每个字符串
        for s in strs:
            # 检查当前字符串是否以当前公共前缀开头
            while not s.startswith(prefix):
                # 如果不是，公共前缀减少最后一个字符，直到为空或满足条件
                prefix = prefix[:-1]
                # 如果公共前缀已经为空，直接返回空字符串
                if not prefix:
                    return ""
        
        # 返回最终的公共前缀
        return prefix
