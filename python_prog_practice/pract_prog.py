'''1. Write a program to find the length of the string without using inbuilt function (len)'''

# string_ = "hello"
# count = 0
# for char in string_:
#     count += 1
# print(count)

'''2. Write a program to reverse a string without using any inbuilt functions.'''

# def _rev(s):
#     rev = ""
#     for char in s:
#         rev = char + rev
#     return rev
# print(_rev("hello"))

# def _rev(s): #hello
# #     if len(s) == 1:
# #         return s
# #     return s+_rev(s[-1])
# #
# # print(_rev("hello"))

# def _rev(s, res=""): #hello
#     if len(s) != 0:
#         res = res+ s[-1]
#         _rev(s[:-1], res)
#     return res
#
# print(_rev("hello"))

# def _rev(s):
#     return s[::-1]
#
# print(_rev("hello"))

'''3. Write a program to replace one string with another. e.g. "Hello World" replace "World" with "Universe".'''

# s = "Hello World"
# print(s.replace("World","universe"))

'''4. How to convert a string to a list and vice-versa.'''

# s = "Hello World"
# l = list(s)
# l1 = s.split()
# s1 = "".join(l)
# s2 = " ".join(l1)
# print(l1)
# print(l)
# print(s1)
# print(s2)

'''5. Covert the string "Hello welcome to Python" to a comma separated string.'''
# s = "Hello welcome to Python"
# print(s.replace(" ", ","))

'''6. Write a program to print alternate characters in a string.'''
# word = "python"
# print(word[::2],word[1::2],sep="")

'''7. Write a Program to print ascii values of the characters present in a string.'''
# word = "build"
# print({char:ord(char) for char in word})

'''8. Write program to convert upper case to lower case and vice-versa without using inbuilt method.'''
# default_ = "Hello"
# # swapcase_ = default_.swapcase()
# # print(swapcase_)
# d = 32
# print("".join([chr(ord(char)+d) if 'A' <= char <= 'Z' else chr(ord(char)-32) for char in default_]))
#

'''9. Write program to swap two numbers without using 3rd variable.'''
# a = 10 #5
# b = 20 #30
# a, b = b, a
# # a, b = [a + (b-a), b - (b-a)]
# print(a, b)

'''10. Write program to merge two different lists.'''
# l1 = [1,2,3]
# l2 = [4,5,6]

# print(l1+l2)
# print([item for item in (*l1,*l2)])


# l = [4,5,6]
# l1 = [1,2]
# l3 = [3]
# lis = []
# for i in range((len(l)*2)-1):
#     lis.append(0)
# lis.append(l[-1])
# print(lis)

# lis = [0 for i in range((len(l3)*2)-1)]
# lis.append(l3[-1])
# print(lis)

"""11. Write program to read a random line in a file. (ex. 50, 65, 78th line)"""

# from itertools import islice
#
# path = "" == > (file path)
#
# lis = [50, 65, 78]
#
#
# def read_specific_lines(num):
#     with open(path) as f:
#         res = islice(f, num, num + 1)
#         return res
#
#
# print(map(read_specific_lines, lis))
#











# class Demo:
#
#     def add(self, a, b):
#         self.a = a
#         self.b = b
#         a += 5
#         return a + b
#
#     def add1(self):
#         return a
#
#
# a = Demo()
# print(a.add(1,2))
# print(a.add1())








#
# l = [1,2,2,2,2,2,2,4]

# l1 = [4, 2, 2, 2, 2, 2, 2, 1]
# # # # print(list(reversed(l)))
# # #
# # l = [item if l.count(item) == 1 else l.remove(item) for item in reversed(l) ]
#
# l = [item if l.count(item) == 1 else str(l.remove(item)) for item in reversed(l) ]

# print(l)
# # #
# #
# print(l)
#
# l = [1,2,3,2,4]
#
# print(str(None).replace("None",""))




