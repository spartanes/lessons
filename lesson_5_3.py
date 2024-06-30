import string

string_1 = input('Type in the words: ').title()
string_2 = string_1.translate(str.maketrans('', '', string.punctuation))

print(string_1)

words = string_2.split()

hashtag = '#' + ''.join(words)

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
