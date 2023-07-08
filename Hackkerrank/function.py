def is_leap(year):
    leap = False

    # Write your logic here

    # El año es divisible entre 4, no es divisible entre 100, si es divisible entre 400
    if ((year % 4 == 0) and ((year % 400 == 0) or (year % 100 != 0))):
        leap = True

    return leap


year = int(input())
print(is_leap(year))
