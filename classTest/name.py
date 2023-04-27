import unittest

from name_function import get_formatted_name


# print("Enter 'q' at any time to quit.")
# while True:
#     first = input("Please give me a first name: \n")
#     if first == "q":
#         break
#     last = input("Please give me a last name: \n")
#     if last == "q":
#         break
#
#     formatted_name = get_formatted_name(first, last)
#     print("\nNeatly formatted name: " + formatted_name + ".")


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确处理Janis Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name("janis", None, "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_last_middle_name(self):
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()
