Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:24:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print "Hello World"
Hello World
>>> print 'Hello World'
Hello World
>>> print '''Hello World'''
Hello World
>>> print """Hello World"""
Hello World
>>> print '''Hello World
Hello World Again'''
Hello World
Hello World Again
>>> a = 10
>>> b = 2.2
>>> c = True
>>> d = 'Hello'
>>> type(a)
<type 'int'>
>>> a
10
>>> a, b, c, d
(10, 2.2, True, 'Hello')
>>> # something like this
>>> type(b), type(c), type(d)
(<type 'float'>, <type 'bool'>, <type 'str'>)
>>> 10
10
>>> 1000
1000
>>> 'hello'
'hello'
>>> a = d
>>> type(a)
<type 'str'>
>>> a
'Hello'
>>> a
'Hello'
>>> d
'Hello'
>>> id(a)
57209520L
>>> id(d)
57209520L
>>> a = 1000
>>> id(a)
56465144L
>>> a = 1001
>>> id(a)
56465048L
>>> a = 1000
>>> id(a)
56465144L
>>> f = 999 + 1
>>> id(f)
56457512L
>>> a = 10 + 4
>>> a = a * 4
>>> a
56
>>> a = 2 ** 10
>>> a
1024
>>> a = 3
>>> b = 4
>>> a/b
0
>>> a * 1.0/b
0.75
>>> a /b * 1.0
0.0
>>> a /(b * 1.0)
0.75
>>> r = a /(b * 1.0)
>>> r
0.75
>>> type(r)
<type 'float'>
>>> type(a)
<type 'int'>
>>> float(a)
3.0
>>> type(a)
<type 'int'>
>>> type(float(a))
<type 'float'>
>>> a1 = float(a)
>>> a1
3.0
>>> a
3
>>> print type(a)
<type 'int'>
>>> float(a)/b
0.75
>>> print(type(a))
<type 'int'>
>>> a = 'hello'
>>> type(a)
<type 'str'>
>>> a + 'Hi'
'helloHi'
>>> a
'hello'
>>> a = a + 'Hi'
>>> a
'helloHi'
>>> a += ' there'
>>> a
'helloHi there'
>>> a = 'High' + 5

Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a = 'High' + 5
TypeError: cannot concatenate 'str' and 'int' objects
>>> a = '5' + 5

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    a = '5' + 5
TypeError: cannot concatenate 'str' and 'int' objects
>>> a = 'High' + str(5)
>>> a
'High5'
>>> a = 'High' + '5'
>>> 'hello' * 5
'hellohellohellohellohello'
>>> print "-" * 50
--------------------------------------------------
>>> a = 'hello bangalore'
>>> a[0]
'h'
>>> a[6]
'b'
>>> len(a)
15
>>> id(a)
57655344L
>>> id(a[0])
41902968L
>>> a[14]
'e'
>>> a[15]

Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a[15]
IndexError: string index out of range
>>> a[-1]
'e'
>>> a
'hello bangalore'
>>> a[-15]
'h'
>>> a[-16]

Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    a[-16]
IndexError: string index out of range
>>> a
'hello bangalore'
>>> id(a[0]), id(a[1])
(41902968L, 41051440L)
>>> 
>>> a
'hello bangalore'
>>> a[0:5]
'hello'
>>> a[0:200]
'hello bangalore'
>>> a[20348:89]
''
>>> a[-1:-5]
''
>>> a[-5:-1]
'alor'
>>> a[3:-1]
'lo bangalor'
>>> a[5:-12]
''
>>> a[-10:10]
' bang'
>>> a[-3:3]
''
>>> a[-5:-1:1]
'alor'
>>> a[-1:-5:-1]
'erol'
>>> a[5:-12: -1]
' o'
>>> a[-3:3: -1]
'olagnab o'
>>> a[-10:10: -1]
''
>>> a = '0123456789'
>>> len(a)
10
>>> a[-1:-10:-1]
'987654321'
>>> a[-1:-11:-1]
'9876543210'
>>> a[-1: len(a) * -1 -1:-1]
'9876543210'
>>> b = 20
>>> b * -1
-20
>>> -b
-20
>>> a[-1: -len(a) -1:-1]
'9876543210'
>>> a[0:1283012]
'0123456789'
>>> a[0:]
'0123456789'
>>> a[5:]
'56789'
>>> a[0:6]
'012345'
>>> a[:6]
'012345'
>>> a[:]
'0123456789'
>>> a[::1]
'0123456789'
>>> a[::-1]
'9876543210'
>>> a[::2]
'02468'
>>> import os
>>> os.getcwd()
'D:\\sw\\Python27'
>>> a
'0123456789'
>>> a[::1]
'0123456789'
>>> a[::2]
'02468'
>>> a[::-2]
'97531'
>>> a[::3]
'0369'
>>> len(a)
10
>>> id(a)
42224016L
>>> type(a)
<type 'str'>
>>> a.startswith('0')
True
>>> b
20
>>> b.startswith('2')

Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    b.startswith('2')
AttributeError: 'int' object has no attribute 'startswith'
>>> a.endswith('9')
True
>>> url = 'https://google.com'
>>> a.startswith('http')
False
>>> url.startswith('http')
True
>>> a = 'the discovery of India'
>>> a.capitalize()
'The discovery of india'
>>> a.title()
'The Discovery Of India'
>>> a.upper()
'THE DISCOVERY OF INDIA'
>>> a.lower()
'the discovery of india'
>>> a
'the discovery of India'
>>> a.split()
['the', 'discovery', 'of', 'India']
>>> a.upper().split()
['THE', 'DISCOVERY', 'OF', 'INDIA']
>>> l = a.split()
>>> l
['the', 'discovery', 'of', 'India']
>>> type(l)
<type 'list'>
>>> a.split(" ")
['the', 'discovery', 'of', 'India']
>>> b = 'Samuel Jackson,John Trovolta,Uma Thurman,Bruce Wills'
>>> b.split(',')
['Samuel Jackson', 'John Trovolta', 'Uma Thurman', 'Bruce Wills']
>>> b = 'id2001::123::67'
>>> b.split('::')
['id2001', '123', '67']
>>> 'discover'.split('c')
['dis', 'over']
>>> s = 'kalsdlf]\asdf'
>>> s.split('\\')
['kalsdlf]\x07sdf']
>>> s = 'kalsdlf]\\asdf'
>>> s.split('\\')
['kalsdlf]', 'asdf']
>>> s = r'kalsdlf]\asdf'
>>> s.split('\\')
['kalsdlf]', 'asdf']
>>> a = 'India,Japan,USA'
>>> a.split(',')
['India', 'Japan', 'USA']
>>> l = a.split(',')
>>> type(l)
<type 'list'>
>>> l
['India', 'Japan', 'USA']
>>> l[0]
'India'
>>> l = [1,2,3]
>>> l[0]
1
>>> l[-1]
3
>>> l = [1,2,3,'hello']
>>> l = ['India', 'Japan', 'USA']
>>> l[2]
'USA'
>>> l[2][2]
'A'
>>> l[-1][-1]
'A'
>>> l[-1][-1][-1][-1][-1]
'A'
>>> l[2][2]
'A'
>>> l
['India', 'Japan', 'USA']
>>> l[2]
'USA'
>>> l1 = l[2]
>>> l1
'USA'
>>> l1[2]
'A'
>>> l[2][2]
'A'
>>> l = [1,2,3,'hello']
>>> l[0]
1
>>> l[0][-1]

Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    l[0][-1]
TypeError: 'int' object has no attribute '__getitem__'
>>> l[0]
1
>>> a = -1
>>> a = 10
>>> a[-1]

Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    a[-1]
TypeError: 'int' object has no attribute '__getitem__'
>>> l = ['India', 'Japan', 'USA']
>>> l[2] = 'UK'
>>> l
['India', 'Japan', 'UK']
>>> s = 'hello'
>>> s[0]='H'

Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    s[0]='H'
TypeError: 'str' object does not support item assignment
>>> s.replace('h','H')
'Hello'
>>> s
'hello'
>>> s = s.replace('h','H')
>>> s
'Hello'
>>> l
['India', 'Japan', 'UK']
>>> id(l)
56924488L
>>> l[2] = 'USA;
SyntaxError: EOL while scanning string literal
>>> l[2] = 'USA'
>>> id(l)
56924488L
>>> 
>>> s = 'hello bangalore'
>>> s = s.replace('h','H')
>>> s = 'hello bangalore'
>>> id(s)
57647200L
>>> s = s.replace('h','H')
>>> s
'Hello bangalore'
>>> id(s)
57130656L
>>> l
['India', 'Japan', 'USA']
>>> id(l)
56924488L
>>> l[2]='Ukraine'
>>> id(l)
56924488L
>>> l
['India', 'Japan', 'Ukraine']
>>> len(l)
3
>>> l.append('UK')
>>> l
['India', 'Japan', 'Ukraine', 'UK']
>>> b = ['China','USA','USSR']
>>> l.extend(b)
>>> l
['India', 'Japan', 'Ukraine', 'UK', 'China', 'USA', 'USSR']
>>> b
['China', 'USA', 'USSR']
>>> id(l)
56924488L
>>> l = ['India', 'Japan', 'Ukraine']
>>> len(l)
3
>>> len(b)
3
>>> l.append(b)
>>> len(l)
4
>>> l
['India', 'Japan', 'Ukraine', ['China', 'USA', 'USSR']]
>>> l[-1]
['China', 'USA', 'USSR']
>>> l[-1][-1]
'USSR'
>>> l[-1][-1][-1]
'R'
>>> l = ['India', 'Japan', 'Ukraine']
>>> len(l)
3
>>> l.extend('Afghanistan')
>>> len(l)
14
>>> l
['India', 'Japan', 'Ukraine', 'A', 'f', 'g', 'h', 'a', 'n', 'i', 's', 't', 'a', 'n']
>>> l.extend(10)

