import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    # 注意我们如何使用原始字符串(在前面放一个‘r’)来避免必须转义反斜杠
    # 还要注意，我们对`@`字符进行了转义，因为它在某些正则表达式中具有特殊意义
    return users[users["mail"].str.match(r"^[a-zA-Z][a-zA-Z0-9_.-]*\@leetcode\.com$")]

