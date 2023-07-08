import textwrap

def wrap(string, max_width):
    wrapped_string = []
    for l in range(0, len(string), max_width):
        wrapped_string.append(string[l:max_width+l])
    wrapped_string = "\n".join(wrapped_string)
    return wrapped_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)