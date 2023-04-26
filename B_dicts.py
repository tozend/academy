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
import string
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


# # Pirate frequency
# from typing import List
#
#
# def pirate_frequency(input_string: str, threshold: int) -> List[str]:
#     """
#     Returns a list of letters that appear more than a certain
#     number of times in a given string.
#     """
#     char_frequency = {}
#     for char in input_string.lower():
#         if char in string.ascii_letters:
#             char_frequency[char] = char_frequency.setdefault(char, 0) + 1
#
#     # result = []
#     # for letter, frequency in char_frequency.items():
#     #     if frequency > threshold:
#     #         result.append(letter)
#
#     result = [letter for letter, frequency in char_frequency.items() if frequency > threshold]
#     return sorted(result)
#
#
# # print(pirate_frequency("Ahoy, matey!", 1))  # ['a', 'e', 'o', 'y'])
# # print(pirate_frequency("Dead men tell no tales.", 3)) # ["e"]
# # print(pirate_frequency("Thar she blows!", 3)) # []
# print(pirate_frequency("Avast, ye landlubbers!", 1))  # → ['a', 's', 'e', 'l', 'b'])




#
# # Bird Sightings
# from typing import List, Tuple, Dict
#
#
# def analyze_birds(sightings: List[Tuple[str, str]]) -> Dict[str, str]:
#     """
#     Returns a dictionary that maps each color to the most commonly observed bird species of that color.
#     If there are multiple species that are equally common for a given color, returns any one of those species.
#     """
#     result = {}
#     for bird, color in sightings:
#         result[color] = result.setdefault(color, bird)
#
#     return result
#
#
# # Should return: {'red': 'Robin', 'brown': 'Sparrow', 'blue': 'Blue Jay'})
# # print(analyze_birds(
# #     [("Robin", "red"), ("Sparrow", "brown"), ("Robin", "brown"), ("Blue Jay", "blue"), ("Sparrow", "brown"),
# #      ("Blue Jay", "blue"), ("Sparrow", "blue"), ("Sparrow", "brown")]))
#
# print(analyze_birds([("Robin", "red"), ("Sparrow", "brown"), ("Robin", "brown"), ("Blue Jay", "blue"), ("Sparrow", "brown"), ("Blue Jay", "blue"), ("Sparrow", "blue"), ("Sparrow", "brown")]))
#
#









# ----------
# Collections, Functions
# ----------



# #  Recursive function
# list_ = [1, [2, [3], 4]] # 10
# list_ = [[[[1, 4, 5], [[6, 9], [[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]
#
#
# def rec_func(list_):
#     result = 0
#
#     for element in list_:
#         if type(element) is int:
#             result += element
#         elif type(element) is list:
#             result += rec_func(element)
#
#     return result
#
#
# print(rec_func(list_))





# #  DJ helper tool
# songs_db = [{
#     'artist': 'Led Zeppelin',
#     'title': 'Stairways to heaven',
#     'playback': '09:20'
# }, {
#     'artist': 'Metallica',
#     'title': 'Master of puppets',
#     'playback': '04:30'
# }, {
#     'artist': 'Nirvana',
#     'title': 'The Man who sold the world',
#     'playback': '03:10'
# }, {
#     'artist': 'Stepan Galyabarda',
#     'title': 'Lyst do mamy',
#     'playback': '02:20'
# }]
#
#
# def _min_to_sec(time_in_minutes: str):
#     separator_index = time_in_minutes.index(':')
#     time_in_sec = int(time_in_minutes[:separator_index]) * 60 + int(time_in_minutes[separator_index + 1:])
#     return time_in_sec
#
#
# def get_song(db, len_seconds):
#     max_allowed_playback_time = 0
#     artist, title = "", ""
#
#     for song in songs_db:
#         if (_min_to_sec(song['playback']) <= len_seconds) and (
#                 _min_to_sec(song['playback']) >= max_allowed_playback_time):
#             max_allowed_playback_time = _min_to_sec(song['playback'])
#             artist, title = song['artist'], song['title']
#
#     if not max_allowed_playback_time:
#         return False
#
#     return "Best possible song: {}/{}".format(artist, title)
#
#
# print(get_song(songs_db, 145))
# print(get_song(songs_db, 645))






# #  Resources Check
# from typing import List, Tuple
# from enum import Enum
#
# storage = {
#     'wood': 100,
#     'stone': 50,
#     'bricks': 200,
#     'glass': 30
# }
#
#
# def has_enough_resources(required_resources: List[Tuple[str, int]]) -> bool:
#     for element in required_resources:
#         if (element[0] not in storage.keys()) or (element[1] > storage[element[0]]):
#             break
#     else:
#         return True
#
#     return False
#
#
# print(has_enough_resources([("iron", 50), ("stone", 20), ("bricks", 100), ("glass", 20)]))  # True
# print(has_enough_resources([("wood", 50), ("stone", 20), ("bricks", 100), ("glass", 20)]))  # True
# print(has_enough_resources([("wood", 150), ("stone", 20), ("bricks", 50), ("glass", 20)]))  # False