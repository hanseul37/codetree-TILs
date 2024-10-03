# 입력 받기
n = int(input())
arr = list(map(int, input().split()))

# 홀수와 짝수 개수 세기
odd_count = sum(1 for x in arr if x % 2 != 0)
even_count = n - odd_count  # 총 개수에서 홀수 개수를 빼면 짝수 개수

# 최대 묶음 수 계산
if even_count == 0:
    # 홀수만 있을 경우, 홀수 2개씩 묶을 수 있는 만큼만 가능
    max_groups = odd_count // 2
elif odd_count == 0:
    # 짝수만 있을 경우, 1개의 묶음만 가능
    max_groups = 1
else:
    # 짝수와 홀수가 모두 있을 경우
    max_groups = min(odd_count, even_count) + 1

# 결과 출력
print(max_groups)