def calculate_love_score(name1,name2):
    
    add_name = name1+name2
    
    score1 = 0
    score2 = 0
    for letter in add_name:
        if letter == "t" or letter == "T":
            score1 += 1
        if letter == "r" or letter == "R":
            score1 += 1
        if letter == "u" or letter == "U":
            score1 += 1
        if letter == "e" or letter == "E":
            score1 += 1
    

        if letter == "l" or letter == "L":
            score2 += 1
        if letter == "o" or letter == "O":
            score2 += 1
        if letter == "v" or letter == "V":
            score2 += 1
        if letter == "e" or letter == "E":
            score2 += 1

    score = str(score1) + str(score2)
    print(score)
        



calculate_love_score("Kanye West","Kim Kardashian")
