# 만들어 놓은 FourCal 클래스에 덧셈, 뺄셈, 곱셈, 나눗셈을 연산할 때 마다 
# 어떠한 연산을 몇 번 수행했는지 저장. 연산 횟수 출력하는 메서드 추가

cal.ShowCount()

class FourCal:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school
    def add(self, n1, n2):
        result = n1 + n2
        return result
    def minus(self, n1, n2):
        result = n1 - n2
        return result
    def mult(self, n1, n2):
        result = n1 * n2
        return result
    def divide(self, n1, n2):
        if (n2 == 0):
            print('0으로 나눌 수 없습니다.')
        result = n2 / n2
        return result
    def ShowCount():
        print("덧셈 : %2d" %FourCal.add_num)
        print("뺄셈 : %2d" %FourCal.minus_num)
        print("곱셈 : %2d" %FourCal.mult_num)
        print("나눗셈 : %2d" %FourCal.divide_num)
        

calculator2 = FourCal("강단비", 21, "사범대학")
print(calculator2.add(3, 4))