Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]

>>> print(change_sring('pineapple'))
eineapplp
>>> 