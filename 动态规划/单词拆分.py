"""
1. 首先，将提供的单词列表转换为一个集合（wordSet），以便快速查找。
2. 然后，初始化一个动态规划数组 dp，其中 dp[i] 表示字符串 s 的前 i 个字符是否可以由 wordDict 中的单词构成。存储的是True或者False。
3. 接下来，代码通过两层循环检查每个子字符串，如果找到了符合条件的子字符串，就将相应的 dp 值设置为 True。
4. 最后，返回 dp[len(s)] 的值，即整个字符串 s 是否可以由字典中的单词构成。

让我们使用示例 1（s = "leetcode", wordDict = ["leet", "code"]）来逐步解析代码，并说明变量的状态。

1. 首先，我们初始化 wordSet 和 dp。
    wordSet 是一个集合，包含字典中的所有单词。
    dp 是一个布尔数组，用于记录字符串 s 的每个前缀是否可以由字典中的单词拼接而成。dp[0] 初始化为 True，因为空字符串可以被“构成”。

python
Copy code
s = "leetcode"
wordDict = ["leet", "code"]
wordSet = set(wordDict)  # wordSet = {"leet", "code"}
dp = [False] * (len(s) + 1)  # dp = [False, False, False, False, False, False, False, False, False]
dp[0] = True  # dp = [True, False, False, False, False, False, False, False, False]
现在，我们逐步遍历 s，并更新 dp 数组：

当 i = 1 时，我们检查 s[0:1]（即 "l"）。没有 j < 1 使得 dp[j] 为 True 且 s[j:1] 在 wordSet 中。所以 dp[1] 保持为 False。
当 i = 2 时，同样地，我们找不到合适的 j 使得 s[j:2]（即 "le"）在 wordSet 中。所以 dp[2] 仍为 False。
这个过程继续进行，直到 i = 4。当 i = 4 时，我们检查 s[0:4]（即 "leet"）。我们发现，对于 j = 0，dp[j] 是 True（因为 dp[0] 表示空字符串），并且 "leet" 在 wordSet 中。
因此，我们将 dp[4] 设置为 True。
继续这个过程，直到 i = 8。当 i = 8 时，我们检查 s[0:8]（即整个字符串 "leetcode"）。
我们可以找到 j = 4 使得 dp[j] 为 True（因为我们之前设置了 dp[4] 为 True），并且 s[4:8]（即 "code"）在 wordSet 中。
因此，我们将 dp[8] 设置为 True。
最终，dp 数组的状态将是 [True, False, False, False, True, False, False, False, True]，其中 dp[len(s)]（即 dp[8]）为 True。
这表示整个字符串 s 可以由字典中的单词拼接而成。
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
