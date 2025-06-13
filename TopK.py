class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for i in range(len(nums) + 1)]

        for key, val in count.items():
           bucket[val].append(key)
        
        res = []
        for l in range(len(nums), 0, -1):
            for i in bucket[l]:
                res.append(i)
                if len(res) == k:
                    return res