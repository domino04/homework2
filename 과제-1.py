#홀수단(1,3,4,5,7,9단) 출력하는 함수 gugudan_odd 함수 정의
def gugudan_odd(i):
    odd = [1, 3, 5, 7, 9]
    for i in odd:
        for a in range(1, 9):
            print("%d * %d = %d" % (i, a, i*a))

#짝수단(2,4,6,8단) 출력하는 함수 gugudan_even 함수 정의
def gugudan_even(i):
    even = [2, 4, 6, 8]
    for i in even:
        for a in range(1, 9):
            print("%d * %d = %d" % (i, a, i*a))


#인자가 홀수면 gugudan_odd 함수를 실행, 짝수면 gugudan_even 함수를 
#실행하는 함수 gugudan_odd_or_even 함수 정의 및 실행
def gugudan_even(i):
    even = [2, 4, 6, 8]
    for i in even:
        for a in range(1, 9):
            print("%d * %d = %d" % (i, a, i*a))

def gugudan_odd(i):
    odd = [1, 3, 5, 7, 9]
    for i in odd:
        for a in range(1, 9):
            print("%d * %d = %d" % (i, a, i*a))

def find(a):
    if(a % 2 == 0):
        gugudan_even(a)
    else:
        gugudan_odd(a)


#주어진 숫자에 따라 구구단 출력하는 함수
def gugudan(num):
    for i in range(1, num + 1):
        for a in range(1, 10):
            print("%d * %d = %d" % (i, a, i*a))


result = gugudan(5)
print(result)