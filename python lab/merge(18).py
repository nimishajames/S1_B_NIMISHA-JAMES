Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def Merge(dict1, dict2):
    return(dict2.update(dict1))

>>> dict1 = {'a': 10, 'b': 8}
>>> dict2 = {'d': 5, 'c': 2}
>>> print(Merge(dict1, dict2))
None
>>> print(dict2)
{'d': 5, 'c': 2, 'a': 10, 'b': 8}
>>> 