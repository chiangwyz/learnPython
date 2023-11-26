"""
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
如果可以，返回 true ；否则返回 false 。
magazine 中的每个字符只能在 ransomNote 中使用一次。
"""

class Solution:
    # Python 函数来判断 ransomNote 是否可以由 magazine 中的字符构成
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
