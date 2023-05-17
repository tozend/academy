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
# import string
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


# ----------
# Builtins and FP basics
# ----------

# # Polish Flag
# WHITE_SQUARE = "\u2B1c"
# RED_SQUARE = "\U0001F7E5"
#
# def flag(width=10, height=4):
#     white_part = ((WHITE_SQUARE * width) + '\n') * int(height / 2)
#     red_part = ((RED_SQUARE * width) + '\n') * int(height / 2)
#
#     return white_part + red_part
#
#
# print(flag(width=10, height=4))
# #print(flag(width=2, height=2))


# # Tribonacci
# def tribonacci(length=8, signature=(0, 1, 1)):
#
#     result = list(signature)
#
#     # for i in range(length-3):
#     #     #result.append(result[-1] + result[-2] + result[-3])
#     #     result.append(sum(result[-3:]))
#
#
#     [result.append(sum(result[-3:])) for _ in range(length - 3)]
#     return result
#
#
# print(tribonacci(8, [0,1, 1])) # [0, 1, 1, 2, 4, 7, 13, 24]
# #print(tribonacci([0,0,1]))


#
# # Practice with function arguments
# def gen_mul_table(width=10, height=10, *, sep_width=3, print_header=False, print_footer=True):
#     result = ""
#
#     if print_header:
#         result += f"Multiplication Table {width} x {height}\n"
#
#     for i in range(1, width + 1):
#         for j in range(1, height + 1):
#             result += f'{i * j:{sep_width}}'
#         result += "\n"
#
#     if print_footer:
#         result += '-' * 30
#
#     return result[:-1]
#
#
# #print(gen_mul_table(5, 5))
# print(gen_mul_table(4, 4, print_header=True, sep_width=4, print_footer=True))
# # gen_mul_table(3, 3, 5)


# # Common Topics
# FRIENDS = [
#     ["Python", "Drawing", "Games", "Girls", "Weapons", "Games", "Books"],
#     ["Music", "Politics", "Books", "Girls", "Python", "Cinema", "Cars"],
#     ["Cinema", "Music", "Drawing", "Python", "Books", "History"],
#     ["War", "Sport", "Books", "Games", "Python", "Cinema", "Cars"],
#     ["Knifes", "Games", "Books", "Girls", "Cinema", "Cars", "Python"],
#     ["Sport", "Drawing", "Books", "Girls", "Games", "Music"],
# ]
#
#
# def get_common_topics(friends=FRIENDS, topics=3):
#     topics_rank = dict()
#
#     for friend in friends:
#         for topic in set(friend):
#             topics_rank[topic] = topics_rank.get(topic, 0) + 1
#
#     result = list()
#
#     for _ in range(topics):
#         max_keys = sorted([k for k, v in topics_rank.items() if v == max(topics_rank.values())])
#         result.append(max_keys[0])
#         topics_rank.pop(max_keys[0])
#
#     return result
#
# print(get_common_topics(topics=6))


# #  Simple reversing decorator
# def deco(func):
#     def wrapper(*args):
#         return str(func(*args))[::-1]
#     return wrapper
#
#
# @deco
# def test_me():
#     return True
#
#
# print(test_me())  # "eurT"


# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# say_hello()

#
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         #func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# say_hello()


# def my_deco(func):
#     print("Init...") # We'll see this once
#     return func
#
# @my_deco
# def test1(x):
#     return x
#
# print(test1(25))
# print(test1(48))


# def my_deco(func):
#     def wrapper(*args):
#         wrapper.counter += 1
#         return func(*args)
#
#     wrapper.counter = 0
#     return wrapper
#
#
# @my_deco
# def test1(x):
#     return x
#
#
# print(test1(25), test1(48), test1(55))
# print(test1(1))
# print(test1.counter)
# print(test1(1))
# print(test1.counter)


