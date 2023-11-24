"""
对于字符串数组 ["flower","flow","flight"]，我们想要找到最长公共前缀：

初始化前缀: 设定 prefix 为数组中的第一个字符串 "flower"。

第一次迭代:

s = "flower"，prefix 保持不变，因为它与自身匹配。
s = "flow"，这时 "flow" 确实是以 "flower" 的前缀 "flow" 开头的，所以 prefix 保持不变。
s = "flight"，不是以 "flower" 开头的，所以我们需要缩短 prefix。
缩短 prefix: 由于 "flight" 不是以 "flower" 开头的，我们需要逐个字符缩短 prefix：

缩短为 "flowe"，"flight" 不以此开头，继续缩短。
缩短为 "flow"，"flight" 仍不以此开头，继续缩短。
缩短为 "flo"，"flight" 仍不以此开头，继续缩短。
缩短为 "fl"，现在 "flight" 是以 "fl" 开头的。
第二次迭代: 用新的 prefix "fl" 再次遍历字符串数组以确认它是否是所有字符串的前缀。

s = "flower"，以 "fl" 开头，prefix 保持 "fl"。
s = "flow"，以 "fl" 开头，prefix 保持 "fl"。
s = "flight"，以 "fl" 开头，prefix 保持 "fl"。
结束: prefix 最终为 "fl"，这是所有字符串的公共前缀。
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
