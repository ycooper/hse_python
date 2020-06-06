lines = ''
word_count = {}
with open("input.txt", "r") as f:
    lines = f.read().splitlines()
for line in lines:
    for word in line.split():
        print(word_count.get(word, 0), end=' ')
        word_count[word] = word_count.get(word, 0) + 1