# def makebold(fn):
#     def wrapped(*args, **kwargs):
#         return "<b>" + str(fn(*args, **kwargs)) + "</b>"
#     return wrapped
#
# def makeitalic(fn):
#     def wrapped(*args, **kwargs):
#         return "<i>" + str(fn(*args, **kwargs)) + "</i>"
#     return wrapped
#
# def makered(fn):
#     def wrapped(*args, **kwargs):
#         return "<span style='color: red;'>" + str(fn(*args, **kwargs)) + "</span>"
#     return wrapped
#
# @makebold
# @makeitalic
# @makered
# def hello(text="Goodbye World!"):
#     return text
#
# #hello = makebold(makeitalic(makered(hello)))
#
# print(hello())


# #  Only Evens
# def get_only_evens(list_: list) -> list:
#     # result = []
#     # for count, element in enumerate(list_):
#     #     if (element % 2 == 0) and (count % 2 == 0):
#     #         result.append(element)
#
#     result = [element for count, element in enumerate(list_) if (element % 2 == 0) and (count % 2 == 0)]
#     return result
#
# print(get_only_evens([1, 3, 2, 6, 4, 8]))


# # Unused Digits
#
# # #-Old solution
# # def unused_digits(*args):
# #     digits_left = [str(x) for x in range(10)]
# #     digits_to_check = "".join([str(x) for x in args])
# #
# #     for char in digits_to_check:
# #         if char in digits_left:
# #             digits_left.remove(char)
# #
# #     result = ''.join(digits_left)
# #     return result
#
# def unused_digits(*args):
#     possible_digits = {str(x) for x in range(10)}
#     digits_to_check = set("".join([str(x) for x in args]))
#
#     result = "".join(sorted(possible_digits - digits_to_check))
#     return result
#
#
# print(unused_digits(12, 34, 56, 78))  # "09"
# print(unused_digits(2015, 8, 26))  # "3479"


# # Rabbits and chickens
# def count_rabbits_chickens(heads, legs):
#     rabbits = 0
#
#     for _ in range(heads):
#         chickens = 0
#         for _ in range(heads):
#             if (chickens + rabbits == heads) and (rabbits * 4 + chickens * 2 == legs):
#                 return rabbits, chickens
#             chickens += 1
#         rabbits += 1
#
#     return "Not possible"
#
#
# print(count_rabbits_chickens(3, 10))  # 2, 1


# # Shipping Cost
# from typing import List, Tuple
#
# shipping_rates = {
#     'New York': 250.0,
#     'Los Angeles': 300.0,
#     'Seattle': 200.0,
#     'Houston': 275.0
# }
#
#
# def total_cost_to_port(cargo: List[Tuple[str, float, str]], port: str) -> float:
#     """The function calculates the total shipping cost
#     for all items that are being shipped to that specific port.
#     """
#     if port not in shipping_rates:
#         return 0.0
#
#     # total_cost = 0.0
#     #
#     # for item in cargo:
#     #     if item[2] == port:
#     #         total_cost += item[1] * shipping_rates[port]
#
#     total_cost = sum(item[1] * shipping_rates[port] for item in cargo if item[2] == port)
#     return total_cost
#     #albo jako totalny oneliner:
#     #return sum(item[1] * shipping_rates[port] for item in cargo if item[2] == port) if port in shipping_rates else 0.0
#
#
# #print(total_cost_to_port([("Apples", 5.0, "New York"), ("Oranges", 3.0, "Los Angeles"), ("Bananas", 2.5, "Seattle"), ("Pineapples", 4.0, "Houston")], "Los Angeles")) #     900.0)
# print(total_cost_to_port([("Apples", 5.0, "New York"), ("Apples", 10.0, "New York")], "New York")) #     900.0)


# ----------
# Practice / HomeTasks review session #2
# ----------


# # Obfuscator of duplicates
# test_string = "Hello, my password is: 'AaaBBBccc', cooool, right?"
# expected_result = "Hello, my password is: '*********', c***ol, right?"
#
#
# def test_me(test_string):
#     result = ''
#
#     for i in range(len(test_string)):
#         if test_string.lower()[i] == test_string.lower()[i-1] == test_string.lower()[i-2] and result[i-1] != '*':
#             result = result[:-2] + '***'
#             continue
#         result += test_string[i]
#
#     return result
#
#
# if test_me(test_string) == expected_result:
#     print("You did well: %s" % expected_result)
# else:
#     print("You got:\n%s\nTry again..." % test_me(test_string))


