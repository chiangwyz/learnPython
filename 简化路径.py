"""
思路：
1. 栈的使用：栈是一种先进后出的数据结构，适合用来处理类似路径这样的问题，
   因为我们可以通过入栈和出栈操作来模拟进入目录和返回上级目录的行为。
2. 路径分割：路径以斜杠 '/' 分割，因此我们首先将路径按照斜杠 '/' 分割成多个部分。
3. 遍历处理：遍历分割后的每个部分，根据它们的特性进行处理：
   如果是 '..', 表示需要返回上级目录，即从栈中弹出一个元素。
   如果是有效目录名，将其加入栈中。
   如果是 '.' 或空字符串，则忽略，因为它们分别表示当前目录和无效的路径部分。
4. 结果构建：遍历结束后，栈中的元素就是简化后的路径各部分，将它们用 '/' 连接起来，形成最终的简化路径。

这个路径 "/a/./b/../../c/" 是一个 Unix 风格的文件系统路径，每个部分代表了文件系统中的一个位置。
让我们分解这个路径，以便更好地理解它的含义：
/：路径的开始，表示根目录。
a/：进入名为 a 的子目录。
.：表示当前目录，所以 ./ 实际上并没有改变当前的位置。
b/：进入名为 b 的子目录。
..：表示上一级目录。第一个 ../ 会从 b 目录回到 a 目录。
..：第二个 ../ 会从 a 目录回到根目录（因为 a 已经是根目录下的一个子目录）。
c/：进入名为 c 的子目录。
因此，当我们按照这个路径走的时候，我们首先进入 a 目录，然后进入其子目录 b，接着回到 a，然后再回到根目录，最后进入 c 目录。
所以，最终的位置是根目录下的 c 目录，因此简化后的路径是 "/c"。

在这段代码中，使用 elif 而不是 else 是为了明确表达代码的意图和逻辑。
当你使用 if-elif-else 结构时，你正在表达一系列的特定条件检查，每个条件是互斥的。
在这种情况下，elif 用于明确指出每个条件是独立的，并且仅当前一个条件不满足时才会检查下一个条件。

例如，对于这段路径处理的代码：
第一个 if 检查的是当前部分是否是 ".."，即是否需要回到上一级目录。
elif 检查的是当前部分是否是 "." 或者为空，这表示当前目录或无效路径部分，应该忽略。
最后的 else 处理所有其他情况，即有效的目录名。
使用 elif 而不是多个 if 或者 else，可以提高代码的可读性，让其他开发者（或未来的你）更容易理解每个条件检查的目的。
此外，它还可以防止在某些情况下发生不必要的条件评估，提高代码效率。
"""
class Solution:
    def simplifyPath(self, path: str) -> str:
        # 创建一个栈来存储路径的各个部分
        stack = []
        # 使用斜杠 '/' 将路径分割成多个部分
        parts = path.split('/')

        # 遍历路径的每个部分
        for part in parts:
            # 如果当前部分是 '..'，表示需要返回上一级目录
            if part == '..':
                # 如果栈不为空，弹出栈顶元素，即返回上级目录
                if stack:
                    stack.pop()
            # 如果当前部分是有效目录名（即非空且不是 '.'），则将其添加到栈中
            elif part and part != '.':
                stack.append(part)

        # 使用单个斜杠 '/' 将栈中的所有目录名连接起来，并确保结果以斜杠 '/' 开头
        return '/' + '/'.join(stack)

# 示例测试
sol = Solution()
print(sol.simplifyPath("/home/"))  # 输出："/home"
print(sol.simplifyPath("/../"))    # 输出："/"
print(sol.simplifyPath("/home//foo/"))  # 输出："/home/foo"
print(sol.simplifyPath("/a/./b/../../c/"))  # 输出："/c"






