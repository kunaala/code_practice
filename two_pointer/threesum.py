def threeSum(nums):
    res = []
    nums = sorted(nums)
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        p1 = i+1
        p2 = len(nums)-1
        print(p1,p2,i)
        while p1 < p2:
            entry = [nums[p1], nums[p2], nums[i]] 
            if nums[p1] + nums[p2] == -nums[i]:
                res.append(entry)
                p1 += 1
                while nums[p1] == nums[p1-1] and p1 < p2:
                    p1+=1

            elif nums[p1] + nums[p2] < -nums[i]:
                p1+=1
            else:
                p2-=1
    return res

                

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    nums = [-1,-2,-2,1]
    print(threeSum(nums)) 