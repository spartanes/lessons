def correct_sentence(sentence1, sentence2):
    def correct(s):
        s = s.capitalize()
        if not s.endswith('.'):
            s += '.'
        return s
    return  correct(sentence1), correct(sentence2)

print(correct_sentence("greetings", "friends"))
print(correct_sentence("hello", 'Hello'))
print(correct_sentence("Greetings", "Friends"))
print(correct_sentence("Greetings", "friends."))
print(correct_sentence("greetings", "friends."))
print('OK')
