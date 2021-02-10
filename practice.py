"""
date:2021-02-01
<here is my practice station.>
"""
import os

print("="*50)
print("Life is too short.. You need python")
print("="*50)


print("I have a {} a song to sing To help me cope.... with anything.".format("dream"))

print("\n")

class Calculator():
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        return self.first+self.second
    def div(self):
        return self.first-self.second
    def multiple(self):
        return self.first*self.second
    def dip(self):
        if(self.second==0):
            return 0
        return self.first/self.second

print("="*10)
print("calculator")
print("="*10)


first=int(input("first:"))
second=int(input("second:"))

print("\n")

a=Calculator(first,second)
print("{}+{}={}".format(first,second,a.add()))
print("{}-{}={}".format(first,second,a.div()))
print("{}*{}={}".format(first,second,a.multiple()))
print("{}/{}={}".format(first,second,a.dip()))

print("="*10)

print("{0:!^12}".format("python"))

name="hong gil dong"
age=30

print(f"my name is {name} and my age is {age}")
print("="*10)

os.system("pause")