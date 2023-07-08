def swap_case(s):
    swapped_s = ""
    for letter in s:
        if (letter.islower()):
            swapped_s += (letter.upper())
        else:
            swapped_s += (letter.lower())
    return swapped_s


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
