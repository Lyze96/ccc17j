def findlength(height, data = []):

    a = 1
    b = height-1

    length = 0

    while a <= b:
        if a == b:
            num = int(data[a]/2)
            length += num
        elif data[a] > 0 and data[b] > 0:
            num = min(data[a], data[b])
            length += num

        a += 1
        b -= 1

    return length


boards = int(input())
datastr = input().split()
data = []

for i in range(4001):
    data.append(0)

for d in datastr:
    data[int(d)] += 1

maxlength = 0
ways = 0

for h in range(2, 4001):

    length = findlength(h, data)

    if length > maxlength:
        maxlength = length
        ways = 0

    if length > 0 and length == maxlength:
        ways += 1

print(maxlength, ways)