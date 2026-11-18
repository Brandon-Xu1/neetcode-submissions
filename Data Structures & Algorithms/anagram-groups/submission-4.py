class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for word in strs:
            freq = [0] * 26
            for char in word:
                value = ord(char) - ord('a')
                freq[value] += 1
            
            if tuple(freq) in seen:
                seen[tuple(freq)].append(word)
            else:
                seen[tuple(freq)] = [word]
        

        return list(seen.values())