Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [10, 10, 11, 12, 12, 13, 14, 16, 15, 16, 12]
>>> list2 = [10, 10, 11, 12, 12, 16, 14, 16, 15, 19, 12]
>>> for value in list1:
      if value in list2:
         common=1

         
>>> if common==1:
	print("there are common elements")
else:
	print("no common elements")

	
there are common elements
>>> 