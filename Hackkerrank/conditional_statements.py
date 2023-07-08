
# My solution
""" n = int(input().strip())

if (n % 2 != 0):
    print("Weird")
else:
    if ((n >= 2) and (n <= 5)):
        print("Not Weird")
    elif ((n >= 6) and (n <= 20)):
        print("Weird")
    elif ((n > 20)):
        print("Not Weird") """

# Other solution
n = int(input().strip())

if (n % 2 != 0):
    print("Weird")
else:
    if (n in range(2, 6)):
        print("Not Weird")
    elif (n in range(6, 21)):
        print("Weird")
    elif (n > 20):
        print("Not Weird")
