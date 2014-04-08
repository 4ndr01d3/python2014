def radix(number, r = 16, case = "upper"):
    lower = "0123456789abcdef"
    upper = "0123456789ABCDEF"
    if case == "upper":
        digits = upper
    else:
        digits = lower
    ret = ""
    while number > 0:
        ret = digits[number % r] + ret
        number = number/r
    return ret


for i in range(100):
    print radix(i,2)

