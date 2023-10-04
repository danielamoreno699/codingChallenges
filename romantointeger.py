def romanToInt(s):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0

    for i in reversed(s):
        if i in dic:
            if value > 0 and dic[i] < dic[s[s.index(i) + 1]]:
                value -= dic[i]
            else:
                value += dic[i]

    return value

print(romanToInt('VI'))  # Should print 6
print(romanToInt('IV'))  # Should print 4
