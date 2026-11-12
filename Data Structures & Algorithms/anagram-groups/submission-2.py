class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort = {}
        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            
            if tuple(freq) in sort:    
                sort[tuple(freq)].append(word)
            else:
                sort[tuple(freq)] = [word]

        return list(sort.values())