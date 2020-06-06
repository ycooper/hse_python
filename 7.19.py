word_count = {}
words = []
with open('input.txt', 'r', encoding='utf8') as f:
    words = f.read().splitlines()

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

answer = []

for word, count in word_count.items():
    answer.append((-count, word))

answer.sort()

with open("output.txt", "w", encoding="utf8") as f:
    if - answer[0][0] > len(words) / 2:
        f.write(answer[0][1] + "\n")
    else:
        f.write(answer[0][1] + "\n")
        f.write(answer[1][1] + "\n")
