n = int(input())
pupils = [None] * n
school_languages = set()
min_languages = 0

for i in range(n):
    m = int(input())
    languages = set()
    for j in range(m):
        next_language = str(input())
        languages.add(next_language)
        school_languages.add(next_language)
    pupils[i] = languages

common_languages = set(school_languages)

for i in pupils:
    common_languages &= i

print(len(common_languages))
for i in common_languages:
    print(i)
print(len(school_languages))
for i in school_languages:
    print(i)
