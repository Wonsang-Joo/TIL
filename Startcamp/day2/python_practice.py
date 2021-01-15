#1. 기초 자료형
# number = 3
# print(number)
# print(type(number))
# string = '문자열'
# print(type(string))
# boolean = True
# print(boolean)
# print(type(boolean))

# string_number = '3'
# print(int(string_number) + 5)

#2. f-string  f를 이용해서 문자열 안에 변수 삽입 추가 { }필요
# name = '김창규'
# print(f'제 이름은 {name}입니다.')


# #3.List
# my_list = ['python', 'html', 'markdown',]
# print(my_list[2])


#딕셔너리 선언

age_dict = {
    '박소현': 25,
    '김지용': 83,
}

#딕셔너리 요소(원소) 접근

# print(age_dict['김지용'])
# print(age_dict.get('김지용'))

# 딕셔너리 요소 변경

age_dict['김지용'] = 103
# print(age_dict['김지용'])


# 기초 연산자 
# print(3 + 5)
# print(5 - 3)
# print(3 * 5)
# print(100 / 5)
# prunt(100 // 3) #몫
# print(100 % 3) #나머지
# print(2 ** 5) #제곱

#비교 연산자
# print(5 == 5)
# print(5 == '3')
# print(5 != 3) #다르다
# print(5 >= 3) #이상이하
# print(5 > 3) #초과

#조건문
n = 10
#1. 주어진 양수 n이 홀수, 짝수인지 판단하여 출력하는 코드를 작성해라.
# if n % 2 == 1:
#     print('홀수')
# else:
#     print('짝수')

#2. 주어진 숫자 n이 양수인지, 0인지, 음수인지 판단하여 출력하는 코드
#직접 해보기


#반복문

# numbers = [1, 2, 3,]
# for number in numbers:
#     print(number)


#레인지는 끝나는 숫자가 1 더 큼

numbers = range(1, 10)
for number in numbers:
    if number % 2 == 1:
        print(f'숫자 {number}은(는) 홀수네요!')
    else:
        print('짝수는 싫어')
        
#숫자 '뭐시기'는 홀수입니다.

