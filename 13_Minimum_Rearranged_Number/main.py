# Rearrange the digits of a number to create the minimum possible value without leading zeros.

def MinimumInteger(num):
    if num == 0:
        return 0
    
    is_negative = num < 0

    # don't care if it is negative just make it absolute for further working.
    absnum = abs(num)

    # convert the integer in list
    digits = [int(digit) for digit in str(absnum)]

    # 1 if postive no. sort in asc without leading 0 else in desc

    if not is_negative:
        digits.sort()

        if digits[0] == 0:
            for i in range(1 , len(digits)):

                if digits[i] > 0:

                    digits[0] , digits[i] = digits[i] , digits[0]
                     
                    break

    else:
        digits.sort(reverse=True)

    # the sorted list has been generated now convert it back into int
    result = int("".join(str(d) for d in digits))

    if is_negative:
        result = -result
    return result

num = int(input())
print(MinimumInteger(num))