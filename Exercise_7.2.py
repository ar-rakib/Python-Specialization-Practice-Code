fname = input("Enter file name: ")
fh = open(fname)
count = 0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue




    else:
        count=count+1
        num=line.find('0')
        floatnum=float(line[num:])
        total=total+floatnum

avearge=total/count
print('co',avearge)
