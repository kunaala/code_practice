def longestConsecutive(nums):
    longest = 0
    nums = set(nums)
    for i in nums:
        if i-1 not in nums:
            seq_len =1
            while i+1 in nums:
                seq_len +=1
                i+=1
            longest = max(seq_len,longest)  
    return longest

if __name__ == "__main__":
    nums = [0,9,3,10,11,2,1,12,13,5,4] 
    print(longestConsecutive(nums)) 