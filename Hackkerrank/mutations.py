""" string = "abecedario"
string = list(string)
string[5] = "f"
string = "".join(string)
print(string) """
""" 
string = "abecedario"
string = string[:5] + "f" + string[6:]
print(string) """


def mutate_string(string, position, character):
    # opcion 1:
    # s = string[:position] + character + string[position+1:]

    # Opcion 2:
    s = list(string)
    s[position] = character
    return "".join(s)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
