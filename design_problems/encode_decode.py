
def encode(strs):
    encoded_str =""
    for i in strs:
        encoded_str += str(len(i))+ "|" + i
    return encoded_str

def decode(encoded_str):
    strs, i =[],0
    while i < len(encoded_str):
        num = int(encoded_str[i])
        strs.append(encoded_str[i+2:i+2+num])
        i+=num+2
    return strs


if __name__ == "__main__":
    strs = ["hai","how","do","you","do"]
    encoded_str = encode(strs)
    print(decode(encoded_str)) 