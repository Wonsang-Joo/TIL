# 21.01.28 Homework (주원상)

### 1번. Circle 인스턴스 만들기

```
아래와 같은 Circle 클래스가 있을 때, 반지름이 3이고, x, y좌표가 (2, 4)인 Circle 인스턴스를 만들어 넓이와 둘레를 출력하시오.
```

```python
circle_1 = Circle(3, 2, 4)

circle_1.area()

circle_1.circumference()

```



### 2번. Dog과 Bird는 Animal이다

```
다음과 같이 Animal 클래스가 주어질 때, 해당 클래스를 상속 받아 아래의 보기와 같이 동작하는 Dog 클래스와 Bird 클래스를 작성하시오.
```

```python
class Animal:
    
    def __init__(self, name):
        self.name = name
        
    def walk(self):
        print(f'{self.name}! 걷는다!')
        
    def eat(self):
        print(f'{self.name}! 먹는다!')
        
        
class Dog(Animal):
    
    def walk(self):
        print(f'{self.name}! 먹는다')
        
    def bark(self):
        print(f'{self.name}! 짖는다')
        
        
        
class Bird(Animal):
    
    def walk(self):
        print(f'{self.name}! 걷는다!')
        
    def fly(self):
        print(f'{self.name}! 푸드덕!')
        
    def eat(self):
        print(f'{self.name}! 먹는다!')
        
        
        
dog = Dog('멍멍이')
dog.walk()
dog.bark()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()
```



### 3번. 오류의 종류

```
아래에 제시된 오류들이 각각 어떠한 경우에 발생하는지 간단하게 작성하시오.
```

```python
ZeroDivisionError: 0으로 나눌경우
NameError:지역 혹은 전역 이름 공간내에서 유효하지 않는 이름
TypeError:자료형에 대한 타입 자체가 잘못 되었을 경우
IndexError:존재하지 않는 index로 조회할 경우
KeyError:딕셔너리에서 key가 없는 경우
ModuleNotFoundError:모듈을 찾을 수 없는 경우
ImportError:모듈을 찾았으나 가져오는 과정에서 실패하는 경우
```

