# 21.01.21 Workshop (주원상) 

### 1번. 숫자의 의미 

```
정수로 이루어진 list를 전달 받아, 각 정수에 대응되는 아스키 문자를 이어붙인
문자열을 반환하는 get_secret_word 함수를 작성하시오. 단, list는 65이상 90이하
그리고 97이상 122이하의 정수로만 구성되어 있다.

```

```python
def get_secret_number(word):
    total = 0
    
    for char in word:
        total += ord(char)
    
    return total


```



### 2번. 내 이름은 몇일까?

```
문자열을 전달 받아 해당 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 반환하는
get_secret_number 함수를 작성하시오. 단, 문자열은 A~Z, a~z로만 구성되어 있다.
```

```python
def get_secret_number(word):
    total = 0
    
    for char in word:
        total += ord(char)
    
    return total


```



### 3번. 강한 이름

```
문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하
여 더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수를 작성하시오.
```

```python
def get_strong_word(word1, word2):
    
    word1_total = get_secret_number(word1)
    word2_total = get_secret_number(word2)
    
    if word1_total > word2_total:
        return word1
    else:
        return word2
    


```

