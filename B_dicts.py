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


# ----------
# Practice / HomeTasks review session #1
# ----------


# # Palindrome detection
# import re
#
# def is_palindrome(s):
#     s = ''.join(re.findall('[^ !.,?]+', s)).lower()
#     unpaired_chars = s
#
#     for i, char in enumerate(s):
#         if char == s[-i-1]:
#             unpaired_chars = unpaired_chars.replace(char, '', 1)
#
#     return not unpaired_chars
#
#
# print(is_palindrome("racecar"))  # True
# print(is_palindrome("Race Car"))  # True
# print(is_palindrome("A man, a plan, a canal, Panama!"))  # True





# # Dictionary KV swapper
# data = {"key1": 25, 100: "value100", "cadabra": "abra", (1, 2): (3, 4), "shmobject": object, False: None}
#
#
# def dict_swap(data):
#     # result = {}
#     # for key, value in data.items():
#     #     if value.__hash__:
#     #         result[value] = key
#
#     result = {value: key for key, value in data.items() if value.__hash__}
#     return result
#
# print(dict_swap(data))
# # Advanced task (#2 in tests):
# tricky_data = {"cadabra": "abra", (1, 2): [3, 4], "oops": {}}
# print(dict_swap(tricky_data))






# # Sum of digits in a string
#
# def sum_digits(input_str: str) -> int:
#     # result = 0
#     # for char in input_str:
#     #     if str.isdecimal(char):
#     #         result += int(char)
#
#     #result = sum([int(char) for char in input_str if str.isdecimal(char)])
#     return sum([int(char) for char in input_str if str.isdecimal(char)])
#
#
# # Small tests
# print(sum_digits("abc123___##05__5"))  # 16
# print(sum_digits("00000000000"))  # 0
# print(sum_digits("@@@@@@-1.0####"))  # 1
# print(sum_digits("100____½"))  # 1





# Pirate frequency
from typing import List


def pirate_frequency(string: str, threshold: int) -> List[str]:
    """
    Returns a list of letters that appear more than a certain
    number of times in a given string.
    """

    return []


print(pirate_frequency("Ahoy, matey!", 1))  # ['a', 'e', 'o', 'y'])
