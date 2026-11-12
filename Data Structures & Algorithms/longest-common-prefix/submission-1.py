class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            j = 0
            for char in strs[i]:
                if j < len(prefix):
                    if char == prefix[j]:
                        j+=1
                    else:
                        break
                else: 
                    break
            prefix = prefix[:j]
        return prefix
                
                