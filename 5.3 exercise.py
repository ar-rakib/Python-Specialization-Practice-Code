largest=None
smallest=None

while True:
    try:
        num=input('Enter the number:')
        if num=='done':
            break
        value=int(num)
        if largest is None or value>largest:
            largest=value
        elif smallest is None or value<smallest:
                smallest=value

    except:
        print('Invalid input')
        continue


print('Maximum number',largest)
print('Minimum number',smallest)
