c) Always returns the same output for the same input
13 The filter()function in Python returns:
Answer = T
Answer = F
Answer = T
Answer = F
18 itertools provide memory-efficient tools for working with iterators, including infinite
Answer = T
# def remove_vowels(str):
# vowels = "aeiouAEIOU"
# return "".join([char for char in str if char not
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_nums = filter(lambda x: x % 2 != 0, nums)
# squared_odds = list(map(lambda x: x**2, odd_nums))
# import functools
# import time
# @functools.lru_cache(maxsize=None)
# def fibonacci(n):
# if n < 2:
# return n
# return fibonacci(n-1) + fibonacci(n-2)
# start_time = time.time()
# print(f"Fibonacci(35) = {fibonacci(35)}")
# end_time = time.time()
# print(f"Time taken: {end_time - start_time:.5f}
# def make_adder(n):
# def adder(x):
# return x + n
# return adder
# def apply_twice(func, value):
# return func(func(value))
# print(apply_twice(lambda x: x + 1, 5))
# def etl_pipeline(texts):
# stopwords = {"the", "a", "is", "in", "at", "of",
# all_Words = [word.lower() for text in texts for
# filtered_Words = filter(lambda word: word and word
# word_Frequencies = {}
# for word in filtered_Words:
# word_Frequencies[word] =
# return word_Frequencies
# def my_reduce(func, iterable, initializer=None):
# iterator = iter(iterable)
# if initializer is None:
# try:
# value = next(iterator)
# except StopIteration:
# raise TypeError("Empty sequence with no
# else:
# value = initializer
# for element in iterator:
# value = func(value, element)
# return value
# def log_call(func):
# def nestedFunc(*args, **kwargs):
# print(f"--- Calling function: {func.__name__}
# result = func(*args, **kwargs)
# print(f"--- Finished function: {func.__name__}
# return result
# return nestedFunc