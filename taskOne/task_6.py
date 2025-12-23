import math
import re
s = input()
i = 0 
result = ""
er = [',', '.', '-', '_', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
while i < len(s):
    ch = s[i]
    if er.count(ch) == 0:
        if ch == ch.upper():
            ch = ch.lower()
        else:
            ch = ch.upper()
        result += ch
    else:
        result += ch
    i += 1