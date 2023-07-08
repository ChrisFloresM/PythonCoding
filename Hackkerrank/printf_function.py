if __name__ == '__main__':

    # first solution
    n = int(input())

    for i in range(1, n + 1):
        print(i, end='')

    text = ""

# An alternative
    for i in range(1, n+1):
        text += str(i)
    print(text)

print("\nHello world! ", end="This ends here!")
