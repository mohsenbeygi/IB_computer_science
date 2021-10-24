n = int(input())

element_1 = 1
element_2 = 1
for i in range(1, n):
    element_2 += element_1
    element_1 = element_2 - element_1

print(element_1)
