fname = input("Enter file name: ")
fh = open(fname)
List = list()

for line in fh:

    for word in line.split():
        if not word in List:
            List.append(word)

List.sort()
print (List)
