if __name__ == '__main__':
    n, m = map(int, input().split())
    
    #using center function
    for n_patterns in range(1, n, 2):
        print((".|."*n_patterns).center(m, "-"))   
        
    print("WELCOME".center(m,"-"))
    
    for n_patterns in range(n-2, 0, -2):
        print((".|."*n_patterns).center(m, "-"))
        
"""     if(m == 3*n):
        n_patterns = 1
    
        for row in range(n//2):
            print("-"*((m//2 - 1)-(3*row)) + ".|."*n_patterns + "-"*((m//2 - 1)-(3*row)))
            n_patterns += 2
        
        print("-"*((m//2)-3) + "WELCOME" + "-"*((m//2)-3))
        n_patterns -=2
    
        for row in range((n//2-1), -1, -1):
            print("-"*((m//2 - 1)-(3*row)) + ".|."*n_patterns + "-"*((m//2 - 1)-(3*row)))
            n_patterns -= 2
    else:
        print("Incorrect pattern proportion") """
    


        
    