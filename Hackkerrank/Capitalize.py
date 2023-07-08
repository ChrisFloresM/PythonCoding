#Capitalize a string name

def solve(s):
    for name in s.split():
        if name.isalpha():
            s = s.replace(name, name.capitalize())
    return s

print(solve("1 w 2 r 3g"))