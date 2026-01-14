word, k = input().split()
k = int(k)
left, max_len, window = 0, 0, dict()
for right in range(len(word)):
    if word[right] in window:
        window[word[right]] += 1
    else:
        window[word[right]] = 1        
        
    while len(window) > k:
        window[word[left]] -= 1
        if window[word[left]] == 0:
            del window[word[left]]
        left += 1
    max_len = max(right - left + 1, max_len)
print(max_len)