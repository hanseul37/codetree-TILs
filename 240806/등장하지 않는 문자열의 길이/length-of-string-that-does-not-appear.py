n = int(input())
word = input()

max_length = 0

# 연속된 문자로 구성된 부분 문자열인지 확인하는 함수
def is_consecutive(sub):
    for i in range(len(sub) - 1):
        if ord(sub[i]) + 1 != ord(sub[i + 1]):
            return False
    return True

# 가능한 모든 부분 문자열 길이에 대해 반복
for i in range(1, n):
    for j in range(n - i):
        first = word[j:j + i]
        if is_consecutive(first):
            second = word[j + i:]
            if first in second:
                max_length = i

print(max_length + 1)