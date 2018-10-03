Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
[GCC 5.4.0 20160609] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> 10 = 10
SyntaxError: can't assign to literal
>>> a = 2
>>> vars()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 2, '__package__': None}
>>> type(3,5)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    type(3,5)
TypeError: type() takes 1 or 3 arguments
>>> vars ()
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 2, '__package__': None}
>>> print(123)
123
>>> print(98.6)
98.6
>>> print('Hello world')
Hello world
>>> false

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    false
NameError: name 'false' is not defined
>>> print(false)

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(false)
NameError: name 'false' is not defined
>>> print(is)
SyntaxError: invalid syntax
>>> print(return)
SyntaxError: invalid syntax
>>> x = 12.2
>>> y = 14
>>> vars()
{'a': 2, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 12.2, 'y': 14, '__name__': '__main__', '__doc__': None}
>>> x = 12.2
>>> y = 14
>>> x = 100
>>> ID = 'x=12.2'
project = ("100"+ID)
>>> ID = 'x=12.2'
project = ("x=100"+ID)
>>> ID = "x=100"
>>> print x=100
SyntaxError: invalid syntax
>>> print "x=100"
x=100
>>> vars()
{'a': 2, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', 'ID': 'x=100', '__doc__': None}
>>>  underscore _"spam"
 
  File "<pyshell#24>", line 1
    underscore _"spam"
    ^
IndentationError: unexpected indent
>>> "underscore_spam"
'underscore_spam'
>>> "underscore_sSPAM"
'underscore_sSPAM'
>>> vars()
{'a': 2, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', 'ID': 'x=100', '__doc__': None}
>>> “
mnemonic
”
= 
“
memory aid
”

SyntaxError: invalid syntax
>>> (“mnemonic”= “memory aid”)  \
	     
SyntaxError: invalid syntax
>>> 
>>> a = 5
>>> b = 9
>>> c = 5 * 9
>>> print(c)
45
>>> vars()
{'a': 5, 'c': 45, 'b': 9, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 100, 'y': 14, '__name__': '__main__', 'ID': 'x=100', '__doc__': None}
>>> a
5
>>> a = 2
>>> b = 2
>>> c = 2 * 2
>>> print(pay)

Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    print(pay)
NameError: name 'pay' is not defined
>>> x = 2
>>> x = x +2
>>> print(x)
4
>>> x = 4
>>> x = 2 * x ( 1- x )

Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    x = 2 * x ( 1- x )
TypeError: 'int' object is not callable
>>> x=2*x(1-x)

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    x=2*x(1-x)
TypeError: 'int' object is not callable
>>> x = 4
>>> x =2*x(-x)

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    x =2*x(-x)
TypeError: 'int' object is not callable
>>> vars()
{'a': 2, 'c': 4, 'b': 2, '__builtins__': <module '__builtin__' (built-in)>, '__package__': None, 'x': 4, 'y': 14, '__name__': '__main__', 'ID': 'x=100', '__doc__': None}
>>> x = 0.6
>>> 0.6 =3.9*0.6(1-0.6)
SyntaxError: can't assign to literal
>>> x=3.9*x(1-x) print(x)
SyntaxError: invalid syntax
>>> x=3.9*x(1-x)

Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    x=3.9*x(1-x)
TypeError: 'float' object is not callable
>>> print(x)
0.6
>>> x = 0.6
>>> x =3.9*x(1-x)

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    x =3.9*x(1-x)
TypeError: 'float' object is not callable
>>> x = 3.9 * x * ( 1 - x )
>>> x
0.9359999999999999
>>> xx = 2
>>> xx = xx + 2
>>> print(xx)
4
>>> yy = 440 * 12
>>> print(yy)
5280
>>> zz = yy / 1000
>>> print(zz)
5
>>> jj = 23
>>> kk = jj % 5
>>> print(kk)
3
>>> print(4 ** 3)
64
>>> "operator predence"
'operator predence'
>>> x = 1 + 2 * 3 - 4 / 5 ** 6
>>> print"(operator predence)"
(operator predence)
>>> x = 1 + 2 * 3 - 4 / 5 ** 6
>>> print(x)
7
>>> x = 1 + 2 ** 3 / 4 * 5
>>> print(x)
11
>>> ddd = 1 + 4
>>> print(ddd)
5
>>> eee = 'hello '+ 'there'
>>> print(eee)
hello there
>>> eee	= 'hello ' + 'there'
>>> eee = eee + 1

Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    eee = eee + 1
TypeError: cannot concatenate 'str' and 'int' objects
>>> type(eee)
<type 'str'>
>>> type('hello')
<type 'str'>
>>> type(1)
<type 'int'>
>>> xx = 1
>>> type (xx)
<type 'int'>
>>> temp = 98.6
>>> type(temp)
<type 'float'>
>>> type(1)
<type 'int'>
>>> type(1.00)
<type 'float'>
>>> print(float(99) + 100)
199.0
>>> i = 42
>>> type(i)
<type 'int'>
>>> f = float(i)
>>> print(f)
42.0
>>> type(f)
<type 'float'>
>>> print(10 / 2)
5
>>> print(9 / 2)
4
>>> print(99 / 100)
0
>>> print(10.0 / 2.0)
5.0
>>> print(99.0 / 100.0)
0.99
>>> sval = '123'
>>> type(sval)
<type 'str'>
>>> print(sval + 1)

Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    print(sval + 1)
TypeError: cannot concatenate 'str' and 'int' objects
>>> ival = int(sval)
>>> type(ival)
<type 'int'>
>>> print(ival + 1)
124
>>> nsv = 'hello bob'
>>> niv = int(nsv)

Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    niv = int(nsv)
ValueError: invalid literal for int() with base 10: 'hello bob'
>>> nsm = input('Who are you?')
Who are you?

Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    nsm = input('Who are you?')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> print('Welcome' nam)
SyntaxError: invalid syntax
>>> 
>>> print('Welcome', nam)

Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    print('Welcome', nam)
NameError: name 'nam' is not defined
>>> print('Welcome', nam)

Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    print('Welcome', nam)
NameError: name 'nam' is not defined
>>> Viktorija = input('Who are you?')
Who are you? Viktorija

Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    Viktorija = input('Who are you?')
  File "<string>", line 1, in <module>
NameError: name 'Viktorija' is not defined
>>> Who are you? "Viktorija"
SyntaxError: invalid syntax
>>> Viktorija = input('Who are you?')
Who are you? print('Welcome', Viktorija)

Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    Viktorija = input('Who are you?')
  File "<string>", line 1
    print('Welcome', Viktorija)
        ^
SyntaxError: invalid syntax
>>> "Viktorija" = input('Who are you?')
SyntaxError: can't assign to literal
>>> nam = input('Who are you?')
Who are you? "nam"
>>> print('Welcome', nam)
('Welcome', 'nam')
>>> Viktorija = input('Who are you?')
Who are you? "Viktorija"
>>> print('Welcome', Viktorija)
('Welcome', 'Viktorija')
>>> inp = input('Europe floor?')
Europe floor?int(inp) + 1 

Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    inp = input('Europe floor?')
  File "<string>", line 1, in <module>
NameError: name 'inp' is not defined
>>> big = word

Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    big = word
NameError: name 'word' is not defined
>>> cd

Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    cd
NameError: name 'cd' is not defined
>>> inp = input('Europe floo?')
Europe floo? = int('Europe floo') + 1 

Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    inp = input('Europe floo?')
  File "<string>", line 1
    = int('Europe floo') + 1
    ^
SyntaxError: invalid syntax
>>> inp = input('Europe floor?)
	    
SyntaxError: EOL while scanning string literal
>>> inp = input('Europe floor?')
Europe floor? 0
>>> inp = input('Europe floo?r')
Europe floo?r

Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    inp = input('Europe floo?r')
  File "<string>", line 0
    
    ^
SyntaxError: unexpected EOF while parsing
>>> inp = input('Europe floor?')
Europe floor?"0"
>>> usf = int(inp) + 1
>>> print('US floor', usf)
('US floor', 1)
>>> 
('US floor', 1)
('US floor', 1)
>>> 

