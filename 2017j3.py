a, b = input().split()
c, d = input().split()

charge = int(input())

distance = abs(int(a) - int(c)) + abs(int(b) - int(d))

if (charge - distance) % 2 == 0 and charge >= distance:
    print("Y")
else:
    print("N")