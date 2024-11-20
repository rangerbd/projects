# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# # - Scores 91 - 100: Grade = "Outstanding" 

# # - Scores 81 - 90: Grade = "Exceeds Expectations" 

# # - Scores 71 - 80: Grade = "Acceptable" 

# # - Scores 70 or lower: Grade = "Fail" 

# for items in student_scores:

#     if student_scores[items] >= 91 :
#         student_scores[items] = "outstanding"
#     elif student_scores[items] >= 81 and student_scores[items] <= 90:
#         student_scores[items] = "Exceeds Expectation"
#     elif student_scores[items] >= 71 and student_scores[items] <= 80:
#         student_scores[items] = "Acceptable"
#     elif student_scores[items] <= 70 :
#         student_scores[items] = "Fail"

# print(student_scores)

dictionaries = {
    "dipto" : 123,
    "fff" : 333,
    "ggg" : 100,
}

highest_score = 0
for letter in dictionaries:
    score = 0
    if dictionaries[letter] > score:
        score += dictionaries[letter]
        if score > highest_score:
            highest_score = score
print(letter)