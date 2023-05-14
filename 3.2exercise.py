
hrs=input("Enter hours: ")
hours=float(hrs)
rat=input("Enter per hour rate: ")
rate=float(rat)
if hours<=40:
    pay=hours*rate
    Pay=float(pay)
else:
    pay=40*rate+(hours-40)*(rate*1.5)
    Pay=float(pay)


print("The pay is:",Pay)
