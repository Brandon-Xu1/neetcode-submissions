class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublist = {}
        

        for word in strs:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            key = tuple(freq)
            if key in sublist:
                sublist[key].append(word)
            else:
                sublist[key] = [word]
    
        return list(sublist.values())
