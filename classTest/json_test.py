import json

# numbers = [2, 3, 4, 8, 15, 33]

# filename = "numbers.json"
# with open(filename, 'w') as file_object:
#     json.dump(numbers, file_object)
# with open(filename) as file:
#     numbers = json.load(file)
#
# print(numbers)


# user_name = input("What is your name? ")
file_name = "user_name.json"
# with open(file_name, 'w') as file:
#     json.dump(user_name, file)
#     print("We'll remember you when you come back, " + user_name + "!")
with open(file_name) as file:
    user_name = json.load(file)
    print("Welcome back, " + user_name + "!")
