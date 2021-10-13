# solution 1
n = int(input())

digit_count = 0

while n > 0:
    digit_count += 1
    n = n // 10

print(digit_count)

# solution 2
n = int(input())

digit_count = 0

while n >= 10 ** digit_count:
    digit_count += 1

print(digit_count)