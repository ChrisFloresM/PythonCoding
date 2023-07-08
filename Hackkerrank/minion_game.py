def minion_game(string):
    # your code goes here
    stuart_score = 0
    kevin_score = 0
    vowels = "AEIOU"

    for i in range(len(string)):
        if string[i] in 'AEIOU':
            kevin_score += len(string) - i
            print(f"The kevin score is: {kevin_score} on iteration {i}")
        else:
            stuart_score += len(string) - i
            print(f"The Stuart score is: {stuart_score} on iteration {i}")
    
    if(kevin_score > stuart_score):
        print("Kevin", kevin_score)
        
    elif(stuart_score > kevin_score):
        print("Stuart", stuart_score)
    else:
        print("Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)