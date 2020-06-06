import sys

lines = ''
word_count = {}
words = []
for line in sys.stdin:
    for word in list(map(str, line.split())):
        words.append(word)

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

answer = []

for word, count in word_count.items():
    answer.append((-count, word))

answer.sort()

for i in answer:
    print(i[1])
