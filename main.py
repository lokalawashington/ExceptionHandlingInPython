# with open("a_file.txt") as file:
#    file.read()
# filenotfound exception
#
# try:
#     file = open("a_file.txt")
#     #key error
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     # print("There was an error")
#     file.write("Hey I am learning python and python is fun")
# except KeyError as error_message:
#     print(f"key{error_message}does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     #file.close()
#     #print("File was closed")
#     raise TypeError("This is an error that I made up")


"""Second code exercise"""

# height = float(input("height: "))
# weight = float(input("weight: "))
# if height > 3:
#     raise ValueError("Human height must not be greater than 3 meters")
# bmi = weight/height ** 2
# print(bmi)

"""third code exercise"""
fruits = ["Apple", "Pear", "Oranges"]

# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit +" "+ "pie")
#
# make_pie(4)
# # indexError
# # make_pie(4)

"""Reform working code"""

# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print("Fruit pie ")
#     else:
#         print(fruit + " " + "pie")
#
# make_pie(4)

"""Third code exersice"""
"""KeyError Handling Excercise"""
facebook_posts = [
    {'likes': 21, 'Comments': 2},
    {'likes': 31, 'Comments': 2, ' Share': 1},
    {'likes': 33, "comments": 8, 'share': 3},
    {'comments': 4, 'share': 2},
    {'comments': 1, 'share': 1},
    {'likes': 19, 'comments': 3}
]

total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post["likes"]
    except KeyError:
        #total_likes + = 0
        pass
print(total_likes)
