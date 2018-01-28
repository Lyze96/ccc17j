n = int(input())
k = int(input())

result = 0

for i in range(k+1):
    result += n
    n *= 10

print(result)