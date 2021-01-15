#import문은 스크립트 파일 최상단에
import random

numbers = range(1, 46)
# print(numbers)

lucky_numbers = random.sample(numbers, 6)
# print(lucky_numbers)

#정렬
print(sorted(lucky_numbers))