Traceback (most recent call last):
  File "<pyshell#238>", line 1, in <module>
    l.extend(10)
TypeError: 'int' object is not iterable
>>> l.extend('Afghanistan','Pakistan')

Traceback (most recent call last):
  File "<pyshell#239>", line 1, in <module>
    l.extend('Afghanistan','Pakistan')
TypeError: extend() takes exactly one argument (2 given)
>>> l.extend(
	)

Traceback (most recent call last):
  File "<pyshell#240>", line 1, in <module>
    l.extend(
TypeError: extend() takes exactly one argument (0 given)
>>> l.extend(['Afghanistan','Pakistan'])
>>> l
['India', 'Japan', 'Ukraine', 'A', 'f', 'g', 'h', 'a', 'n', 'i', 's', 't', 'a', 'n', 'Afghanistan', 'Pakistan']
>>> l = ['India', 'Japan', 'Ukraine']
>>> l.insert(2,'USA')
>>> l
['India', 'Japan', 'USA', 'Ukraine']
>>> l.insert(0,'SL')
>>> l
['SL', 'India', 'Japan', 'USA', 'Ukraine']
>>> l.insert(-1, 'UK')
>>> l
['SL', 'India', 'Japan', 'USA', 'UK', 'Ukraine']
>>> l.insert(2000,'UK')
>>> l
['SL', 'India', 'Japan', 'USA', 'UK', 'Ukraine', 'UK']
>>> l
['SL', 'India', 'Japan', 'USA', 'UK', 'Ukraine', 'UK']
>>> l.remove('UK')
>>> l
['SL', 'India', 'Japan', 'USA', 'Ukraine', 'UK']
>>> del l[0]
>>> l
['India', 'Japan', 'USA', 'Ukraine', 'UK']
>>> b
['China', 'USA', 'USSR']
>>> del b
>>> b

Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> l
['India', 'Japan', 'USA', 'Ukraine', 'UK']
>>> l.pop()
'UK'
>>> l
['India', 'Japan', 'USA', 'Ukraine']
>>> l = ['cmd1','cmd2','cmd3']
>>> c = l.pop()
>>> c
'cmd3'
>>> c = l.pop()
>>> c
'cmd2'
>>> c = l.pop()
>>> c
'cmd1'
>>> c = l.pop()

Traceback (most recent call last):
  File "<pyshell#270>", line 1, in <module>
    c = l.pop()
IndexError: pop from empty list
>>> l =['India', 'Japan', 'USA', 'Ukraine']
>>> l.pop(2)
'USA'
>>> l
['India', 'Japan', 'Ukraine']
>>> a = True
>>> 
>>> 
>>> if a:
	print "Truthful"

	
Truthful
>>> if a:
print "Truthful"
  File "<pyshell#280>", line 3
    print "Truthful"
        ^
IndentationError: expected an indented block
>>> if a:
    print "Truthful"

    
Truthful
>>> a = 10
>>> if a < 10:
	print "Single digit"

	
>>> a = -1
>>> a = -100
>>> if a < 10:
	print "Single digit"

	
Single digit
>>> if a > 0 and a < 10:
	print "Single digit"

	
>>> a = 10
>>> if a > 0 and a < 10:
	print "Single digit"

	
>>> if a > 0 and a < 10:
	print "Single digit"
else:
	print "May be 2 digits"

	
May be 2 digits
>>> if a > 0 and a < 10:
	print "Single digit"
elif a > 10 and a < 100:
	print "Double digit"
else:
	print "2+ digits"

	
2+ digits
>>> if a > 0 and a < 10:
	print "Single digit"
else:
	if a < 100:
		print "Double digit"
	else:
		print "2 + digit"

Double digit
>>> 
>>> #'*******************'
>>> a = 10
>>> import random
>>> random.randint(1,3)
2
>>> random.randint(1,3)
1
>>> count = 0
>>> while count < 5:
	a = a + random.randint(1,3)
	count = count + 1

	
>>> a
22
>>> while count < 5:
	a = a + random.randint(1,3)
	count = count + 1

	
>>> a
22
>>> count
5
>>> l = ['KA','TN','TS','UP','HR']
>>> count = 0
>>> while count < len(l):
	print l[count]

	
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA
KA


Traceback (most recent call last):
  File "<pyshell#324>", line 2, in <module>
    print l[count]
  File "D:\sw\Python27\lib\idlelib\PyShell.py", line 1356, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> while count < len(l):
	print l[count]
	count += 1

	
KA
TN
TS
UP
HR
>>> l
['KA', 'TN', 'TS', 'UP', 'HR']
>>> while count < len(l):
	print l[count]
	count += 1

	
>>> count
5
>>> count = 0
>>> while count < len(l):
	print l[count]
	count += 1

	
KA
TN
TS
UP
HR
>>> l
['KA', 'TN', 'TS', 'UP', 'HR']
>>> for item in l:
	print item

	
KA
TN
TS
UP
HR
>>> item
'HR'
>>> for item in l:
	print item

	
KA
TN
TS
UP
HR
>>> l
['KA', 'TN', 'TS', 'UP', 'HR']
>>> ",".join(l)
'KA,TN,TS,UP,HR'
>>> clear

Traceback (most recent call last):
  File "<pyshell#344>", line 1, in <module>
    clear
NameError: name 'clear' is not defined
>>> c1 = [ 1,2,3,4,5]
>>> c2 = ['a','b','c','d','e']
>>> len(c1), len(c2)
(5, 5)
>>> c3 = c1 + c2
>>> c3
[1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
>>> zip(c1, c2)
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
>>> l = [1,'hello']
>>> x = l.pop()
>>> type(x)
<type 'str'>
>>> x
'hello'
>>> l
[1]
>>> x = l.pop()
>>> type(x)
<type 'int'>
>>> x
1
>>> l = ['KA', 'TN', 'TS', 'UP', 'HR']
>>> 'KA' in l
True
>>> 'KA' in l and 'TN' in l
True
>>> ['KA','HR'] in l
False
>>> ['KA','TN'] in l
False
>>> 'KA' in l or 'DL' in l
True
>>> 'KA' in l and 'DL' in l
False
>>> s1 = 'KA'
>>> s1 in l
True
>>> KA in l

Traceback (most recent call last):
  File "<pyshell#368>", line 1, in <module>
    KA in l
NameError: name 'KA' is not defined
>>> 'KA' in l
True
>>> l2 = [1,2,3,5]
>>> 4 in l2
False
>>> '3' in l2
False
>>> 3 in l2
True
>>> l = ['KA','ZZ', 'TN', 'ZZ', TS', 'UP', 'HR', 'ZZ']
     
SyntaxError: invalid syntax
>>> l = ['KA','ZZ', 'TN', 'ZZ', 'TS', 'UP', 'HR', 'ZZ']
>>> len(l)
8
>>> l.count('ZZ')
3
>>> while 'ZZ' in l:
	l.remove('ZZ')

	
>>> l
['KA', 'TN', 'TS', 'UP', 'HR']
>>> range(5)
[0, 1, 2, 3, 4]
>>> r = ''
>>> for i in range(5):
	r = r + "," + str (random.randint(1,10))

	
>>> r
',1,1,2,10,3'
>>> r1 = r.split(',')
>>> r1
['', '1', '1', '2', '10', '3']
>>> int('1')
1
>>> int('')

Traceback (most recent call last):
  File "<pyshell#391>", line 1, in <module>
    int('')
ValueError: invalid literal for int() with base 10: ''
>>> #for i in range(5):
>>> for i in [0,1,2,3,4]:
	print i

	
0
1
2
3
4
>>> r1
['', '1', '1', '2', '10', '3']
>>> for i in r1:
	print r1

	
['', '1', '1', '2', '10', '3']
['', '1', '1', '2', '10', '3']
['', '1', '1', '2', '10', '3']
['', '1', '1', '2', '10', '3']
['', '1', '1', '2', '10', '3']
['', '1', '1', '2', '10', '3']
>>> for i in r1:
	print i

	

1
1
2
10
3
>>> total = 0
>>> for i in r1:
	if i != '':
		total = total + int(i)

		
>>> total
17
>>> r1
['', '1', '1', '2', '10', '3']
>>> r = ''
>>> for i in range(5):
	r = r + "," + str (random.randint(1,10))

	
>>> r
',7,1,3,2,1'
>>> r1 = r.split(',')
>>> total = 0
>>> for i in r1:
	if i != '':
		total = total + int(i)

		
>>> range(5)
[0, 1, 2, 3, 4]
>>> type(range(5))
<type 'list'>
>>> type(range(5)) == list
True
>>> a_t = ()
>>> len(a_t)
0
>>> type(a_t)
<type 'tuple'>
>>> sh  = ('batman','spiderman','superman')
>>> len(sh)
3
>>> type(sh)
<type 'tuple'>
>>> len(sh)
3
>>> sh[1]
'spiderman'
>>> sh  = 'batman','spiderman','superman'
>>> sh
('batman', 'spiderman', 'superman')
>>> sh1, sh2, sh3 = sh
>>> sh1
'batman'
>>> sh2
'spiderman'
>>> sh3
'superman'
>>> a = 10
>>> b = 20
>>> t = b
>>> b = a
>>> a = t
>>> a
20
>>> b
10
>>> a, b = b, a
>>> a
10
>>> b
20
>>> l = [1,2]
>>> a1, a2 = l
>>> a1
1
>>> a2
2
>>> 
>>> c1
[1, 2, 3, 4, 5]
>>> c2
['a', 'b', 'c', 'd', 'e']
>>> zip(c1,c2)
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
>>> zip('hello', 'HELLO')
[('h', 'H'), ('e', 'E'), ('l', 'L'), ('l', 'L'), ('o', 'O')]
>>> c1 = [1, 2, 3, 4]
>>> c2
['a', 'b', 'c', 'd', 'e']
>>> zip(c1,c2)
[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
>>> zip(c1,c2, c1,c2,'hello')
[(1, 'a', 1, 'a', 'h'), (2, 'b', 2, 'b', 'e'), (3, 'c', 3, 'c', 'l'), (4, 'd', 4, 'd', 'l')]
>>> l = zip(c1,c2, c1,c2,'hello')
>>> for item in l:
	print item

	
(1, 'a', 1, 'a', 'h')
(2, 'b', 2, 'b', 'e')
(3, 'c', 3, 'c', 'l')
(4, 'd', 4, 'd', 'l')
>>> for item in l:
	print item[2],item[1]

	
1 a
2 b
3 c
4 d
>>> l = [(1,2,3), (4,5,6)]
>>> t = ([1,2,3], [4,5,6])
>>> 
>>> l.append(4)
>>> l
[(1, 2, 3), (4, 5, 6), 4]
>>> l.pop(0)
(1, 2, 3)
>>> l
[(4, 5, 6), 4]
>>> l[0][2]=5

Traceback (most recent call last):
  File "<pyshell#470>", line 1, in <module>
    l[0][2]=5
TypeError: 'tuple' object does not support item assignment
>>> t = ([1,2,3], [4,5,6])
>>> t[0].pop()
3
>>> t
([1, 2], [4, 5, 6])
>>> t[0].pop()
2
>>> t[0].pop()
1
>>> t
([], [4, 5, 6])
>>> t[0].extend(range(5))
>>> t
([0, 1, 2, 3, 4], [4, 5, 6])
>>> t1 = t
>>> type(t1)
<type 'tuple'>
>>> type(t)
<type 'tuple'>
>>> id(t1)
56804232L
>>> id(t)
56804232L
>>> t[0].count(2)
1
>>> t = (1,2,3,4)
>>> t.count(1)
1
>>> t.index(4)
3
>>> t[3]
4
>>> l = [(1,2,3), (4,5,6)]
>>> type(l)
<type 'list'>
>>> d  = {'name':'Aditya', 'email':'sp.aditya@gmail.com'}
>>> d[0]

Traceback (most recent call last):
  File "<pyshell#492>", line 1, in <module>
    d[0]
KeyError: 0
>>> d['name']
'Aditya'
>>> d['email']
'sp.aditya@gmail.com'
>>> d['city']

Traceback (most recent call last):
  File "<pyshell#495>", line 1, in <module>
    d['city']
KeyError: 'city'
>>> d  = {'name':'Aditya', 'email':'sp.aditya@gmail.com'}
>>> d['city']='Bangalore'
>>> d
{'city': 'Bangalore', 'name': 'Aditya', 'email': 'sp.aditya@gmail.com'}
>>> d['phone']=['0801231231', '083208403']
>>> d
{'city': 'Bangalore', 'name': 'Aditya', 'phone': ['0801231231', '083208403'], 'email': 'sp.aditya@gmail.com'}
>>> l = [d,d,d,d]
>>> l
[{'city': 'Bangalore', 'name': 'Aditya', 'phone': ['0801231231', '083208403'], 'email': 'sp.aditya@gmail.com'}, {'city': 'Bangalore', 'name': 'Aditya', 'phone': ['0801231231', '083208403'], 'email': 'sp.aditya@gmail.com'}, {'city': 'Bangalore', 'name': 'Aditya', 'phone': ['0801231231', '083208403'], 'email': 'sp.aditya@gmail.com'}, {'city': 'Bangalore', 'name': 'Aditya', 'phone': ['0801231231', '083208403'], 'email': 'sp.aditya@gmail.com'}]
>>> len(l)
4
>>> l[0]['phone'][0]
'0801231231'
>>> d  = {'name':'Aditya', 'email':'sp.aditya@gmail.com'}
>>> d['city']='Bangalore'
>>> d
{'city': 'Bangalore', 'name': 'Aditya', 'email': 'sp.aditya@gmail.com'}
>>> d['city']='Bengaluru'
>>> d
{'city': 'Bengaluru', 'name': 'Aditya', 'email': 'sp.aditya@gmail.com'}
>>> d[1] = 'one'
>>> d
{'city': 'Bengaluru', 1: 'one', 'name': 'Aditya', 'email': 'sp.aditya@gmail.com'}
>>> d.keys()
['city', 1, 'name', 'email']
>>> d.values()
['Bengaluru', 'one', 'Aditya', 'sp.aditya@gmail.com']
>>> d.items()
[('city', 'Bengaluru'), (1, 'one'), ('name', 'Aditya'), ('email', 'sp.aditya@gmail.com')]
>>> d = {'city': 'Bangalore', 'name': 'Aditya', 'email': 'sp.aditya@gmail.com'}
>>> #key city has value Bangalore
>>> for item in d.keys():
	print 'key', item , 'has value', d[item]

	
key city has value Bangalore
key name has value Aditya
key email has value sp.aditya@gmail.com
>>> for k in d.keys():
	print 'key', k , 'has value', d[k]

	
key city has value Bangalore
key name has value Aditya
key email has value sp.aditya@gmail.com
>>> for k in d:
	print 'key', k , 'has value', d[k]

	
key city has value Bangalore
key name has value Aditya
key email has value sp.aditya@gmail.com
>>> for item in d.items():
	print item
	print type(item)

	
('city', 'Bangalore')
<type 'tuple'>
('name', 'Aditya')
<type 'tuple'>
('email', 'sp.aditya@gmail.com')
<type 'tuple'>
>>> for item in d.items():
	k = item[0]
	v = item[1]
	print 'key', k, 'has value' v
	
SyntaxError: invalid syntax
>>> for item in d.items():
	k = item[0]
	v = item[1]
	print 'key', k, 'has value', v

	
key city has value Bangalore
key name has value Aditya
key email has value sp.aditya@gmail.com
>>> for item in d.items():
	k,v = item
	print 'key', k, 'has value', v

	
key city has value Bangalore
key name has value Aditya
key email has value sp.aditya@gmail.com
>>> for k,v in d.items():
	print 'key', k, 'has value', v

	
key city has value Bangalore
key name has value Aditya
key email has value sp.aditya@gmail.com
>>> 
>>> 
>>> 
>>> 
>>> 
>>> s = 'hello there good afternoon'
>>> #fh = open('mar6.txt', 'wt')
>>> import os
>>> os.getcwd()
'D:\\sw\\Python27'
>>> fh = open('mar6.txt', 'wt')
>>> fh.write(s)
>>> fh.close()
>>> fh = open('mar6.txt', 'wt')
>>> fh.write(s)
>>> fh.write(s)
>>> fh.close()
>>> fh = open('mar6.txt', 'wt')
>>> fh.write(s)
>>> fh.write('\n')
>>> fh.write(s)
>>> fh.close()
>>> 
>>> 
>>> fh.write(s)

Traceback (most recent call last):
  File "<pyshell#560>", line 1, in <module>
    fh.write(s)
ValueError: I/O operation on closed file
>>> fh = open('mar6.txt', 'at')
>>> fh.write('appened to the file')
>>> fh.close()
>>> 
>>> 
>>> 
>>> 
>>> fh = open('mar6.txt','rt')
>>> fh.write('write')

Traceback (most recent call last):
  File "<pyshell#569>", line 1, in <module>
    fh.write('write')
IOError: File not open for writing
>>> 
>>> 


>>> s = fh.read()
>>> s
'line 1\nline 2\nline 3\nline 4'
>>> s = fh.read()
>>> s
''
>>> fh.seek(0)
>>> s = fh.read()
>>> s
'line 1\nline 2\nline 3\nline 4'
>>> fh.seek(0)
>>> l = fh.readlines()
>>> l
['line 1\n', 'line 2\n', 'line 3\n', 'line 4']
>>> fh.seek(0)
>>> for line in fh:
	print line

	
line 1

line 2

line 3

line 4
>>> fh.open('alsdjflaj')

Traceback (most recent call last):
  File "<pyshell#586>", line 1, in <module>
    fh.open('alsdjflaj')
AttributeError: 'file' object has no attribute 'open'
>>> open('alsdjflaj')

Traceback (most recent call last):
  File "<pyshell#587>", line 1, in <module>
    open('alsdjflaj')
IOError: [Errno 2] No such file or directory: 'alsdjflaj'
>>> fh = open('C:\\Users\\Dell lap\\Desktop\\Python\\oracle\\mar-5-9\\f1.txt', 'wt')
>>> fh.write('something')
>>> fh.close()
>>> fh = open('C:/Users/Dell lap/Desktop/Python/oracle/mar-5-9/f1.txt', 'wt')
>>> fh.write('something again')
>>> fh.close()
>>> fh = open(r'C:\Users\Dell lap\Desktop\Python\oracle\mar-5-9\f2.txt', 'wt')
>>> fh.write('something')
>>> fh.close()
>>> fh = open('mar6.txt','rt')
>>> l1 = fh.readline()
>>> l1
'line 1\n'
>>> fh.tell()
8L
>>> type(fh)
<type 'file'>
>>> fh
<open file 'mar6.txt', mode 'rt' at 0x00000000036636F0>
>>> len(fh)

Traceback (most recent call last):
  File "<pyshell#603>", line 1, in <module>
    len(fh)
TypeError: object of type 'file' has no len()
>>> 
>>> 
>>> 
>>> fh = open(r'C:\Users\Dell lap\Desktop\Python\oracle\mar-5-9\batman.json')
>>> 
>>> data = fh.read()
>>> type(data)
<type 'str'>
>>> data[:100]
'{"Search":[{"Title":"Batman Begins","Year":"2005","imdbID":"tt0372784","Type":"movie","Poster":"http'
>>> import json
>>> data = json.loads(data)
>>> type(data)
<type 'dict'>
>>> data.keys()
[u'Search', u'totalResults', u'Response']
>>> type(data['Search'])
<type 'list'>
>>> len(data['Search'])
10
>>> type(data['Search'][0])
<type 'dict'>
>>> data['Search'][0].keys()
[u'imdbID', u'Year', u'Type', u'Poster', u'Title']
>>> for movie in data['Search']:
	print movie['Title']

	
Batman Begins
Batman v Superman: Dawn of Justice
Batman
Batman Returns
Batman Forever
Batman & Robin
The LEGO Batman Movie
Batman: The Animated Series
The LEGO Batman Movie
Batman: Under the Red Hood
>>> 
>>> 
>>> 
>>> 
>>> def sayhi():
	print "Hi"

	
>>> sayhi()
Hi
>>> def sayhi():
	print "Hi"
	return "Hi"

>>> x = sayhi()
Hi
>>> x
'Hi'
>>> type(x)
<type 'str'>
>>> l = []
>>> l.append(1)
>>> def sayhi():
	return "Hi"

>>> def add(x,y):
	return x + y

>>> add(3,4)
7
>>> x = add(5,6)
>>> print x
11
>>> add(5,add(10,7))
22
>>> len.__doc__
'len(object) -> integer\n\nReturn the number of items of a sequence or collection.'
>>> print len.__doc__
len(object) -> integer

Return the number of items of a sequence or collection.
>>> id.__doc__
"id(object) -> integer\n\nReturn the identity of an object.  This is guaranteed to be unique among\nsimultaneously existing objects.  (Hint: it's the object's memory address.)"
>>> l.append.__doc__
'L.append(object) -- append object to end'
>>> l.sort.__doc__
'L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;\ncmp(x, y) -> -1, 0, 1'
>>> len(10)

Traceback (most recent call last):
  File "<pyshell#654>", line 1, in <module>
    len(10)
TypeError: object of type 'int' has no len()
>>> len.__doc__
'len(object) -> integer\n\nReturn the number of items of a sequence or collection.'
>>> def sayhi():
	'This function says a cheerful Hi'
	return "Hi"

>>> sayhi.__doc__
'This function says a cheerful Hi'
>>> def add(x,y):
	''' add(x,y) -> x + y
returns back addition of x and y'''
	return x + y

>>> add.__doc__
' add(x,y) -> x + y\nreturns back addition of x and y'
>>> print add.__doc__
 add(x,y) -> x + y
returns back addition of x and y
>>> 
>>> 
>>> 
>>> 
>>> def full_name(fn, ln, title)
SyntaxError: invalid syntax
>>> def full_name(fn, ln, title):
	return title.capitalize() + "." + fn + " " + ln

>>> full_name('Aditya','Prabhakara','mr')
'Mr.Aditya Prabhakara'
>>> full_name(fn='Aditya', ln='SP', title='mr')
'Mr.Aditya SP'
>>> full_name('Aditya','Prabhakara')

Traceback (most recent call last):
  File "<pyshell#673>", line 1, in <module>
    full_name('Aditya','Prabhakara')
TypeError: full_name() takes exactly 3 arguments (2 given)
>>> full_name(fn='Aditya', title='mr', ln='SP')
'Mr.Aditya SP'
>>> def full_name(fn, ln, title = 'mr'):
	return title.capitalize() + "." + fn + " " + ln

>>> full_name('Aditya','SP')
'Mr.Aditya SP'
>>> full_name('Aditya','SP', 'Dr')
'Dr.Aditya SP'
>>> full_name( ln='SP', fn='Aditya')
'Mr.Aditya SP'
>>> l = [45,12,78,34,90,32]
>>> sorted(l)
[12, 32, 34, 45, 78, 90]
>>> l
[45, 12, 78, 34, 90, 32]
>>> sorted(l)
[12, 32, 34, 45, 78, 90]
>>> sorted(l)[::-1]
[90, 78, 45, 34, 32, 12]
>>> sorted(l,reverse=True)
[90, 78, 45, 34, 32, 12]
>>> sorted(l,None,None,True)
[90, 78, 45, 34, 32, 12]
>>> sorted(reverse=True, l)
SyntaxError: non-keyword arg after keyword arg
>>> sorted(reverse=True, iterable=l)

Traceback (most recent call last):
  File "<pyshell#688>", line 1, in <module>
    sorted(reverse=True, iterable=l)
TypeError: 'iterable' is an invalid keyword argument for this function
>>> sorted(l, reverse=True)
[90, 78, 45, 34, 32, 12]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def any_args(*args):
	print args
	print type(args)

	
>>> any_args(1,2,3,4)
(1, 2, 3, 4)
<type 'tuple'>
>>> any_args(1,2)
(1, 2)
<type 'tuple'>
>>> add(3,4)
7
>>> #add(1,2,3,4,5)
>>> #add()
>>> #add(1,2,3)
>>> def add(*args):
	total = 0
	for i in args:
		total += i
	return total

>>> add(1,2,3,4,5)
15
>>> add()
0
>>> add(1,2,3)
6
>>> def add(*args):
	return sum(args)

>>> add(1,2,3,4,5)
15
>>> add()
0
>>> add(1,2,3)
6
>>> sum.__doc__
"sum(sequence[, start]) -> value\n\nReturn the sum of a sequence of numbers (NOT strings) plus the value\nof parameter 'start' (which defaults to 0).  When the sequence is\nempty, return start."
>>> str = 'hello'
>>> str(1)

Traceback (most recent call last):
  File "<pyshell#721>", line 1, in <module>
    str(1)
TypeError: 'str' object is not callable
>>> del str
>>> str(1)
'1'
>>> def n_kw(*kwargs):
	print n_kw
	print type(n_kw)

	
>>> def n_kw(**kwargs):
	print n_kw
	print type(n_kw)

	
>>> n_kw(1)

Traceback (most recent call last):
  File "<pyshell#729>", line 1, in <module>
    n_kw(1)
TypeError: n_kw() takes exactly 0 arguments (1 given)
>>> def n_kw(**kwargs):
	print kwargs
	print type(kwargs)

	
>>> n_kw(k = 'x')
{'k': 'x'}
<type 'dict'>
>>> 
