dictionaries = {
    "a" : "this is the first one",
    "b" : "this is the second one",
    "c" : "this is the third one",
}

# print(dictionaries)

#clearing the existing dictionary

# dictionaries = {}

# print(dictionaries)

#editing a dictionary

dictionaries["a"] = "this is the edited version"

# print(dictionaries)

#loop through the dictionary

# for items in dictionaries:
#     print(items)

for key in dictionaries:
    print(f"{key} : {dictionaries[key]}")
    
