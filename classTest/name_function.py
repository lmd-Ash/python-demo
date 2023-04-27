def get_formatted_name(first, middle, last):
    """返回整洁的名字"""
    if middle:
        full_name = first + " " + middle + " " + last
    else:
        full_name = first + " " + last
    return full_name.title()

# def get_formatted_name(first, last):
#     """返回整洁的名字"""
#     full_name = first + " " + last
#     return full_name.title()
