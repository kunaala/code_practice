from email import charset


def lengthOfLongestSubstring(s):
    max_len = 0
    substr = set()
    mapstr = {}
    for idx,val in enumerate(s):
        if val not in substr: 
            substr.add(val)
            mapstr[val] = idx
            max_len = max(max_len,len(substr))
        else:
            ind = mapstr[val]
            substr = set()
            substr.update(s[ind:idx])
            mapstr[val] = idx
        print(substr,mapstr)
    return max_len

def longestSubstring(s):
    max_len = 0
    l = 0
    charSet = set()
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[r])
        max_len = max(max_len,r-l+1)
       
    return max_len


if __name__ == "__main__":
    s = "pwwkew"
    print(longestSubstring(s)) 