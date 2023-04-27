# 导入pizza.py文件
# import pizza
# pizza.make_pizza(18, 'pepperoni')

# from 文件名 import 方法名/类名

# # 导入特定的函数
# from pizza import make_pizza
#
# make_pizza(18, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# # 导入特定的函数并指定别名
# from pizza import make_pizza as mp
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# 导入模块的所有函数
from pizza import *
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')