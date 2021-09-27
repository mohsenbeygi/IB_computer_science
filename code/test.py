# codeforces problem 1567A
t = int(input())

while t:
    length = int(input())
    line = input()
    string = ''
    for i in range(0, length):
        if line[i] == 'D':
            string += 'U'
        elif line[i] == 'U':
            string += 'D'
        elif line[i] == 'L':
            string += 'L'
        elif line[i] == 'R':
            string += 'R'
    t-=1
    print(string)
