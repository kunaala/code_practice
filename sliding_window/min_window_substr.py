def minWindow(s: str, t: str) -> str:
    if len(t) > len(s): return ""
    wind_map, t_map = {}, {}
    for i in t:
        t_map[i] = t_map.get(i,0) + 1
    l =0
    matches = 0
    min_len = len(s)
    substr = ""
    for r in range(len(s)):
        # print(s[l:r+1])
        if s[r] in t_map:
            wind_map[s[r]] = wind_map.get(s[r],0) +1
            if wind_map[s[r]] == t_map[s[r]]:
                matches += 1
            while  l < len(s) and matches == len(t_map.keys()):
                cand_str = s[l:r+1]
                if len(cand_str) <= min_len: 
                    substr = cand_str
                    min_len = len(substr)
                if s[l] in wind_map: 
                    wind_map[s[l]] -= 1
                    if wind_map[s[l]] != t_map[s[l]]: matches -=1
                print("sliding to",l+1)
                l+=1
            
                
                

        print(s[l:r+1],substr,wind_map)
    return substr
            
        
if __name__ == "__main__":
    s1 = "aaaaaaaaaaaabbbbbcdd"
    s2 = "abcdd""
    
    print(minWindow(s1,s2))