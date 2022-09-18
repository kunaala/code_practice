def product_array(nums):
    answer = [1] * len(nums)

    acc = 1
    for i in range(len(nums)):
        acc *= nums[i]
        answer[i] = acc 
    acc = 1
    print(answer)
    for i in range(len(nums)-1,-1,-1):
        if i > 0:
            answer[i] = acc * answer[i-1]
            acc *= nums[i]
        else:
            answer[i] = acc
    return answer


if __name__ == "__main__":
    nums = [3,4,7,3]
    print(product_array(nums)) 