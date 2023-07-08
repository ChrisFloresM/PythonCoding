def print_rangoli(size):
    # your code goes here
    init = (96 + size )
    width = (3*size + size-3)
    
    #Top cone
    for row in range(size):
        my_list = [init]
        current_val = init
    
        for n in range(row):
            current_val -= 1
            my_list.append(current_val)
    
        for n in range(row):
            current_val += 1
            my_list.append(current_val)
            
        pattern = "-".join(list(map(chr, my_list)))
        print(pattern.center(width, "-"))
    
    #Bottom cone
    for row in range (size-2, -1, -1):
        my_list = [init]
        current_val = init
    
        for n in range(row):
            current_val -= 1
            my_list.append(current_val)
    
        for n in range(row):
            current_val += 1
            my_list.append(current_val)
            
        pattern = "-".join(list(map(chr, my_list)))
        print(pattern.center(width, "-"))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)