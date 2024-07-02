def print_word(N:int):
    if N == 0:
        return
    print_word(N - 1)
    print('HelloWorld')

N = int(input())
print_word(N)