# name = "adA loveLac"
# print(name.title())
# print(name.upper())
# print(name.lower())


# first_name = "ada"
# last_name = "lovelace"
# full_name = first_name + "-" + last_name
# print(full_name)
# print("Hello, " + full_name.title() + "!")

# print("Languages:\nPython\n\tC\tJavaScript")

# word = "大啖食粮之刻已至\n\t\t\t\t——————说客 "
# print(word)

# age = 26
# message = "Happy " + str(age) + " Birthday!"
# print(message)

# array = ['ass', 'we', 'can']
# # print(array)
# # print(array[1])
# # print(array[-1])
# # message = "My first hole was a " + array[0].title() + "."
# # print(message)
# array.append("♂")
# array.insert(1, "♂")
# print(array)
# # del array[4]
# # print(array)
# array1 = array.pop()
# print(array)
# print(array1)

# arr = ['honda', 'yamaha', 'suzuki', 'ducat']
# print(arr)
# arr.remove('ducat')
# print(arr)
# print(len(arr))

# magicians = ['alice', 'david', 'carolina']
# # for magician in magicians:
# #     print(magician.title() + ", that was a great trick!")
# #     print("I can't wait to see your next trick, " + magician.title() + ".\n")
# #
# # print("Thank you, everyone. That was a great magic show!")
#
# for magician in magicians:
#     print(magician.title() + ", that was a great trick!")
# print("I can't wait to see your next trick, " + magician.title() + ".\n")

# range会差一，即range(1, 5)输出的是1到4
# for value in range(1, 5):
#     print(value)

# numbers = list(range(1, 6))
# print(numbers)

# 代表从2开始，一直加2，知道等于或者超过11停止
# even_numbers = list(range(2, 11, 2))
# print(even_numbers)

# 两个星号表示乘方运算
# squares = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# digits = [1, 3, 4, 5, 7, 10, 22, 46]
# print(min(digits))
# print(max(digits))
# print(sum(digits))

# squares = [value ** 2 for value in range(1, 11)]
# print(squares)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# # print(players[0:3])
# # print(players[1:3])
# # print(players[:3])
# # print(players[2:])
# # print(players[-3:])
# # print(players[:-3])
# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())

# my_foods = ['肥肠', '羊杂', '腊肠']
# friend_foods = my_foods[:]
# # 这行不通
# # friend_foods = my_foods
# my_foods.append("猪耳朵")
# friend_foods.append("鸭心")
# print("My favorite foods are: \n" + str(my_foods))
# print("My friend's favorite foods are: \n" + str(friend_foods))

# 不可变的
# dimensions = (200, 50)
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)
#
# dimensions = (233, 666)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)

# cars = ["audi", "bmw", "subaru", "toyota"]
# for car in cars:
#     if car == "bmw":
#         print(car.upper())
#     else:
#         print(car.title())

# age_0 = 22
# age_1 = 18
# print(age_0 >= 21 and age_1 >= 22)
# age_1 = 22
# print(age_0 >= 21 and age_1 >= 22)
#
# print(age_0 >= 21 or age_1 >= 21)
# age_0 = 18
# age_1 = 18
# print(age_0 >= 21 or age_1 >= 21)

# requested_toppings = ['mushrooms', 'onions', 'pineapple']
# print('mushrooms' in requested_toppings)
# print('pepperoni' in requested_toppings)

# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'
#
# if user not in banned_users:
#     print(user.title() + ", you can post a response if you wish.")

# age = 120
# if age < 4:
#     print("You admission cost is $0.")
# elif age < 18:
#     print("You admission cost is $5.")
# else:
#     print("You admission cost is $10.")

# requested_toppings = ['mushrooms', 'extra cheese']
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")
# print("\nFinished making your pizza!")

# available_topping = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping in available_topping:
#         print("Adding " + requested_topping + ".")
#     else:
#         print("Sorry, we don't have " + requested_topping + ".")
#
# print("\nFinished making your pizza!")