# # Find longest palindrome
#
# def isPalindrome(s):
#     return s == s[::-1]
#
# def get_longest_palindrome(s):
#     palindromes = []
#
#     for i in range(len(s)):
#         for j in range(i + 1, len(s) + 1):
#             word = s[i:j]
#             if isPalindrome(word):
#                 palindromes.append(word)
#
#     return max(palindromes, key=len)
#
# #print(get_longest_palindrome("AbA121"))  # Aba
# #print(get_longest_palindrome("AbAtopot123321"))  # 123321
# print(get_longest_palindrome("hohoho"))


# # ----------
# # Code Style, modules/packages
# # ----------
#
#
# # Merging logs
# list1 = [
#     {"id": "3456", "message": "Service started OK", "datetime": 1474624881},
#     {"id": "123124", "message": "DB stopped! Whatta hell!", "datetime": 1474456391},
#     {"id": "12353", "message": "MQ broker is not brokering!", "datetime": 1474624591},
#     {"id": "1223134", "message": "U hev bin pwned by hax0r tim!", "datetime": 1474624799},
#     {"id": "1213234", "message": "Need more vespene gas!", "datetime": 1474624791},
# ]
#
# list2 = [
#     {"id": "3456", "message": "Service started OK", "datetime": 1474624881},
#     {"id": "12353", "message": "MQ broker is not brokering!", "datetime": 1474624591},
#     {"id": "3334113", "message": ""'; DELETE FROM customers WHERE 1 or username = '"; ", "datetime": 1474624789},
#     {"id": "1213235", "message": "Require more minerals!", "datetime": 1474624792},
# ]
#
#
# def merge_logs(list1, list2):
#     # merged_logs = {log['id']: log for log in list1 + list2} # {'3456': {'id': '3456', 'message': 'Service started OK', 'datetime': 1474624881}, '123124': {'id': '123124', 'message': 'DB stopped! Whatta hell!', 'datetime': 1474456391}
#     # merged_logs = list(merged_logs.values())
#
#     merged_logs = list({log['id']: log for log in list1 + list2}.values())
#     sorted_logs = sorted(merged_logs, key=lambda k: k['datetime'])
#     return sorted_logs
#
# print(merge_logs(list1, list2))


# ----------
# OOP #1
# ----------


# # Farm Simulator
# class NonNegative:
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError('Cannot be negative')
#         instance.__dict__[self.name] = value
#
#     def __set_name__(self, owner, name):
#         self.name = name
#
#
# class Farm:
#     square = NonNegative()
#     sheep = NonNegative()
#     chickens = NonNegative()
#     cows = NonNegative()
#
#     price_sheep = 500
#     price_cow = 1000
#     price_chicken = 50
#     price_square = 700
#
#     def __str__(self):
#         return f'Farm "{self.name}", sq: {self.square} ha, value: ${self.get_value()}'
#
#     # This is currently incomplete:
#     def __init__(self, name, square, sheep, cows, chickens):
#         self.name = name
#         self.square = square
#         self.sheep = sheep
#         self.cows = cows
#         self.chickens = chickens
#
#     def get_value(self):
#         "Return money value of the farm"
#         result = (self.square * self.price_square) + (self.sheep * self.price_sheep) +\
#                  (self.cows * self.price_cow) + (self.chickens * self.price_chicken)
#         return result
#
#     def __eq__(self, other):
#         "Return True/False if value of SELF is equal to the value of OTHER"
#         return self.get_value() == other.get_value()
#
#     def __gt__(self, other):
#         "Return True/False if value of SEL is greater than the value of OTHER"
#         return self.get_value() > other.get_value()
#
#
# # Simple Test
# farm1 = Farm("My First Farm", 400, 10, 10, 10)
# farm2 = Farm("My Second Farm", 300, 40, 30, 20)
#
# print(farm1)
# print(farm2)
# print(farm1 > farm2)



