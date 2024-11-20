# travel_log = {
#     "france" : ["paris","llle","marsille"],
#     "germany" : "berlin"
# }

# print(travel_log["france"][1])

# # nested list

# nested_list = ["a","b","c",["a","b"]]
# print(nested_list[3][1])

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])