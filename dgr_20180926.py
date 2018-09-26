Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> input("Cienijamais lietotāj, lūdzu, ievadi skaitli: ")
Cienijamais lietotāj, lūdzu, ievadi skaitli: 100
100
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> mans_mainiigais = input("Cienijamais lietotāj, lūdzu, ievadi skaitli: ")
Cienijamais lietotāj, lūdzu, ievadi skaitli: 100
>>> vars()
{'mans_mainiigais': 100, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> mans_mainiigais
100
>>> mans_mainiigais
100
>>> mans_mainiigais = input("Cienijamais lietotāj, lūdzu, ievadi skaitli: ")
Cienijamais lietotāj, lūdzu, ievadi skaitli: 200
>>> vars()
{'mans_mainiigais': 200, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180926.py ===============
Cienijamais lietotāj, lūdzu, ievadi skaitli: 85
>>> vars()
{'mans_mainiigais': 85, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180926.py', '__package__': None, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180926.py ===============
Cienijamais lietotāj, lūdzu, ievadi skaitli: 4
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180926.py ===============
Cienijamais lietotāj, lūdzu, ievadi skaitli: 12
>>> vars()
{'mans_mainiigais': 12, '__builtins__': <module '__builtin__' (built-in)>, '__file__': '/home/user/RTR105/test_1_20180926.py', '__package__': None, 'x': 144, '__name__': '__main__', '__doc__': None}
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180926.py ===============
Cienijamais lietotāj, lūdzu, ievadi skaitli: 45
Lietotāj, Tu esi ievadījid vērtību: 45
Kā arī tagad atmiņā ir arī x = 2025
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180926.py ===============
Cienijamais lietotāj, lūdzu, ievadi skaitli: 33
Lietotāj, Tu esi ievadījid vērtību: 33
Kā arī tagad atmiņā ir arī x = 1089
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180926.py ===============
Cienijamais lietotāj, lūdzu, ievadi skaitli: 2
Lietotāj, Tu esi ievadījid vērtību: 2
Kā arī tagad atmiņā ir arī x = 4
>>> type(mans_mainiigais)
<type 'int'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180926.py ===============
Cienijamais lietotāj, lūdzu, ievadi skaitli: 1.1
Lietotāj, Tu esi ievadījid vērtību: 1.1000
Kā arī tagad atmiņā ir arī x = 1.210
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180926.py ===============
Cienijamais lietotāj, lūdzu, ievadi skaitli: 1.1
Lietotāj, Tu esi ievadījid vērtību:     1.1000
Kā arī tagad atmiņā ir arī x =           1.210
>>> type(mans_mainiigais)
<type 'float'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180926.py ===============
Cienijamais lietotāj, lūdzu, ievadi skaitli: 1
Lietotāj, Tu esi ievadījid vērtību:     1.0000
Kā arī tagad atmiņā ir arī x =           1.000
>>> type(mans_mainiigais)
<type 'int'>
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180926.py ===============
Cienijamais lietotāj, lūdzu, tekstu: AAaaaa

Traceback (most recent call last):
  File "/home/user/RTR105/test_1_20180926.py", line 3, in <module>
    x = mans_mainiigais * mans_mainiigais
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
=============== RESTART: /home/user/RTR105/test_1_20180926.py ===============
Cienijamais lietotāj, lūdzu, tekstu: gdfg
Lietotāj, Tu esi ievadījid vērtību: gdfg
>>> 

