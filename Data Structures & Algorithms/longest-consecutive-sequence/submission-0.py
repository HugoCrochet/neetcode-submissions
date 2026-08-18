class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for x in num_set:
            if (x-1) not in num_set: 
                lenght = 1
                while (x+lenght) in num_set:
                    lenght +=1 
                if lenght > res: res = lenght
        return res

                