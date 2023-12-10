"""
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
如果可以，返回 true ；否则返回 false 。
magazine 中的每个字符只能在 ransomNote 中使用一次。


解题思路：
通过比较 magazine 字符串中字符的数量是否满足 ransomNote 字符串中相应字符的需求，
来决定 ransomNote 能否由 magazine 构成。
这个过程中，magazine 中的每个字符计数都会被逐一减去 ransomNote 中相应字符的使用，
如果 magazine 中的字符数量足够，最终将返回 True，表示可以构成；
如果任何时候字符数量不足，将返回 False，表示无法构成。
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
      # 创建一个字典来保存 magazine 中每个字符的计数
      magazine_counts = {}
      for char in magazine:
          magazine_counts[char] = magazine_counts.get(char, 0) + 1
  
      # 遍历 ransomNote，检查每个字符是否在 magazine 中有足够的数量
      for char in ransomNote:
          if magazine_counts.get(char, 0) == 0:
              return False
          magazine_counts[char] -= 1
  
      return True
