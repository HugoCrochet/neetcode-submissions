class Solution:
    def maxArea(self, heights: List[int]) -> int:
        h,L=0,0
        l,r=0,len(heights)-1
        volume,water=0,0
        while l<r:
            h = min(heights[l], heights[r])
            L = r-l
            volume = h*L
            if volume > water: water = volume
            if heights[l]<heights[r]: l+=1
            else:r-=1
        return water        

        
        