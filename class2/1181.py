N = int(input())
word_list = []
i = 0

while i < N:
    word = str(input())
    word_list.append((word, len(word)))
    i += 1

word_list = list(set(word_list))

word_list.sort(key=lambda word : (word[1], word[0]))

for word in word_list:
    print(word[0])