""" insert(i, e): Insert integer e at position i
    print: Print the list.
    remove(e): Delete the first occurrence of integer
    append(e): Insert integer at the end of the list.
    sort: Sort the list.
    pop: Pop the last element from the list.
    reverse: Reverse the list. """

if __name__ == '__main__':
    N = int(input())

command_list = []
my_list = []

for i in range(N):
    command_list.append(input().split())

    if command_list[i][0] == "insert":
        my_list.insert(int(command_list[i][1]), int(command_list[i][2]))

    elif command_list[i][0] == "print":
        print(my_list)

    elif command_list[i][0] == "remove":
        my_list.remove(int(command_list[i][1]))

    elif command_list[i][0] == "append":
        my_list.append(int(command_list[i][1]))

    elif command_list[i][0] == "sort":
        my_list.sort()

    elif command_list[i][0] == "pop":
        my_list.pop()

    elif command_list[i][0] == "reverse":
        my_list.reverse()
