#
# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last
#

def print_full_name(first, last):
    # Write your code here
    printing_string = "Hello You just delved into Python"

    string_list = printing_string.split(" ")
    string_list.insert(1, first)
    string_list.insert(2, last + "!")

    print(" ".join(string_list))


"""     print("Hello " + first + " " + last + "! You just delved into Python") """


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
