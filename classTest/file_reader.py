# with open('D:\\Downloads\\pi_digits.txt') as file_object:
#     # contents = file_object.read()
#     # print(contents)
#     # # 删除（剥除）字符串末尾的空白
#     # print(contents.rstrip())
#
#     # for line in file_object:
#     #     print(line.rstrip())
#
#     lines = file_object.readlines()
#
# pl_string = ""
# for line in lines:
#     # print(line.rstrip())
#     pl_string += line.strip()
#
# print(pl_string)
# print(len(pl_string))

# 可指定读取模式（'r'）、写入模式（'w'）、附加模式（'a'）或让你能够读取和写入文件的模式（'r+'）。
# 如果你省略了模式实参，Python将以默认的只读模式打开文件
# 如果你要写入的文件不存在，函数open()将自动创建它。然而，以写入（'w'）模式打开文件时千万要小心
# 因为如果指定的文件已经存在，Python将在返回文件对象前清空该文件。
filename = "D:\\Downloads\\write.txt"
# with open(filename, 'w') as file_object:
#     file_object.write("ass♂we♂can\n")
#     file_object.write("do♂it♂again\n")

with open(filename, 'a') as file_object:
    file_object.write("I'm ♂孙红雷♂")
