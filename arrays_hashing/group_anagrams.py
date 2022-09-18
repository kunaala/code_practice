def groupAnagrams(strs):
    dict_list =[]
    grp_list ={}
    idx = 0 
    for i in strs:
        d ={}
        for ch in i:
            d[ch] = 1 + d.get(ch,0)   
        if d in dict_list:
            grp = dict_list.index(d) 
            grp_list[grp].append(i)
        else:
            dict_list.append(d)
            grp_list[idx] = [i]
            idx+=1
            
    return list(grp_list.values())

if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))
