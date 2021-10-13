n = int(input())

digits_sum = 0
digit = 0

while n > 0:
    digit = n % 10
    digits_sum += digit
    n = n // 10

print(digits_sum)