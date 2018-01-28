d = int(input())

result = int(d/720)*31
d = d % 720

time = 0
while time <= d:

    if int(time / 60) % 12 == 0:
        hour1 = 1
        hour2 = 2
    else:
        hour1 = int(((time / 60) % 12) / 10)
        hour2 = int(((time / 60) % 12) % 10)

    min1 = int((time % 60) / 10)
    min2 = int((time % 60) % 10)

    for i in range(-4, 5):
        if hour1 == 0 and min1 == hour2+i and min2 == hour2+(2 * i):
            result += 1
        if hour1 == 1 and hour2 == hour1+i and min1 == hour1+(2 * i) and min2 == hour1+(3 * i):
            result += 1

    time += 1


print(result)