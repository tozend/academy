list_ = list("1234567")


def left_rotate(l, num):
    result = l[num:] + l[:num]
    return result


# Tests:
print(left_rotate(list_, 4))  # should be ["5", "6", "7", "1", "2", "3", "4"]