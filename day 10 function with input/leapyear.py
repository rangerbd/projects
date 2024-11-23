def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("this is a leapyear")
            else:
                print("this is not a leapyear")
        else:
            print("this is not a leapyear")        
    else:
        print("this is not a leapyear")

is_leap_year(2100)