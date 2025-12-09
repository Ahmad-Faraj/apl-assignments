class Positive:
def __init__(self, name):
self.name = name
def __get__(self, instance, owner):
if instance is None: return self
def __set__(self, instance, value):
if value < 0:
instance.__dict__[self.name] = value
class BankAccount:
balance = Positive("balance")
def __init__(self, amount):
self.balance = amount
# Test
acc = BankAccount(100)
print(acc.balance)
# acc.balance = -50