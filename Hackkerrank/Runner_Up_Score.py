if __name__ == '__main__':
    n = int(input())
    # Map: function that works as an iterator to return a result after applying a function to every item of an iterable (tuple, lists, etc.)
    arr = map(int, input().split())

    my_list = list(arr)

    for i in range(my_list.count(max(my_list))):
        my_list.remove(max(my_list))

    print(max(my_list))
