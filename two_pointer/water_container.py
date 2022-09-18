def maxArea(heights) -> int:
        l,r = 0, len(heights) -1 
        max_area = min(heights[l],heights[r])*(r-l)
        
        while l < r: 
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
            area = min(heights[l],heights[r])*(r-l)
            max_area = max(area,max_area)
            # print(heights[l],heights[r],area,max_area)
        return max_area

if __name__ == "__main__":
    heights = [1,4,2,18,12,2,4,1]
    print(maxArea(heights))