# Practice 1

> 데이터 & 제어문

## 갯수 구하기

> 주어진 리스트의 요소는 학생 이름으로 구성되어 있다. 학생들의 수를 출력하시오.

------

```
[출력 예시]
3
```

In [2]:

```
students = ['김철수', '이영희', '조민지']

# 아래에 코드를 작성하시오.

len(students)

```

Out[2]:

```
3
```

In [3]:

```
len(students)
```

Out[3]:

```
3
```

## 득표수 구하기

> 주어진 리스트는 반장 선거 투표 결과이다. 이영희의 총 득표수를 출력하시오.

------

```
[출력 예시]
4
```

In [4]:

```
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']

# 아래에 코드를 작성하시오.




  File "<ipython-input-4-42f8a8f0ac26>", line 8
    if name not in vote_counter:
    ^
IndentationError: expected an indented block
```

## 최댓값 구하기

> 주어진 리스트의 요소 중에서 최댓값을 출력하시오.

------

```
[출력 예시]
22
```

In [5]:

```
numbers = [7, 10, 22, 4, 3, 17]

# 아래에 코드를 작성하시오.

print(max(numbers))
22
```

## 최솟값 구하기

> 주어진 리스트의 요소 중에서 최솟값을 출력하시오.

------

```
[출력 예시]
3
```

In [6]:

```
numbers = [7, 10, 22, 4, 3, 17]

# 아래에 코드를 작성하시오.

print(min(numbers))
3
```

## 최댓값과 등장 횟수 구하기

> 주어진 리스트의 요소 중에서 최댓값과 등장 횟수를 출력하시오.

------

```
[출력 예시]
22 3
```

In [3]:

```
numbers = [7, 10, 22, 7, 22, 22]

# 아래에 코드를 작성하시오.

max_value = numbers[0]
count = 0
for number in numbers:
    if number > max_value:
        max_value = number
        count = 1 #카운트 초기화 (새로운 최대값으로 바꼈으므로)
        
    elif number == max_value:  # elif는 위에랑 통합, if만 쓰면 다른 if랑 따로따로
        count += 1
        
print(max_value, count)

22 3
```

## 5의 개수 구하기

> 주어진 리스트의 요소 중에서 5의 개수를 출력하시오.

------

```
[출력 예시]
3
```

In [5]:

```
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

# 아래에 코드를 작성하시오.
# count = 0

# for number in numbers:
#     if number == 5:
#         count += 1
        
# print(count)

print(numbers.count(5))
3
```

## 'a'가 싫어

> 입력으로 짧은 영단어 word가 주어질 때, 해당 단어에서 'a'를 모두 제거한 결과를 출력하시오.

------

```
[입력 예시]
apple

[출력 예시]
pple
```

In [7]:

```
word = input()

# 아래에 코드를 작성하시오.
result = ''

for char in word:
    if char != 'a':
        result += char
        
print(result)

apple
pple
```

## 단어 뒤집기

> 입력으로 짧은 영어단어 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

------

```
[입력 예시]
apple

[출력 예시]
elppa
```

In [9]:

```
# word = input()

# 아래에 코드를 작성하시오.
word = 'apple'

result = ''

for char in word:
    result = char + result
    
    print(result)
    
print(result)

a
pa
ppa
lppa
elppa
elppa
```





# Workshop

> 데이터 & 제어문

## 1. 간단한 N의 약수 (SWEA #1933)

> 입력으로 1개의 정수 N이 주어진다. 정수 N의 약수를 오름차순으로 출력하는 프로그램을 작성하시오.

------

```
[제약 사항]
N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)

[입력 예시]
입력으로 정수 N이 주어진다.

[출력 예시]
정수 N의 모든 약수를 오름차순으로 출력한다.
```

In [3]:

```
N = int(input())

# 아래에 코드를 작성하시오.

for i in range(1, N+1):
    if N % i == 0:
        print(i)
10
1
2
5
10
```

## 2. 중간값 찾기 (SWEA #2063 변형)

> 중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다. 리스트 numbers에 입력된 숫자에서 중간값을 출력하라.

------

```python
[출력 예시]
64
```

In [10]:

```
numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]

# 아래에 코드를 작성하시오.
# center_index = len(numbers) // 2

# sorted_numbers = sorted(numbers)

# print(sorted_numbers[center_index])

length = 0
for _ in numbers:
    length += 1
print(length)
33
```