""" 

Métodos para validación de strings

str.isalnum(): Verifica si todos los elementos son alfanumericos
str.isalpha(): Verifica si todos los elementos de un string son alfabeticos
str.isdigit(): Verifica si todos los elementos de un string son digitos
str.islower(): verifica si todos los elementos de un string estan en minusculas
str.isupper(): verifica si todos los elementos de un string estan en mayusculas

"""
""" 
TODO:
First line: Alphanumeric
Second line: Alphabetical
Third line: Digits
Fourth line: lowercase
Fifth line: Uppercase

"""

if __name__ == '__main__':
    s = input()
    print(any([l.isalnum() for l in s]))
    print(any([l.isalpha() for l in s]))
    print(any([l.isdigit() for l in s]))
    print(any([l.islower() for l in s]))
    print(any([l.isupper() for l in s]))
