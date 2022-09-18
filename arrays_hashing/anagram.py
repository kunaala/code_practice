def isAnagram(s, t):
    if len(s) != len(t):
        return False
    s_dict,t_dict = {}, {}
    for i in range(len(s)):
        s_dict[s[i]] = 1 + s_dict.get(s[i],0)
        t_dict[t[i]] = 1 + t_dict.get(t[i],0)
    
    # print(s_dict,t_dict)
    if s_dict == t_dict: return True
    else: return False

def sortAnagram(s,t):
    if sorted(s) == sorted(t):
        return True
    else:
        return False

if __name__ == "__main__":
    s = "malodhakar"
    t = "kardhaloma"
    print(isAnagram(s,t))
    print(sortAnagram(s,t))
