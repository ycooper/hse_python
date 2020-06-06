n = int(input())
dict1 = {}
dict2 = {}
for i in range(n):
    words = str(input()).split()
    dict1[words[0]] = words[1]
    dict2[words[1]] = words[0]
word = str(input())
if dict1.get(word, 0) != 0:
    print(dict1[word])
else:
    print(dict2[word])
