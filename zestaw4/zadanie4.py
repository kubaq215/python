from functools import singledispatch, singledispatchmethod
from math import log10, ceil

@singledispatch
def Append(a, b):
    print('Type not supported')

@Append.register(int)
def _(a, b):
    res = a * (10 ** ceil(log10(b))) + b
    return res

@Append.register(str)
def _(a, b):
    return a + b

@Append.register(list)
def _(a, b):
    return a + b

Append(2.0, 11.0)
print(Append(34, 6))
print(Append('Hello', 'World'))
print(Append([1,2,3], [5,6,7]))

class Message:
    pass

class ErrorMessage(Message):
    def __init__(self, text):
        self.text = text

class WarningMessage(Message):
    def __init__(self, text):
        self.text = text

class MessageDisplay:
    @singledispatchmethod
    def display(mess: Message):
        pass

    @display.register
    def _(self, mess: ErrorMessage):
        print(f"ERROR - {mess.text}")

    @display.register
    def _(self, mess: WarningMessage):
        print(f"Warning - {mess.text}")

messages = [
    ErrorMessage(text = 'This is an error'), 
    WarningMessage(text = 'This is a warning')]

displayer = MessageDisplay()

print()

for message in messages:
    displayer.display(message)