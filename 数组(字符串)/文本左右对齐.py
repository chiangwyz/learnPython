"""
1. 初始化：创建一个空列表 result 用于存放最终结果，一个空列表 current_line 用于存放当前行的单词，
    以及一个整数 current_length 用于追踪当前行已使用的字符数（不包括空格）。

2. 遍历单词：遍历输入的 words 数组。对于每个单词，判断加入这个单词后是否会超过 maxWidth。
    如果不超过，就将其加入到 current_line 中，并更新 current_length。
    如果超过，就处理 current_line 中的单词，使其格式化为一行，然后清空 current_line 并添加当前单词。

3. 格式化行：为了格式化一行，需要计算空格的数量并均匀分配。如果 current_line 只有一个单词，那么这个单词后面应该跟随足够的空格。
    如果有多个单词，空格应该尽可能均匀分布在单词之间。最后一行应该是左对齐的，即在行尾填充空格。

4. 处理最后一行：在遍历结束后，最后一行可能还没有处理。按照左对齐的方式处理这一行，并添加到 result 中。

5. 返回结果：返回存放最终结果的 result 列表。
"""

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        # 存放最终结果
        result = []
        # 存放当前行的单词
        current_line = []
        # 当前行已使用的字符数（不包括空格）
        current_length = 0

        for word in words:
            # 判断是否需要新的一行
            if current_length + len(current_line) + len(word) > maxWidth:
                self.adjustLine(current_line, current_length, maxWidth, result)
                current_line, current_length = [], 0

            current_line.append(word)
            current_length += len(word)

        # 处理最后一行（左对齐）
        last_line = ' '.join(current_line).ljust(maxWidth)
        result.append(last_line)

        return result

    # 若需要新的新的一行，对新的一行进行组装
    def adjustLine(self, current_line, current_length, maxWidth, result):
        # 计算需要添加的空格总数
        space_count = maxWidth - current_length
        if len(current_line) == 1:
            # 如果只有一个单词，所有额外空格都加在这个单词后面
            current_line[0] += ' ' * space_count
        else:
            # 如果有多个单词，均匀分布空格
            space_between_words = space_count // (len(current_line) - 1)  # 每个间隔的空格数
            extra_spaces = space_count % (len(current_line) - 1)  # 不能均匀分配的额外空格数

            for i in range(len(current_line) - 1):
                current_line[i] += ' ' * (space_between_words + (1 if i < extra_spaces else 0))

        # 将调整好的行添加到结果中
        result.append(''.join(current_line))

# 测试
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

sol = Solution()
result1 = sol.fullJustify(words, maxWidth)
for res in result1:
    print(res)
