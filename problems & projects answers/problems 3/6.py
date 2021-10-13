n = int(input())

maximum = int(input())

for i in range(1, n):
    number = int(input())
    if number > maximum:
        maximum = number

print(maximum)