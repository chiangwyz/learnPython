"""
1. 首先，将提供的单词列表转换为一个集合（wordSet），以便快速查找。
2. 然后，初始化一个动态规划数组 dp，其中 dp[i] 表示字符串 s 的前 i 个字符是否可以由 wordDict 中的单词构成。存储的是True或者False。
3. 接下来，代码通过两层循环检查每个子字符串，如果找到了符合条件的子字符串，就将相应的 dp 值设置为 True。
4. 最后，返回 dp[len(s)] 的值，即整个字符串 s 是否可以由字典中的单词构成。
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 将字典转换成集合，便于快速查找
        wordSet = set(wordDict)
        # 初始化动态规划数组，dp[i]表示s的前i个字符是否可以由字典中的单词构成
        dp = [False] * (len(s) + 1)
        # 空字符串总是可以被构成
        dp[0] = True

        # 遍历字符串s的所有子串
        for i in range(1, len(s) + 1):
            for j in range(i):
                # 如果s的前j个字符可以被构成，且s[j:i]（即s的第j到第i-1个字符组成的子串）在字典中
                # 那么s的前i个字符也可以被构成
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break

        # 返回整个字符串s是否可以由字典中的单词构成
        return dp[len(s)]
