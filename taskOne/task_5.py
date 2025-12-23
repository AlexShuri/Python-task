s = input().strip()
i = 0
result = ""
while i < len(s):
    ch = s[i]
    count = 1
    while i + 1 < len(s) and s[i] == s[i + 1]:
        count += 1
        i += 1

    if result == "":
        result = f"({count}, {ch})"
    else:
        result += f" ({count}, {ch})"
    i += 1
print(result)