# alien_0 = {'color': 'green', 'points': 5}
# # print(alien_0['color'])
# # print(alien_0['points'])
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)
# del alien_0['x_position']
# print(alien_0)

# favorite_languages = {
#     'jem': 'python',
#     'sarah': 'c',
#     'edward': 'java',
#     'phil': 'python',
# }
# print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }
# for key, value in user_0.items():
#     print("\nKey: " + key)
#     print("Value: " + value)
# for name in user_0.keys():
#     print(name.title())

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#     }
# for name in favorite_languages.values():
#     print(name.title())

# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print("Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:5]:
#     print(alien)
# print(".....")
# print("Total number of alien: " + str(len(aliens)))

# message = input("Tell me something, and I will repeat it back to you: \n")
# print(message)

# %是求余数，一个数%2，如果余数为0，则为偶数，否则为奇数
# number = input("Enter a number, and I'll tell you if it's even or odd: \n")
# number = int(number)
# if number % 2 == 0:
#     print("\nThe number "+str(number)+" is even.")
# else:
#     print("\nThe number "+str(number)+" is odd.")

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. \n"
#
# # message = ""
# # while message != 'quit':
# #     message = input(prompt)
# #     if message != 'quit':
# #         print(message)
# active = True
# while active:
#     message = input(prompt)
#     if message == "quit":
#         active = False
#     else:
#         print(message)

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# responses = {}
# # 设置一个标志，指出调查是否继续
# polling_active = True
# while polling_active:
#     # 提示输入被调查者的名字和回答
#     name = input("\nWhat is your name? \n")
#     response = input("Which mountain would you like to climb someday? \n")
#
#     # 将答卷存储在字典中
#     responses[name] = response
#
#     # 看看是否还有人要参与调查
#     repeat = input("Would you like to let another person respond? (yes/ no) \n")
#     while repeat != 'yes' and repeat != 'no':
#         repeat = input("Would you like to let another person respond? (yes/ no) \n")
#     if repeat == 'no':
#         polling_active = False
#
# # 调查结束，显示结果
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(name + " would like to climb " + response + ".")

# def greet_user(username):
#     """简单的问候"""
#     print("Hello, " + username.title() + "!")
# greet_user("ass")

# def describe_pet(pet_name, animal_type='dog'):
#     """显示宠物的信息"""
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#
# describe_pet(pet_name='willie')
# describe_pet(pet_name='willie', animal_type='cat')

# def get_name(first_name, last_name, middle_name):
#     """返回名字"""
#     if middle_name:
#         full_name = first_name + middle_name + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# # name = get_name('ass', 'we can', '♂')
# name = get_name('ass', 'we can', None)
# print(name)

# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名"""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
#
#
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("\nFirst name: ")
#     l_name = input("\nLast name: ")
#     if f_name == 'q':
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

# # 首先创建一个列表，其中包含一些要打印的设计
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
#
# # 模拟打印每个设计，直到没有未打印的设计为止
# # 打印每个设计后，都将其移到列表completed_models中
# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         # 模拟根据设计制作3D打印模型的过程
#         print("Printing model: " + current_design)
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     # 显示打印好的所有模型
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
#
# print_models(unprinted_designs, completed_models)
# # 切片表示法[:]创建列表的副本
# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)


# 形参名*toppings中的星号让Python创建一个名为toppings的空元组，并将收到的所有值都封装到这个元组中
# def make_pizza(*toppings):
#     """打印顾客点的所以配料"""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
#
#
# make_pizza("peperoni")
# make_pizza("mushrooms", "green peppers", "extra cheese")

# 形参必须放在实参后面
# def make_pizza(size, *toppings):
#     """概述要制作的披萨"""
#     print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
#     for topping in toppings:
#         print("- " + topping)
#
#
# make_pizza(16, "peperoni")
# make_pizza(12, "mushrooms", "green peppers", "extra cheese")


# 形参**user_info中的两个星号让Python创建一个名为user_info的空字典，并将收到的所有名称—值对都封装到这个字典中
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile["first_name"] = first
    profile["last_name"] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
