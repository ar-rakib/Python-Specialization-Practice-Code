def computepay(h,r):

    if h>40:
        p = 1.5 * r * (h - 40) + (40 *r)
        return p
    else:
            p = h*r
            return p

hrs = input("Enter Hours:")
hours=float(hrs)
rt=input("Enter rate:")
rate=float(rt)
P = computepay(hours,rate)
print("Pay", P)
