# Chapter 05-1
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다

# 함수 정의 방법
# def fuction_name(parameter)
#   code

# 예쩨1
def first_function(w):
    print("Hello ", w)

word = 'Good boy'

first_function(word)
print()

# 예제2
def return_function(w1):
    value = 'Hello, ' + str(w1)
    return value

x = return_function('Good boy2')
print(x)
print()

# 예제 3 다중반환
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1, y2, y3

x, y, z = func_mul(10)
print(x,y,z)
print()

# 예제 4 튜플리턴
def func_mul2(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1, y2, y3)

q = func_mul2(20)
print(q, type(q), list(q))

# 예제 5 리스트
def func_mul3(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return [y1, y2, y3]

p = func_mul3(30)
print(p, type(p), set(p))
print()

# 딕셔너리 리턴
def func_mul4(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return {'v1' : y1, 'v2' : y2, 'v3' : y3}

d = func_mul4(40)
print(type(d), d, d.get('v1'), d.items(), d.keys())
print()

# 중요
# *args, **kwargs

# *args(언팩킹)    // 튜플형
def args_func(*args):    # 매개변수명 자유
    for i, v in enumerate(args):
        print('Result : {}'.format(i), v)
    print('-------')

args_func('Lee')        # *args를 매개변수에 넣으면, list든 tuple이든 여러 데이터가
args_func('Lee', 'Park')# 넘어와도 하나하나씩 처리 해 준다는 뜻이다.
args_func('Lee', 'Park', 'Kim')
print()

# **kwargs(언팩킹) // key와 value
def kwargs_func(**kwargs):  # 매개변수명 자유
    for v in kwargs.keys():
        print("{}".format(v), kwargs[v])
    print('---------')

kwargs_func(name1 = 'Lee')
kwargs_func(name1 = 'Lee', name2 = 'Park', NAME3 = 'Cho')
print()

# 전체 혼합
def example(args_1, args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)
    print()

example(10,20,'lee','kIM','Park',age1 = 20, age2 = 30, age3 = 40)
print()

# 중첩함수
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("In func")
    func_in_func(num + 100)

nested_func(100)
print()
# func_in_func(1000)  # 이 함수는 nested_func()함수 안에서만 정의 되어있다.

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발 시 가독성 오히려

#def mul_func(x,y):
#    return x * y

#lambda x,y: x*y # 위의 함수를 lamda로 바꾸면 다음과 같다.

# 일반적 함수 -> 할당
def mul_func(x,y):
    return x * y

q = mul_func(10,50)
print(q)
print(mul_func(20,50))
print()

# 람다함수 -> 할당
lambda_mul_func = lambda x,y:x*y
print(lambda_mul_func(50,50))

def func_final(x,y,func):
    print(x * y * func(100,100))

func_final(10,20,lambda x,y:x*y)    # lambda는 이름이 없는 함수라, func parameter에 그대로 넣어도 된다.
