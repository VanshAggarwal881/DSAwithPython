def Valid_p(string):
    stack = []
    closeToOpen = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }

    for i in string:
        # string : "[()]"
        # since keys of hashmap : closetoopen .... are closing only and their values are opening tags so we will fill the stack with opening tags only so that when i becomes closing in string then...
        if i not in closeToOpen:
            stack.append(i)

        # then it will be present in the hashmap askeys and we will compare their values with the last element of stack like this and try to make the stack empty
        else:
            if stack and stack[-1] == closeToOpen[i]:
                stack.pop()

    # IF STRING IS "((((" THEN IT WILL ONLY FILL THE STACK AND THE CONDITION WILL NEVER TOUCH ELSE STAEMENT TO MAKE THE STACK EMPTY SO HERE IS THE RETURN CONDITION

    return True if not stack else False

s = input()
result = Valid_p(s)
if result:
    print("true")
else:
    print("false")