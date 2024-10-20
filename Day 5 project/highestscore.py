student_score = [1,2,3,4,5,6,78,1024,89,234,123,12,99,999,1033]

sum = 0
#finding the max number from a list with max function
print(max(student_score))
#adding the whole number from a list

for n in student_score:
    sum+=n
print(sum)

#find out the highest number without using any function

for number in student_score:
    if number > sum:
        sum = number
        
print(sum)

