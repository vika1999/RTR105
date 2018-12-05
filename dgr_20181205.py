Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> original = "To be or not to be"
>>> type(original)
<class 'str'>
>>> original [0]
'T'
>>> original [1]
'o'
>>> original [2]
' '
>>> original [3]
'b'
>>> ord(original[0])
84
>>> bin(ord(original[0]))
'0b1010100'
>>> ord(original[0]) ^ key
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    ord(original[0]) ^ key
NameError: name 'key' is not defined
>>> key = 5
>>> ord(original[0]) ^ key
81
>>> chr(ord(original[0]) ^ key)
'Q'
>>> original
'To be or not to be'
>>> key
5
>>> message = ""
>>> N = len(original)
>>> for i in range(N):
	message = message + chr(ord(orogonal[i]) * key)

	
Traceback (most recent call last):
  File "<pyshell#22>", line 2, in <module>
    message = message + chr(ord(orogonal[i]) * key)
NameError: name 'orogonal' is not defined
>>> message = ""
>>> N = len(original)
>>> for i in range(N):
	message = message + chr(ord(original[i]) * key)

	
>>> 
>>> for i in range(N):
	message = message + chr(ord(original[i]) * key)

	
>>> message
'Ƥȫ\xa0Ǫǹ\xa0ȫȺ\xa0ȦȫɄ\xa0Ʉȫ\xa0ǪǹƤȫ\xa0Ǫǹ\xa0ȫȺ\xa0ȦȫɄ\xa0Ʉȫ\xa0Ǫǹ'
>>> message = ""
>>> N = len(original)
>>> for i in range(N):
	message = message + chr(ord(original[i]) * key)

	
>>> message
'Ƥȫ\xa0Ǫǹ\xa0ȫȺ\xa0ȦȫɄ\xa0Ʉȫ\xa0Ǫǹ'
>>> message = ""
>>> N = len(original)
>>> for i in range(N):
	message = message + chr(ord(original[i]) ^ key)

	
>>> message
'Qj%g`%jw%kjq%qj%g`'
>>> result = ""
>>> key1 = 6
>>> for i in range(N):
	result = result + chr(ord(message[i]) ^ key1)

	
>>> result
'Wl#af#lq#mlw#wl#af'
>>> result = ""key1 = 6
SyntaxError: invalid syntax
>>> 
>>> result = ""
>>> key1 = 5
>>> for i in range(N):
	result = result + chr(ord(message[i]) ^ key1)

	
>>> result
'To be or not to be'
>>> 
