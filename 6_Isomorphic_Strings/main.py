def Isomporphic_strings(s , t):
    if len(s) != len(t):
        return False
    
    # taking two dictionaries one for s string and other for t string
    s_dict , t_dict = {} , {}
    for i in range(len(s)):
        char_s = s[i]
        char_t = t[i]
        if char_s not in s_dict:
            s_dict[char_s] = char_t
        
        if char_t not in t_dict:
            t_dict[char_t] = char_s

        if s_dict[char_s] != char_t or t_dict[char_t] != char_s:
            return False
    return True

s = "paper"
t = "title"
result = Isomporphic_strings(s , t)
if result == True:
    print("true")
else:
    print("false")