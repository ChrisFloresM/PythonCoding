def print_formatted(number):
    # your code goes here
    n_adjust = len(bin(number)[2:])
    for n in range(1, number+1):    
        print(f"{n}".rjust(n_adjust),f"{n:o}".rjust(n_adjust),f"{n:X}".rjust(n_adjust),f"{n:b}".rjust(n_adjust))
        
""" def print_formatted(number):
    width = len((bin(number))[2:])
    for i in range(1,number+1):
        dec = str(i)
        octal = (oct(i))[2:]
        hexa = ((hex(i))[2:]).upper()
        binary = (bin(i))[2:]
        print(dec.rjust(width),octal.rjust(width),hexa.rjust(width),binary.rjust(width)) """

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)