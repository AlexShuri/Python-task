s = input()
n = int(input())
i = 0
result = ""
len_s = len(s)
while i < len_s:
    if (i + 1) % n == 0:
        result += s[i]
        print(result)
        result = ""
    else:
        result += s[i]
    if i + 1 == len_s:
        print(result)
        break
    i += 1