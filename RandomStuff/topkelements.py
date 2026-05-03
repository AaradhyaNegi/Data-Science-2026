class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        res = []
        most_common = c.most_common()

        for i in range(k):
            res.append(most_common[i][0])
        return res