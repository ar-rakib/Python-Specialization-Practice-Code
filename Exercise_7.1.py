fname = input("enter a file name: ")
fh = open(fname)

text = fh.read()
text = text.upper()
text = text.rstrip()
print(text)
