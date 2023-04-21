# # GCD
# def get_divisors(number):
#     divisors = {1}
#
#     for i in range(1, number):
#         if number % i == 0:
#             divisors.add(i)
#
#     return divisors
#
#
# def gcd(x, y):
#     result = max(get_divisors(x) & get_divisors(y))
#     return result
#
#
# print(gcd(8, 12))
# print(gcd(54, 24))


# # Give me numbers!
# def test_me(x=333, y=7553):
#     result = []
#
#     for i in range(333, 7554):
#         if (i % 7 == 0) and (i % 13 == 0) and (i % 5 != 0):
#             result.append(i)
#
#     return result
#
#
# print(test_me())





# # Balanced List
# def gen_list(num=3):
#     result = [i for i in range(0, num - 1)]
#     result.append(- sum(result))
#     return result
#
#
# print(gen_list(5))




# # Narcissistic Number
# def narcissistic(test_number):
#     number_of_digits = int(len(str(test_number)))
#     sum_of_powers = 0
#
#     for char in str(test_number):
#         sum_of_powers += int(char) ** number_of_digits
#
#     if sum_of_powers == test_number:
#         return True
#
#     return False
#
#
# print(narcissistic(7))  # True
# print(narcissistic(371))  # True
# print(narcissistic(122))  # False
# print(narcissistic(4887))  # False




# # Group Anagrams
# test_list = ["tsar", "rat", "tar", "star", "tars", "cheese"]
#
#
# def is_anagram(str1, str2):
#     str1 = sorted(list(str1.lower()))
#     str2 = sorted(list(str2.lower()))
#     return str1 == str2
#
#
# def group_anagrams(test_list):
#     anagrams = {}
#
#     for element in test_list:
#         list_ = [test_list[i] for i in range(len(test_list)) if is_anagram(element, test_list[i])]
#         if element not in str(anagrams.values()):
#             anagrams[element] = list_
#
#     result = [value for value in anagrams.values()]
#     return result
#
#
# print(group_anagrams(test_list))
