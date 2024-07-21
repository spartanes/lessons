def first_word(text):
    text = text.strip()
    while text and (text[0] in '., '):
        text = text[1:].strip()

    word = ''
    for char in text:
        if char.isalnum() or char == "'":
            word += char
        else:
            break

    return word


print(first_word("Hello world"))
print(first_word("greetings, friends"))
print(first_word("don't touch it"))
print(first_word(".., and so on ..."))
print(first_word("hi"))
print(first_word("Hello.World"))
