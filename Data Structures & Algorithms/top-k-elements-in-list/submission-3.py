class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort(key=lambda x:-x[0])

        res = []
        i=0
        while len(res) < k:
            res.append(arr[i][1])
            i += 1
        return res
        