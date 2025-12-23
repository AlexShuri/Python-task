numbers = list(map(int, input().split()))
result = 1
for i in numbers:
    result *= i
print(result)