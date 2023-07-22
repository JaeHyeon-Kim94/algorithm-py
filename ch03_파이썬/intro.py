# 1. type hint
import sys

a1: int = 1
b1: str = '1'


def fn(a2: int, b2: str):
    print(type(a2))
    print(type(b2))


fn(a1, b1)

# 2. List/dictionary(2.7v~) Comprehension

list_comp = [n * 2 for n in range(0, 15) if n % 2 == 1]
print(list_comp)

original = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
dict_comp = {key: value for key, value in original.items()}
print(dict_comp)


# 3. Generator
# 제너레이터만 생성해두고 필요할 때 값을 만들어낸다.

def get_natural_number():
    n = 0
    while True:
        n += 1
        yield n


print(get_natural_number())
g = get_natural_number()

for _ in range(0, 100):
    print(next(g))

# 4. range
# 2.x 버전에서는 제너레이터 방식의 경우 range()가 아닌 xrange() 사용
# 그러나 3.x 버전부터는 xrange() 사라지고, 제너레이터 역할을 하는 range 클래스 리턴함
print(list(range(5)))

print(range(5))

a = [n for n in range(100000)]

b = range(100000)

print(len(a) == len(b))

# 메모리 점유율에서 차이가 난다.
print(sys.getsizeof(a))
print(sys.getsizeof(b))

# 인덱스 접근시 바로 생성된다.
print(b[999])

# 5. enumerate

a = [1, 2, 3, 4, 5, 45, 2, 5]
print(enumerate(a))
print(list(enumerate(a)))

for i in range(len(a)):
    print(i, a[i])

for i, v in enumerate(a):
    print(i, v)

# 6. 나눗셈 연산자 /와 //
# 정수형을 나눗셈 연산할 경우, 2.x 버전에서는 자료형이 유지(정수형) 되었으나,
# 3.x 버전부터는 / 연산을 할 경우 자료형이 변경되며, //연산을 할 경우 자료형 유지됨.

print(5 / 3)
print(5 // 3)

print(type(5 / 3))
print(type(5 // 3))

# 7. print 함수

print("A1", "B2", sep=',')

print("AA", end=' ')
print("BB")

# list join
arr = ['a', 'b', 'c']
print(arr)
print(' '.join(arr))

idx = 0
fruit = 'apple'

print('{0}: {1}'.format(idx + 1, fruit))
print('{}: {}'.format(idx + 1, fruit))

# formated string literal (3.6+)

print(f'{idx + 1}: {fruit}')


#  8. pass
# 세부적인 구현은 뒤로 미뤄두고 구조만 잡고싶을 때 사용.
# 목업 인터페이스 구현 후 추후 구현 진행

class MyClass(object):
    def method_a(self):
        pass

    def method_b(self):
        print("Method B. pass 없으면 실행되지 않으며 오류 발생")


c = MyClass()

# 9. locals
# 로컬에 선언된 모든 변수를 조회한다.
import pprint

pprint.pprint(locals())