# # OOP practice
# class Animal:
#     "Sample class - feel free to rename, add any attrs/methods you like"
#
#     def __init__(self, name, kind, color):
#         self.name = name
#         self.kind = kind
#         self.color = color
#
#         self.hungry_counter = 1
#
#     def hello(self):
#         return f'🐵 Animal desciption 🐵\nName: {self.name}\nKind: {self.kind}\nColor: {self.color}'
#
#     def trick(self):
#         match self.kind:
#             case 'dog':
#                 self._increase_hungry_level()
#                 return 'Bark!' if self.hungry_counter < 4 else 'Feed me'
#             case 'cat':
#                 self._increase_hungry_level()
#                 return 'Meow!' if self.hungry_counter < 4 else 'Feed me'
#             case _:
#                 self._increase_hungry_level()
#                 return 'Other trick' if self.hungry_counter < 4 else 'Feed me'
#
#     def _increase_hungry_level(self):
#         self.hungry_counter += 1
#
#     def feed(self):
#         self.hungry_counter = 0
#         return 'Thanks for feed!'
#
#
#
#
# zhuchka = Animal("Zhuchka", "dog", "brown")
# print(zhuchka.hello())
# print(zhuchka.trick())
# print(zhuchka.feed())
# print(zhuchka.trick())
# print(zhuchka.trick())
# print(zhuchka.trick())
# print(zhuchka.trick())
# print(zhuchka.trick())
# print(zhuchka.feed())










# ----------
# OOP #2
# ----------

# # Dice
# # The following three constant definitions are equal.
# # But the first(which looks the best) doesn't work
# #   in CodeRunner
# # DICES = "⚀⚁⚂⚃⚄⚅"
# # DICES = "\N{DIE FACE-1}\N{DIE FACE-2}\N{DIE FACE-3}" \
# #        "\N{DIE FACE-4}\N{DIE FACE-5}\N{DIE FACE-6}"
# import random
#
#
# DICES = "\u2680\u2681\u2682\u2683\u2684\u2685"
#
#
# def dice(number=1):
#     # result = []
#     # for _ in range(number):
#     #     result.append(DICES[random.randint(0, len(DICES) - 1)])
#     result = [DICES[random.randint(0, len(DICES) - 1)] for _ in range(number)]
#     return ' '.join(result)
#
#
# # Some basic tests
# print(f'All dices are: {DICES}')
# print(dice())  # Should be some dice outputted
# print(dice(3))  # Should be 3 dice outputted
# print(dice(3).count(" ") == 2 and len(dice(3)) == 5)  # Should be True
# print(all(x in DICES for x in dice(3).replace(" ", "")))  # Should be True




# # Deck of cards
# import random
#
#
# class Card:
#     suit = ''
#     value = ''
#
#     def __init__(self, suit='Spade', value='Q'):
#         self.suit = suit
#         self.value = value
#
#     def __str__(self):
#         return f"[{self.suit} {self.value}]"
#
#     def __repr__(self):
#         return f"[{self.suit} {self.value}]"
#
#
# class Deck:
#     AVAILABLE_SUITS = ('♠', '♥', '♦', '♣')
#     AVAILABLE_VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
#
#     def __init__(self):
#         # self.cards = []
#         #
#         # for suit in self.AVAILABLE_SUITS:
#         #     for value in self.AVAILABLE_VALUES:
#         #         self.cards.append(Card(suit, value))
#         self.cards = [Card(suit, value) for suit in self.AVAILABLE_SUITS for value in self.AVAILABLE_VALUES]
#
#     def shuffle(self):
#         random.shuffle(self.cards)
#
#     def pop(self, num=-1):
#         return self.cards[num]
#
#     def random(self):
#         return random.choice(self.cards)
#
#     # def index(self, suit, value):
#     # result = self.cards.index(Card(suit, value))
#     # return result
#
#     # for count, element in enumerate(self.cards):
#     #     if element == Card(suit, value):
#     #         return count
#
#     def __repr__(self):
#         return self.cards
#
#
# def run_some_tests():
#     "Define a deck and run some tests!"
#
#     deck = Deck()
#     print(deck.pop())
#     deck.shuffle()
#     print(deck.pop())
#     print(deck.pop(23))
#     print([str(deck.random()) for i in range(5)])
#     # print(deck.index('♠', '7'))
#
#
# run_some_tests()
