n = int(input())
arr = input().split()
word = "".join(arr)
for i in range(len(word)//5+1):
    for j in range(1,6):
        if 5 * i + j == len(word) + 1:
            break;
        print(word[5*i+j-1], end="")
    print()