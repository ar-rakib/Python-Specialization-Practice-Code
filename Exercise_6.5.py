text = "X-DSPAM-Confidence:    0.8475"
pos1 = text.find('0')

pos2 = text.find('5')


slice = text[pos1:pos2+1]
num=float(slice)
print(num)
