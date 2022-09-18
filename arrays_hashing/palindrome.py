def isPalindrome(strs) -> bool:
    charList = []
    for i in range(len(strs)):
        if strs[i].isalnum():
            charList.append(strs[i].lower())
    return charList == charList[::-1]
   

def validPalindrome(strs) -> bool:
    l = 0
    r = len(strs)-1
    while l < r:
        if not strs[l].isalnum():
            l+=1
            continue
        if not strs[r].isalnum():
            r-=1
            continue
        if strs[l].lower() == strs[r].lower():
            l+=1
            r-=1            
        else:
            return False
    return True

if __name__ == "__main__":
    strs = "A man, a plan, a canal: Panama"
    strs = "race a car"
    print(validPalindrome(strs)) 
