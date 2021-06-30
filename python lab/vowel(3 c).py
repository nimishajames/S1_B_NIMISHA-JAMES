Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> stringA = "Hello..how are you"
>>> print("Given String: \n",stringA)
Given String: 
 Hello..how are you
>>> vowels = "AaEeIiOoUu"
>>> res = set([each for each in stringA if each in vowels])
>>> print("The vlowels present in the string:\n ",res)
The vlowels present in the string:
  {'u', 'a', 'e', 'o'}
>>> 