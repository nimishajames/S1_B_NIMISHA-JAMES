Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

>>> print( word_count('When you change the quality of your thinking, you change the quality of your life, sometimes instantly.'))
{'When': 1, 'you': 2, 'change': 2, 'the': 2, 'quality': 2, 'of': 2, 'your': 2, 'thinking,': 1, 'life,': 1, 'sometimes': 1, 'instantly.': 1}
>>> 