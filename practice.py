import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

hint_1 = random.choice(friends)
print(hint_1)

hint_2 = random.randint(0,4)
print(friends[hint_2])
