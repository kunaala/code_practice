

def detect_dupes(nums):
    hashset = set()
    for i in nums:
        if i not in hashset: 
            hashset.add(i)
        else:
            return True
    return False 

if __name__ == "__main__":
    nums = [1,1,1,3,3,4,3,2,4,2]
    nums = [1,2,3,4]
    print(detect_dupes(nums))
