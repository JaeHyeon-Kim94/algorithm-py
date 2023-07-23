# 1. type hint
import collections
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


# 10. 자료형
#      None, 정수형(class int, class bool), 실수(class float)
#      집합형(class set), 매핑(dictionary; class dict)
#      불변-문자열(class str), 불변-튜플(class tuple), 불변-바이트(class bytes)
#      가변-리스트(class list)

# 10-1 숫자 : int는 고정정밀도가 아닌 임의정밀도, long이 없음.
#            boolean은 파이썬 내부적으로 0(False), 1(True)로 처리되는 int class임.

# 10-2 매핑과 집합형 : 딕셔너리(매핑)는 key - value 형태이며, Set(집합형)은 value만 선언.
#                   파이썬 컴파일러는 이를 이용해 타입 결정하며, 둘 다 중괄호를 사용하는 공통점이 있다.


# 11. 원시타입 - 자바, C, 파이썬

# 자바/C에서는 숫자와 같은 타입에 대해 원시 타입을 제공한다.
# 이러한 원시타입은 값의 크기만큼만 메모리를 차지하는데,
# 자바에서 제공하는 래퍼클래스(Integer, Boolean 등)들은 객체로 변환되어 메모리 점유율이 크게 늘어난다.
# 객체로 변환되면서 다양한 기능을 제공하기는 하지만, JOL(Java Object Layout) 실행결과를 확인해보면
# 여러 부가정보가 추가되므로 메모리 점유율이 늘어남과 동시에 계산 속도 또한 감소하게 된다.
# 파이썬은 원시타입을 지원하지 않으며 모든 자료형이 객체이다.


# 12. 불변객체와 가변객체
# 불변객체 : boolean, int, float, tuple, str
# 가변객체 : list, set, dictionary

print(id('aaa'))
a = 'aaa'
print(id(a))
# 원시타입이라면 각 값들은 다른 메모리 영역을 차지할 것이나, 객체를 참조하기 때문에 같은 id를 가지며
# 값이 달라질 경우 id가 달라지는 것을 확인할 수 있다.

a = [1, 2, 3, 4, 5]

print(id(a))
print(id([1, 2, 3, 4, 5]))
a.remove(5)
print(id(a))

# 가변객체에 대해서는 a와 [1, 2, 3, 4, 5]의 id가 다름을 확인할 수 있으며
# a의 값이 변경되더라도 같은 id가 유지되는 것을 확인할 수 있다.

# 13. is 와 ==

# python에서 is는 id값(참조값)을, ==는 값을 비교한다.

# try 구문
a = [1, 2, 3, 4, 5, 6, 7, 8]
try:
    print(a[8])
except IndexError:
    print("존재하지 않는 인덱스")


# 14. list
# 파이썬은 원시타입이 아닌 객체 참조 타입만이 존재하여 배열의 요소 또한 포인터로 연결된다.
# 요소로 원시타입이 들어갈 경우 각 자료형마다 크기가 다르기 때문에 한 자료형만 관리 가능하나,
# 파이썬의 경우 여러 자료형을 하나의 리스트에서 관리 가능하다.


# 15. 딕셔너리
# 3.7v+ 부터 입력 순서가 유지되며, 내부적으로 해시 테이블로 구현되어있다.
# 3.6버전까지는 내부 순서 유지되지 않아 collections.OrderedDict() 라는 별도 자료형 제공되었었음.

# 딕셔너리 삭제
dict = {'1':'a', '2':'b', '3':'c'}
del dict['1']
print(dict)

# defaultdict : 존재하지 않는 키를 조회할 겨우 에러 메시지를 출력하는 대신,
#               디폴트 값을 기준으로 해당 키에 대한 딕셔너리 아이템을 생성해준다.

a = collections.defaultdict(int)
a['A']+=1
a['B']+=2
print(a)

# Counter : 아이템에 대한 개수를 계산하여 딕셔너리로 리턴한다.
a = [1, 2, 3, 4, 5, 6, 5, 7, 6, 5, 3, 1]
b = collections.Counter(a)
print(b)

# 빈도가 많은 5개 요소
print(b.most_common(5))
