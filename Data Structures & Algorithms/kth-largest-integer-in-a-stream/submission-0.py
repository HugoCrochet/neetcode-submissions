class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        numbers = self.nums
        numbers_sorted = sorted(numbers)
        return numbers_sorted[-self.k]
        
