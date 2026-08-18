class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices)):
            print("current i :", i, "price : ", prices[i])
            for j in range (i+1, len(prices)):
                print("current j :", j, "price : ", prices[j])
                print("diff : ", prices[j]-prices[i])
                if prices[j]-prices[i]>max:
                    max = prices[j]-prices[i]
            
            print("for now tha max is : ", max)    
        return max


        