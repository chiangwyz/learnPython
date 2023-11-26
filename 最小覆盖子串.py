class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # 字典来保存字符串 t 中所有唯一字符的计数
        dict_t = {}
        for character in t:
            dict_t[character] = dict_t.get(character, 0) + 1

        # 需要找的唯一字符的数量
        required = len(dict_t)

        # 左右指针，用于扩展和收缩滑动窗口
        l, r = 0, 0

        # formed 用于记录当前窗口中包含了多少个唯一字符，
        # 其值满足与 t 中该唯一字符的计数相同
        formed = 0

        # 字典保存当前窗口中所有唯一字符的计数
        window_counts = {}

        # (窗口长度, 左指针, 右指针)
        ans = float("inf"), None, None

        while r < len(s):
            # 从右侧向窗口中添加一个字符
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            # 如果当前添加的字符的数量等于 t 中该字符的数量，则 formed 加 1
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # 尝试并缩小窗口直到它不再涵盖 t 的所有字符
            while l <= r and formed == required:
                character = s[l]

                # 保存可能的最小窗口
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # 窗口左侧的字符将从窗口中移除
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # 移动左指针，我准备检查下一个窗口
                l += 1

            # 移动右指针，我准备检查下一个窗口
            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]:(ans[2] + 1)]

