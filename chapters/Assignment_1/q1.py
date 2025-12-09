You are given a list of product names that contain extra spaces and inconsistent capitalization:
products = [" LAPTOP ", "phone ", " Tablet", "CAMERA "]
Using map() and lambda, clean the data by:
['Laptop', 'Phone', 'Tablet', 'Camera']
products = [" LAPTOP ", "phone ", " Tablet", "CAMERA "]
print(list(map( lambda p : p.strip().title(), products)))
Given a list of temperatures in Celsius, convert them to Fahrenheit using:
F=9/5C+32
celsius = [0, 10, 20, 30, 40]
[32.0, 50.0, 68.0, 86.0, 104.0]
Hint:
celsius = [0, 10, 20, 30, 40]
print(list(map(lambda c : (9 / 5) * c + 32 , celsius
You have a list of integers. You need to:
nums = [1, 2, 3, 4, 5]
[11, 14, 19, 26, 35]
Hint:
nums = [1, 2, 3, 4, 5]
print(list(map(lambda n : n ** 2 + 10, nums)))
Given a list of words, create a new list of tuples (first_char, last_char) for each word.
words = ["python", "lambda", "programming", "map", "function"]
[('p', 'n'), ('l', 'a'), ('p', 'g'), ('m', 'p'), ('f', 'n')]
Hint:
words = ["python", "lambda", "programming", "map",
print(list(map(lambda w : (w[0] , w[-1]) , words)))
marks = [[45, 80, 70], [90, 60, 100], [88, 76, 92]]
[[47, 84, 74], [95, 63, 105], [92, 80, 97]]
Hint:
Use:
marks = [[47, 84, 74], [95, 63, 105], [92, 80, 97]]
print(list(map(lambda row: list(map(lambda x: round(x *