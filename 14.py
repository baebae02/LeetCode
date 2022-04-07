#14. Longest Common Prepix
class Solution(object):
  
    def longestCommonPrefix(self, strs):
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for item in strs:
                if item[i] != ch:
                    return item[:i]
        return shortest
    """
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        shortest = min(strs,key=len)
        print(shortest)
        for i, ch in enumerate(shortest):
            for other in strs:
                print(i, ch, other)
                if other[i] != ch:
                    print("ANS:", i, ch, other)
                    return shortest[:i]
        return shortest 
      """
