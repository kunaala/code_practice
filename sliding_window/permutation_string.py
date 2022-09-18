def checkInclusion(s1,s2):
    s1_map = {}
    for i in s1:
        s1_map[i] = s1_map.get(i,0) + 1
    l,r = 0,0
    while r<len(s2):
        while l < len(s2) and s2[l] not in s1_map:
            l+=1
        s2_map = {}
        # print("reset window",l)
        r = l
        while r-l < len(s1) and r<len(s2) and s2[r] in s1_map:
            s2_map[s2[r]] = s2_map.get(s2[r],0) + 1
            r +=1
            # print(s1_map,s2_map)
        if s2_map == s1_map:
            # print(s1_map,s2_map)
            return True  
        else: 
            l +=1
        
    return False

def checkSubstrAnagram(s1,s2):
    if len(s1) > len(s2):
        return False
    s1Count, s2Count = [0] * 26, [0] * 26
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1
    matches = 0
    for i in range(26):
        matches += 1 if s1Count[i] == s2Count[i] else 0
    l =0
    for r in range(len(s1),len(s2)):
       if matches == 26: return True
       else:
            idx = ord(s2[r]) - ord('a')
            s2Count[idx] += 1
            if s2Count[idx] == s1Count[idx]: matches+=1
            elif s2Count[idx] == s1Count[idx]+1: matches -=1

            idx = ord(s2[l]) - ord('a')
            s2Count[idx] -= 1
            if s2Count[idx] == s1Count[idx]: matches+=1
            elif s2Count[idx] == s1Count[idx]-1: matches -=1
            l+=1
    return matches==26





if __name__ == "__main__":
    s1 = "abc"
    # s1 = "adc"
    s2 = "eidbaooacbo"
    # s2 = "dcda"
    print(checkSubstrAnagram(s1,s2))