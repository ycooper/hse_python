import sys

lines = ''
word_count = {}
words = []
for line in sys.stdin:
    for word in list(map(str, line.split())):
        words.append(word)

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

answer = ''
max_index = 0

for word, count in word_count.items():
    if count > max_index:
        answer = word
        max_index = count
    elif count == max_index and word < answer:
        answer = word

print(answer)
