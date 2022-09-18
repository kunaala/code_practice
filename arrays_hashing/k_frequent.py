def k_frequent(nums, k):
    num_freq = {}
    for i in nums:
        num_freq[i] = 1 + num_freq.get(i,0) 
    return sorted(num_freq, key = num_freq.get,reverse=True)[:k]

def k_most_frequent(nums, k):
    freq_num = [[] for i in range(len(nums)+1)]
    num_freq = {}
    most_frequent = []
    for i in nums:
        num_freq[i] = 1 + num_freq.get(i,0) 
    for key,val in num_freq.items():
        freq_num[val].append(key)
    for i in freq_num[::-1]:
        if len(most_frequent) < k and len(i) != 0:
            [most_frequent.append(ele) for ele in i] 
    return most_frequent

if __name__ == "__main__":
    nums = [2,3,2,3,2,1]
    # most frequent two items
    k = 2
    print(k_most_frequent(nums,k)) 