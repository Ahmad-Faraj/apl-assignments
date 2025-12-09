The __exit__() method in a context manager is always executed, even if an exception occurs
using send(). Coroutines are often used for event-driven programming and concurrency.
Explain why the with statement is preferred over manual resource management. Answer:
cleaned up via __exit__(), even if an exception occurs, making code safer and cleaner.
import time
class Timer:
def __enter__(self):
self.start = time.time()
def __exit__(self, *args):
self.end = time.time()
print(f"Execution took {self.end -
with Timer():
for i in range(1000000):
def even_numbers(n):
for i in range(2, n + 1, 2):
for num in even_numbers(10):
print(num)
def filter_positive():
while True:
num = yield
if num > 0:
print(f"Positive number: {num}")
co = filter_positive()
class Circle:
def draw(self):
class Square:
def draw(self):
def shape_factory(shape_type):
if shape_type == "circle":
elif shape_type == "square":
else:
shape = shape_factory("circle")
print(shape.draw())
class Subject:
def __init__(self):
self.observers = []
def attach(self, observer):
def notify(self, message):
for obs in self.observers:
class Observer:
def update(self, message):
print(f"Received update: {message}")
subject = Subject()
obs1 = Observer()
obs2 = Observer()