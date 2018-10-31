Python 3.6.5 (default, Apr  1 2018, 05:46:30) 
[GCC 7.3.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> open("teksts.txt" , "r")
<_io.TextIOWrapper name='teksts.txt' mode='r' encoding='UTF-8'>
>>> fhand= open('mbox.txt')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    fhand= open('mbox.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'mbox.txt'
>>> fhand = open('mbox.txt')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    fhand = open('mbox.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'mbox.txt'
>>> fhand = open('teksts.txt')
>>> print(fhand)
<_io.TextIOWrapper name='teksts.txt' mode='r' encoding='UTF-8'>
>>> fhand = open('stuff.txt')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    fhand = open('stuff.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'stuff.txt'
>>> stuff = 'Hello\nWorld!'
>>> stuff
'Hello\nWorld!'
>>> print(stuff)
Hello
World!
>>> stuff = 'X\nY'
>>> print(stuff)
X
Y
>>> len(stuff)
3
>>> xfile = open('teksts.txt')
>>> for cheese in xfile:
	print(cheese)

Faila slides



>>> fhand = open('teksts.txt')
>>> count = 0
>>> for line in fhand:
	count = count + 1
	print('Line Count:', count)
	& python open.py
	
SyntaxError: invalid syntax
>>> fhand = open('teksts.txt')
>>> count = 0
>>> for line in fhand:
	count = count + 1
	print('Line Count:', count)
	$ python open.py
	
SyntaxError: multiple statements found while compiling a single statement
>>> fhand = open('teksts.txt')
>>> count = 0
>>> for line in fhand:
	count = count + 1
	print('Line Count:', count)
	$ python open.py
	
SyntaxError: multiple statements found while compiling a single statement
>>> fhand = open('teksts.txt')
>>> fhand = open('teksts.txt')
>>> count = 0
>>> for line in fhand:
	count = count + 1
print('Line Count:', count)
SyntaxError: multiple statements found while compiling a single statement
>>> fhand = open(teksts.txt')
		 
SyntaxError: EOL while scanning string literal
>>> fhand = open('teksts.txt')
		 
>>> count = 0
		 
>>> for line in fhand:
       count = count + 1
print('Line Count:' count)
		 
SyntaxError: invalid syntax
>>> fhand = open('teksts.txt')
		 
>>> count = 0for line in fhand:
       count = count + 1
 print('Line Count:' count)
		 
SyntaxError: multiple statements found while compiling a single statement
>>> Reading the *Whole* File
We can 
read
the whole 
file (newlines and all) 
into a 
single string
>>> fhand = open('teksts-short.txt')
>>> inp = fhand.read()
>>> print(len(inp))
94626
>>> print(inp[:20])
		 
SyntaxError: invalid syntax
>>> Reading the *Whole* File
We can
read
the whole
file (newlines and all)
into a
single string
>>> fhand = open('teksts-short.txt')
>>> inp = fhand.read()
>>> print(len(inp))
94626
>>> print(inp[:20])
		 
SyntaxError: invalid syntax
>>> fhand = open('text-short.txt')
		 
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    fhand = open('text-short.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'text-short.txt'
>>>  open("teksts-short.txt" , "r")
		 
SyntaxError: unexpected indent
>>> open("teksts-short.txt" , "r")
		 
<_io.TextIOWrapper name='teksts-short.txt' mode='r' encoding='UTF-8'>
>>> 
>>> fhand = open('teksts-short.txt')
>>> inp = fhand.read()
>>> print(len(inp))
94626
>>> print(inp[:20])
		 
SyntaxError: invalid syntax
>>> fhand = open('teksts-short.txt')
>>> inp = fhand.read()
>>> print(len(inp))
94626
>>> print(inp[:20])
		 
SyntaxError: multiple statements found while compiling a single statement
>>> fhand = open('teksts-short.txt')
		 
>>> inp = fhand.read()
		 
>>> print(len(inp))
		 
387
>>> print(inp[:20])
		 
From 
stephen.marqua
>>> fhand = open('teksts-short.txt')
		 
>>> for linr in fhand:
	hig
		 exit()
		 
SyntaxError: unexpected indent
>>> fhand = open('tekts-short.txt')
		 
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    fhand = open('tekts-short.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'tekts-short.txt'
>>> open('text-short.txt'°
	 
SyntaxError: invalid character in identifier
>>> open('text-short.txt')
	 
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    open('text-short.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'text-short.txt'
>>> fhand = open('teksts-short.txt')
	 
>>> for line in fhand:
	 if line.startwith('From:'):
	 print(line)
	 
SyntaxError: expected an indented block
>>> fhand = open('teksts-short.txt')
	 
>>> for line in fhand:
      if line.startwith('From:'):
	  print(line)
	 
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> fhand = open('mbox-short.txt')forlineinfhand:ifline.startswith('From:') :print(line
										   
SyntaxError: invalid syntax
>>> fhand = open('mbox-short.txt')forlineinfhand:ifline.startswith('From:') :print(line
										   
SyntaxError: invalid syntax
>>> fhand = open('teksts-short.txt')
										   
>>> for line in fhand:
       if line.startwith('From:'):
         print(line)
										   exit()
										   
SyntaxError: unexpected indent
>>> fhand = open('tekts-short.txt')
										   
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    fhand = open('tekts-short.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'tekts-short.txt'
>>> open("teksts.txt" , "r")
										   
<_io.TextIOWrapper name='teksts.txt' mode='r' encoding='UTF-8'>
>>> fhand = open('teksts-short.txt')
										   
>>> for line in fhand:
     line = line.rstrip()
     if line.startswith('From:'):
          print(line)

From:
>>> stephen.marquard@uct.ac.za
										   
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    stephen.marquard@uct.ac.za
NameError: name 'stephen' is not defined
>>> fhand = open('teksts-short.txt')
										   
>>> for line in fhand:
       line = line.rstrip()
       if not line.starstwith('From:'):
         continue
       print(line)
    fhand = open('teksts-short.txt')
										   
SyntaxError: unindent does not match any outer indentation level
>>> 
