fname = input('input the file: ')

try:
    fhand= open(fname)
except:
    print('the file is not in the list')
    exit()

count=dict()
print(count)

for line in fhand:
    words=line.split()
    print(words)
    print()
    for line in words:
        if line not in count:
            count[line]=1

        else:
            count[line] += 1


print(count)
