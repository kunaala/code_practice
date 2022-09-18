def characterReplacement( s: str, k: int) -> int:
    l,r = 0,1
    char_map ={}
    max_len = 0
    for r in range(len(s)):
        char_map[s[r]] = char_map.get(s[r],0) + 1
        while (r-l+1) - max(char_map.values()) > k: 
            char_map[s[l]] -= 1
            l+=1
            print("changed lptr", s[l])
        max_len = max(max_len,r-l+1)
                
        print(l,r,char_map,max_len)
    

    return max_len

if __name__ == "__main__":
    s = "ABAA"
    print(characterReplacement(s,0))