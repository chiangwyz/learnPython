# unittest简介

```unittest``` 是 Python 标准库中的一个单元测试框架。它提供了一系列工具，用于编写和运行测试，以检查代码的正确性。单元测试是软件开发中一个重要部分，它可以帮助开发者验证代码的行为符合预期，同时也便于日后的代码维护和更新。

## 主要特性

1. 测试用例（Test Cases）：

* unittest 中的基本单位是 TestCase 类。你可以通过继承这个类来创建新的测试用例。

2. 测试套件（Test Suites）：

* 测试套件是一系列的测试用例或测试套件。它用于组合和包含需要一起执行的测试。

3. 测试运行器（Test Runners）：

* 这是用于执行测试的组件。它们会运行测试套件，并提供结果（例如：测试是否通过，错误信息等）。

4. 断言（Assertions）：

* unittest 提供了一系列的断言方法，用于检查特定条件是否为真。常见的断言包括 assertEqual, assertTrue, assertFalse, 等。

## 基本流程

1. 编写测试用例：

* 继承 unittest.TestCase 并定义测试方法（以 test 开头）。

2. 设置和清理：

* 可以使用 setUp 方法在每个测试方法之前进行初始化设置。
* 使用 tearDown 方法在每个测试方法之后进行清理。

3. 运行测试：

* 通过调用 unittest.main() 在脚本底部运行测试。

```python
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        # 初始化设置
        pass

    def test_something(self):
        # 实际的测试内容
        self.assertEqual(1 + 1, 2)

    def tearDown(self):
        # 清理代码
        pass

if __name__ == '__main__':
    unittest.main()
```