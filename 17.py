digits = "zero one two three four five six seven eight nine".split()
teens  = "ten eleven twelve thirteen fourteen fifteen " \
         "sixteen seventeen eighteen nineteen".split()
tens   = "zero ten twenty thirty fourty fifty sixty seventy eighty ninety" \
        .split()

def num(n):
    if n == 1000: return "one thousand"
    hund = n // 100
    tend = n % 100
    ret = ''
    if hund:
        ret = digits[hund] + " hundred"
    if tend:
        if hund: ret += " and "
        tenp = tend // 10
        onep = tend % 10
        if tenp == 1:
            ret += teens[onep]
        else:
            if tenp:
                ret += tens[tenp]
            if onep:
                if tenp: ret += '-'
                ret += digits[onep]
    return ret

print(sum(sum(1 for ch in num(n) if ch not in ' -')
    for n in range(1, 1000 + 1)))
