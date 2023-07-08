if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    def print_numbers(i, j, k):
        if ((i == x) and (j == y) and (k == z)):
            print(f"[{i}, {j}, {k}]", end='')
        else:
            print(f"[{i}, {j}, {k}]", end=', ')

    print("[", end='')

    [print_numbers(i, j, k) for i in range(x+1)
     for j in range(y+1) for k in range(z+1) if (i+j+k != n)]

    print("]", end='')
