word = input()
window = []
left, max_len = 0, 0
for right in range(len(word)):
    if word[right] in window:
        while word[left] != word[right]:
            window.remove(word[left])
            left += 1
        left += 1
    else:
        window.append(word[right])
        max_len = max(len(window), max_len)
print(max_len)