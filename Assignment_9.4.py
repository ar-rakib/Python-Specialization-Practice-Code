#most mail sender and how many times send count

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dictionary = dict()


for line in handle:
    line_split = line.split()
    if 'From' in line_split:
        email = line_split[1]
        dictionary[email]=dictionary.get(email,0)+1


count=0
mail_id = None
mail_count = None

for key,value in dictionary.items():
    if value > count:
        count = value
        mail_id = key
        mail_count = value

print(mail_id , mail_count)
