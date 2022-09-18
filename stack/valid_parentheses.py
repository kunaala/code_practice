from collections import deque

def isValid(s: str) -> bool:
    deq = deque()
    match = {'(':')','{':'}','[':']'}
    if len(s) % 2 == 1: return False 
    for i in s:
        if i in match:
            deq.append(i)
        elif len(deq) != 0 and i == match[deq[-1]]:
            deq.pop()
        else:
            return False
        # print(i,deq)
    if len(deq) == 0: return True
    return False

if __name__ == "__main__":
    bracket_str = "[{()}]"
    print(isValid(bracket_str))