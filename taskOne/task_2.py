numbers = list(map(int, input().split()))
count = 0
o = 0
q = 1
temp = []
for i in numbers:
    if temp.count(i) == 0:
        count += 1
        temp.append(i)
    elif temp.count(i) >= 1:
        continue
print(count)