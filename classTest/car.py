class Car():
    """汽车模拟"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印汽车里程消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """将里程数设置为指定的值，禁止将里程数往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程数增加指定的量"""
        self.odometer_reading += miles


# my_new_car = Car("audi", "a4", 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# # my_new_car.odometer_reading = 18
# my_new_car.update_odometer(18)
# my_new_car.update_odometer(10)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(100)
# my_new_car.read_odometer()
