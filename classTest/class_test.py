class Dog():
    """模拟小狗的简单测试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗坐下的命令"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗打滚的命令"""
        print(self.name.title() + " rolled over!")


my_dog = Dog("willie", 6)
your_dog = Dog('lucy', 3)


# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")
# my_dog.sit()
#
# print("Your dog's name is " + your_dog.name.title() + ".")
# print("Your dog is " + str(your_dog.age) + " years old.")
# your_dog.roll_over()

# from car import Car
#
# my_new_car = Car('audi', 'a4', 2014)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'C'
favorite_languages['edward'] = 'java'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
