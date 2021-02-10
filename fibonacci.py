"""
here is fibonacci function section..
"""

print("="*10)
print("Welcome to python!!")
print("="*10)

print("원하는 숫자를 입력해보세요..\n")

class fibonacci(object):
    def __init__(self,num):
        self.num=num

    def calculate(self):
        if(self.num==0):
            return 1
        if(self.num==1):
            return 1
        if(self.num>=2):
            print("%d+%d=%d\n"%(self.num-2,self.num-1,self.num-2 + self.num-1))
            print("결과값:")
            return self.num-2 + self.num-1
        else:
            print("이 프로그램에는 음수는 없다는 규칙이 적용되므로 0으로 반환합니다..")
            return 0

n=int(input())
a=fibonacci(n)

print(a.calculate())
