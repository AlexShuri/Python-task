n = int(input())
scores = list(map(int, input().split()))

temp = sorted(scores)
max_one = max(temp)
result = 0
i = len(temp) - 1
while i >= 0:
    if temp[i] < max_one:
        result = temp[i]
        break
    i -= 1
print(result)