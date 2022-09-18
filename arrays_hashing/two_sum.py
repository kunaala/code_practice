import enum
def twoSum(nums, target):
    diff ={}
    for idx,val in enumerate(nums):
        if target - val in diff:
            return [diff[target-val], idx]
        else:
            diff[val] = idx
    return

def twoPointerSum(nums, target):
    l,r = 0, len(nums) -1
    while l < r:
        if nums[l] + nums[r] == target:
            return [l+1,r+1]
        elif target - nums[l] > nums[r]:
            l+=1
        else:
            r-=1

if __name__ == "__main__":
    nums = [3,4,7,3]
    target = 6 
    print(twoPointerSum(nums,target)) 