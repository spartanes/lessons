def popular_words(text, words):
    text_words = text.lower().split()

    word_counts = {word: 0 for word in words}

    for word in text_words:
        if word in word_counts:
            word_counts[word] += 1

    return word_counts

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }
print('OK')

