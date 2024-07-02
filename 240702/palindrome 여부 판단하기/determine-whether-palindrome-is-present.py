def palindrome(word:str):
    new_word = word[::-1] 
    return new_word

word = input()
new_word = palindrome(word)
if word == new_word:
    print('Yes')
else:
    print('No')