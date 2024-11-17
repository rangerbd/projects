def calculate_love_score(name1,name2):
    score = 0
    add_name =name1+name2
    def score_checker(title1):
        global score
        true = 0
        love = 0
        for letter in add_name:
            if letter == title1:
                true += 1
                score += true
                print(score)
                
    score_checker("t")
    score_checker("r")
    score_checker("u")
    score_checker("e")


calculate_love_score("Kanye West","Kim Kardashian")
