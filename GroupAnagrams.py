class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in words:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(word)
        
        return list(res.values())