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
>>> sayhi()
'Hi'
>>> def sayhi():
	return "Hi"

>>> sayhi()
'Hi'
>>> a = 10
>>> id(a)
40855376L
>>> id(sayhi)
57933720L
>>> type(a)
<type 'int'>
>>> type(sayhi)
<type 'function'>
>>> b = a
>>> type(b)
<type 'int'>
>>> id(b)
40855376L
>>> greet = sayhi
>>> id(greet)
57933720L
>>> type(greet)
<type 'function'>
>>> greet()
'Hi'
>>> greet = sayhi
>>> x = sayhi()
>>> 
>>> 
>>> 
>>> def f(x):
	print type(x)

	
>>> a
10
>>> f(a)
<type 'int'>
>>> f(sayhi)
<type 'function'>
>>> def f(x):
	print x()

	
>>> f(sayhi)
Hi
>>> sayhi()
'Hi'
>>> print sayhi
<function sayhi at 0x000000000373FF98>
>>> def sayhello():
	return 'Hello'

>>> f(sayhello)
Hello
>>> print sayhi()
Hi
>>> l = [ [5,6,7], [2,9,8], [3,1,7] ]
>>> sorted(l)
[[2, 9, 8], [3, 1, 7], [5, 6, 7]]
>>> sorted.__doc__
'sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list'
>>> 
>>> 
>>> def mykey(item):
	return item[1]

>>> mykey(l[0])
6
>>> mykey(l[1])
9
>>> mykey(l[2])
1
>>> sorted(l, key=mykey)
[[3, 1, 7], [5, 6, 7], [2, 9, 8]]
>>> l = ['Aditya','apple','Azzz']
>>> sorted(l)
['Aditya', 'Azzz', 'apple']
>>> def ic(x):
	return x.lower()

>>> sorted(l, key = ic)
['Aditya', 'apple', 'Azzz']
>>> l = [ [5,6,7], [2,9,8], [3,1,7] ]
>>> 
>>> def mykey(item):
	return item[-1]

>>> sorted(l, key = mykey)
[[5, 6, 7], [3, 1, 7], [2, 9, 8]]
>>> def mysumkey(item):
	return sum(item)

>>> sorted(l, key = mysumkey)
[[3, 1, 7], [5, 6, 7], [2, 9, 8]]
>>> def mysumkey(item):
	print sum(item)
	return sum(item)

>>> sorted(l, key = mysumkey)
18
19
11
[[3, 1, 7], [5, 6, 7], [2, 9, 8]]
>>> l
[[5, 6, 7], [2, 9, 8], [3, 1, 7]]
>>> sum(l[0])
18
>>> def mysumkey(item):
	return sum(item)

>>> sorted(l, key = sum)
[[3, 1, 7], [5, 6, 7], [2, 9, 8]]
>>> sorted(l, key = sum, reverse=True)
[[2, 9, 8], [5, 6, 7], [3, 1, 7]]
>>> sorted('aditya')
['a', 'a', 'd', 'i', 't', 'y']
>>> sorted((4,1,7))
[1, 4, 7]
>>> sum(['a', 'a', 'd', 'i', 't', 'y'])

Traceback (most recent call last):
  File "<pyshell#807>", line 1, in <module>
    sum(['a', 'a', 'd', 'i', 't', 'y'])
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> sum(['a', 'a', 'd', 'i', 't', 'y'], '')

Traceback (most recent call last):
  File "<pyshell#808>", line 1, in <module>
    sum(['a', 'a', 'd', 'i', 't', 'y'], '')
TypeError: sum() can't sum strings [use ''.join(seq) instead]
>>> "".join(['a', 'a', 'd', 'i', 't', 'y'])
'aadity'
>>> ",".join(['a', 'a', 'd', 'i', 't', 'y'])
'a,a,d,i,t,y'
>>> "::".join(['a', 'a', 'd', 'i', 't', 'y'])
'a::a::d::i::t::y'
>>> "/".join(['a', 'a', 'd', 'i', 't', 'y'])
'a/a/d/i/t/y'
>>> kms = [5,10,21,42]
>>> ml = []
>>> for km in kms:
	ml.append(km * 0.62)

	
>>> ml
[3.1, 6.2, 13.02, 26.04]
>>> def tomi(x):
	return x * 0.62

>>> map(tomi, kms)
[3.1, 6.2, 13.02, 26.04]
>>> map(tomi, kms)
[3.1, 6.2, 13.02, 26.04]
>>> map(tomi, kms)
[3.1, 6.2, 13.02, 26.04]
>>> miles = map(tomi, kms)
>>> map.__doc__
'map(function, sequence[, sequence, ...]) -> list\n\nReturn a list of the results of applying the function to the items of\nthe argument sequence(s).  If more than one sequence is given, the\nfunction is called with an argument list consisting of the corresponding\nitem of each sequence, substituting None for missing values when not all\nsequences have the same length.  If the function is None, return a list of\nthe items of the sequence (or a list of tuples if more than one sequence).'
>>> print map.__doc__
map(function, sequence[, sequence, ...]) -> list

Return a list of the results of applying the function to the items of
the argument sequence(s).  If more than one sequence is given, the
function is called with an argument list consisting of the corresponding
item of each sequence, substituting None for missing values when not all
sequences have the same length.  If the function is None, return a list of
the items of the sequence (or a list of tuples if more than one sequence).
>>> 
>>> 
>>> age = [12,67,23,89,23,6,23,89]
>>> new_list = []
>>> for n in age:
	if n > 20 and n < 70:
		new_list.append(n)

		
>>> new_list
[67, 23, 23, 23]
>>> def agerange(x):
	if n> 20 and n < 70:
		return True
	else:
		return False

	
>>> filter(agerange, age)
[]
>>> def agerange(n):
	if n> 20 and n < 70:
		return True
	else:
		return False

	
>>> filter(agerange, age)
[67, 23, 23, 23]
>>> age
[12, 67, 23, 89, 23, 6, 23, 89]
>>> map(agerange, age)
[False, True, True, False, True, False, True, False]
>>> 
>>> 
>>> add(4,5)
9
>>> x = 4
>>> y = 5
>>> add(x,y)
9
>>> 4
4
>>> def sq(x):
	return x * x

>>> lambda x: x * x
<function <lambda> at 0x000000000374D2E8>
>>> sq = lambda x: x * x
>>> sq(6)
36
>>> kms
[5, 10, 21, 42]
>>> map(lambda x : x * .62, kms)
[3.1, 6.2, 13.02, 26.04]
>>> sayhi()
'Hi'
>>> sayhi = 10
>>> sayhi()

Traceback (most recent call last):
  File "<pyshell#866>", line 1, in <module>
    sayhi()
TypeError: 'int' object is not callable
>>> l
[[5, 6, 7], [2, 9, 8], [3, 1, 7]]
>>> map(lambda x : x[1], l)
[6, 9, 1]
>>> sorted(l, key=lambda x : x[1])
[[3, 1, 7], [5, 6, 7], [2, 9, 8]]
>>> sorted(l, key=lambda x : x[3])

Traceback (most recent call last):
  File "<pyshell#870>", line 1, in <module>
    sorted(l, key=lambda x : x[3])
  File "<pyshell#870>", line 1, in <lambda>
    sorted(l, key=lambda x : x[3])
IndexError: list index out of range
>>> sorted(l, key=lambda x : x[2])
[[5, 6, 7], [3, 1, 7], [2, 9, 8]]
>>> 
>>> def agerange(n):
	if n> 20 and n < 70:
		return True
	else:
		return False

	
>>> #filter(agerange, age)
>>> age
[12, 67, 23, 89, 23, 6, 23, 89]
>>> filter(agerange, age)
[67, 23, 23, 23]
>>> filter(lambda x : True if x > 20 and x < 70 else False, age)
[67, 23, 23, 23]
>>> map(lambda x : x * .62, kms)
[3.1, 6.2, 13.02, 26.04]
>>> [ x * 0.62 for x in kms]
[3.1, 6.2, 13.02, 26.04]
>>> y = 20
>>> [
	for x in kms]
SyntaxError: invalid syntax
>>> [ x * 0.62 + y for x in kms]
[23.1, 26.2, 33.019999999999996, 46.04]
>>> [ x * x for x in range(50)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401]
>>> [ x * x for x in range(50) if x %2 == 0]
[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304]
>>> map(lambda x : x * x, filter(lambda x: x%2 ==0, range(50)))
[0, 4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304]
>>> 
>>> 
>>> l = ['ka','tn','ts','up','dl']
>>> for x in l:
	print x

	
ka
tn
ts
up
dl
>>> for x in enumerate(l):
	print x

	
(0, 'ka')
(1, 'tn')
(2, 'ts')
(3, 'up')
(4, 'dl')
>>> for idx, x in enumerate(l):
	print x, 'at', idx

	
ka at 0
tn at 1
ts at 2
up at 3
dl at 4
>>> fh = open(r'C:\Users\Dell lap\Desktop\Python\oracle\mar-5-9\idea\marks.txt')
>>> data = fh.readlines()
>>> data[:5]
['1:44,74,61,54,37,51\n', '2:66,36,91,59,65,79\n', '3:63,74,63,38,69,35\n', '4:71,94,93,91,35,53\n', '5:42,85,91,97,37,100\n']
>>> '    lasdjfk   \n'.strip()
'lasdjfk'
>>> data = [ m.strip() for m in data]
>>> data[:5]
['1:44,74,61,54,37,51', '2:66,36,91,59,65,79', '3:63,74,63,38,69,35', '4:71,94,93,91,35,53', '5:42,85,91,97,37,100']
>>> len(data)
500
>>> data = [ m.split(":") for m in data]
>>> data[:5]
[['1', '44,74,61,54,37,51'], ['2', '66,36,91,59,65,79'], ['3', '63,74,63,38,69,35'], ['4', '71,94,93,91,35,53'], ['5', '42,85,91,97,37,100']]
>>> s = '1:44,74,61,54,37,51'
>>> s = s.split(":")
>>> s
['1', '44,74,61,54,37,51']
>>> s[1].split(",")
['44', '74', '61', '54', '37', '51']
>>> m = s[1].split(",")
>>> m
['44', '74', '61', '54', '37', '51']
>>> map(int, m)
[44, 74, 61, 54, 37, 51]
>>> sum(map(int, m))
321
>>> [ int(x) for x in m]
[44, 74, 61, 54, 37, 51]
>>> data[:5]
[['1', '44,74,61,54,37,51'], ['2', '66,36,91,59,65,79'], ['3', '63,74,63,38,69,35'], ['4', '71,94,93,91,35,53'], ['5', '42,85,91,97,37,100']]
>>> marks = [ m[-1].split(',') for m in data]
>>> marks[:5]
[['44', '74', '61', '54', '37', '51'], ['66', '36', '91', '59', '65', '79'], ['63', '74', '63', '38', '69', '35'], ['71', '94', '93', '91', '35', '53'], ['42', '85', '91', '97', '37', '100']]
>>> marks = [ [m[0], m[-1].split(',')] for m in data]
>>> marks["5]
      
SyntaxError: EOL while scanning string literal
>>> marks[:5]
[['1', ['44', '74', '61', '54', '37', '51']], ['2', ['66', '36', '91', '59', '65', '79']], ['3', ['63', '74', '63', '38', '69', '35']], ['4', ['71', '94', '93', '91', '35', '53']], ['5', ['42', '85', '91', '97', '37', '100']]]
>>> marks = [ [m[0], map(int, m[-1].split(','))] for m in data]
>>> marks[:5]
[['1', [44, 74, 61, 54, 37, 51]], ['2', [66, 36, 91, 59, 65, 79]], ['3', [63, 74, 63, 38, 69, 35]], ['4', [71, 94, 93, 91, 35, 53]], ['5', [42, 85, 91, 97, 37, 100]]]
>>> total_marks=[ [m[0], sum(m[1])] for m in marks]
>>> total_marks[:5]
[['1', 321], ['2', 396], ['3', 342], ['4', 437], ['5', 452]]
>>> 
>>> 
>>> sorted(total_marks, key = lambda x : x[1], reverse=True)[:3]
[['304', 509], ['442', 507], ['231', 505]]
>>> sorted(total_marks, key = lambda x : x[1])[:3]
[['65', 296], ['294', 296], ['404', 304]]
>>> sorted(total_marks, key = lambda x : x[1], reverse=True)[:3]
[['304', 509], ['442', 507], ['231', 505]]
>>> filter(lambda x : x[1] = '67', total_marks)
SyntaxError: lambda cannot contain assignment
>>> filter(lambda x : x[1] == '67', total_marks)
[]
>>> filter(lambda x : x[0] == '67', total_marks)
[['67', 462]]
>>> marks[67]
['68', [95, 57, 64, 82, 92, 97]]
>>> marks[66]
['67', [46, 98, 73, 98, 77, 70]]
>>> sum([46, 98, 73, 98, 77, 70])
462
>>> sum([73,73,99,98,98,98])
539
>>> fh = open(r'C:\Users\Dell lap\Desktop\Python\oracle\mar-5-9\idea\marks.txt')
>>> data = [ line.strip().split(":") for line in fh]
>>> marks = [ [m[0], map(int, m[1].split(','))] for m in data]

>>> total_marks=[ [m[0], sum(m[1])] for m in marks]

>>> print sorted(total_marks, key = lambda x: x[-1], reverse=True)[:3]

[['67', 539], ['304', 530], ['80', 529]]
>>> print sorted(total_marks, key = lambda x: x[-1])[:3]
[['38', 268], ['318', 271], ['36', 279]]
>>> sorted(marks, key = lambda x: sum(x[1]), reverse=True)[:3]
[['67', [73, 73, 99, 98, 98, 98]], ['304', [59, 99, 100, 92, 94, 86]], ['80', [69, 94, 98, 75, 94, 99]]]
>>> len(filter(lambda x: 100 in x[1], marks))
48
>>> len(filter(lambda x: 35 in x[1], marks))
40
>>> len(filter(lambda x: x[1].count(100) > 1, marks))
1
>>> filter(lambda x: x[1].count(100) > 1, marks)
[['439', [74, 100, 100, 58, 55, 91]]]
>>> total_marks[:5]
[['1', 333], ['2', 403], ['3', 384], ['4', 337], ['5', 374]]
>>> d
{'city': 'Bangalore', 'name': 'Aditya', 'email': 'sp.aditya@gmail.com'}
>>> d.items()
[('city', 'Bangalore'), ('name', 'Aditya'), ('email', 'sp.aditya@gmail.com')]
>>> total_d = dict(total_marks)
>>> total_d['200']
422
>>> total_d.keys()[:5]
['344', '345', '346', '347', '340']
>>> total_d.value()[:5]

Traceback (most recent call last):
  File "<pyshell#954>", line 1, in <module>
    total_d.value()[:5]
AttributeError: 'dict' object has no attribute 'value'
>>> total_d.values()[:5]
[421, 415, 340, 460, 396]
>>> len(total_d.keys())
500
>>> 
>>> 
>>> 
>>> def greet():
	def sayhi():
		print "Hi"
	return sayhi

>>> g1 = greet()
>>> g2 = greet()
>>> type(g1)
<type 'function'>
>>> type(g2)
<type 'function'>
>>> g1()
Hi
>>> def greet(name):
	def sayhi():
		print "Hi" , name
	return sayhi

>>> g1 = greet()

Traceback (most recent call last):
  File "<pyshell#972>", line 1, in <module>
    g1 = greet()
TypeError: greet() takes exactly 1 argument (0 given)
>>> def greet(name):
	def sayhi():
		print "Hi" , name
	return sayhi

>>> g1 = greet('Aditya')
>>> g2 = greet('Arun')
>>> g1()
Hi Aditya
>>> g2()
Hi Arun
>>> def greet(name):
	def sayhi():
		print "Hi" , name
		print "Bye", name
	return sayhi

>>> g1 = greet('Aditya')
>>> g1()
Hi Aditya
Bye Aditya
>>> 
>>> 
>>> 
>>> 
>>> def bill_old(item1, item2, tax):
	total = item1 + item2
	grandtotal = total + total * tax
	return grandtotal

>>> bill_old(100,200,.18)
354.0
>>> def bill(item1, item2):
	total = item1 + item2
	def withtax(tax):
		return total + total * tax
	return withtax

>>> b1 = bill(100,200)
>>> 
>>> 
>>> b1(.18)
354.0
>>> bill(100,200)(.18)
354.0
>>> 
>>> 
>>> l1 = ['asd','sadf','sd']
>>> l1 = [l1[0]+l1[1], l[-1]]
>>> l1
['asdsadf', 'dl']
>>> l1 = ['asd','sadf','sd']
>>> l2 = ['qwe','wer','wer]
      
SyntaxError: EOL while scanning string literal
>>> l2 = ['qwe','wer','wer']
>>> zip(l1,l2)
[('asd', 'qwe'), ('sadf', 'wer'), ('sd', 'wer')]
>>> [ fn + " " + ln for fn,ln in zip(l1,l2)]
['asd qwe', 'sadf wer', 'sd wer']
>>> 
>>> 
>>> 
>>> def sayhi():
	print "Hi"

	
>>> sayhi()
Hi
>>> def sayhi():
	print "*" * 30
	print "Hi"
	print "*" * 30

	
>>> sayhi()
******************************
Hi
******************************
>>> def sayhi():
	print "Hi"

	
>>> def deco(f):
	def wrapper():
		print "*" * 30
		f()
		print "*" * 30
	return wrapper

>>> sayhi()
Hi
>>> deco(sayhi)()
******************************
Hi
******************************
>>> def greet():
	print "Hello"

	
>>> deco(greet)()
******************************
Hello
******************************
>>> def deco(f):
	def wrapper():
		print "@" * 30
		f()
		print "@" * 30
	return wrapper

>>> def deco2(f):
	def wrapper():
		print "@" * 30
		f()
		print "@" * 30
	return wrapper

>>> def deco(f):
	def wrapper():
		print "*" * 30
		f()
		print "*" * 30
	return wrapper

>>> deco2(sayhi)()
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Hi
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
>>> deco1(sayhi)()

Traceback (most recent call last):
  File "<pyshell#1047>", line 1, in <module>
    deco1(sayhi)()
NameError: name 'deco1' is not defined
>>> deco(sayhi)()
******************************
Hi
******************************
>>> def deco(f):
	def wrapper():
		print "*" * 30
		f()
		print "*" * 30
	return wrapper

>>> sayhi()
Hi
>>> deco(sayhi)
<function wrapper at 0x000000000374D668>
>>> s1 = deco(sayhi)
>>> s1()
******************************
Hi
******************************
>>> @deco
def sayhi():
	print "Hi"

	
>>> sayhi()
******************************
Hi
******************************
>>> sayhi()
******************************
Hi
******************************
>>> @deco2
@deco
def sayhi():
	print "Hi"

	
>>> sayhi()
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
******************************
Hi
******************************
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
>>> import time
>>> time.sleep(2)
>>> 
>>> 
>>> def hardwork():
	print "Doing work"
	time.sleep(random.randint(1,4))
	print "Done"

	
>>> hardwork()
Doing work
Done
>>> time.time()
1520418874.9
>>> time.time()
1520418879.207
>>> def timer(f):
	def wrapper():
		s = time.time()
		f()
		e = time.time()
		print "It took:", e -s
	return wrapper

>>> @timer
def hardwork():
	print "Doing work"
	time.sleep(random.randint(1,4))
	print "Done"

	
>>> hardwork()
Doing work
Done
It took: 2.09100008011
>>> hardwork()
Doing work
Done
It took: 1.03299999237
>>> time.time()
1520419227.826
>>> time.time()
1520419231.933
>>> 1520419231/60
25340320
>>> 25340320/24
1055846
>>> 1055846/365
2892
>>> d = { x: x**3 for x in range(10) }
>>> d.keys()
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> d.values()
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
>>> d
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729}
>>> d[9]
729
>>> a = 'a quick brown fox jumps over a lazy dog'
>>> a = 'a quick brown fox jumps over the lazy dog'
>>> d = { x: a.count(x) for x in a}
>>> len(a)
41
>>> d
{' ': 8, 'a': 2, 'c': 1, 'b': 1, 'e': 2, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 4, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 2, 'u': 2, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}
>>> d = { x: a.count(x) for x in a if a.count(x) > 1}
>>> d
{'a': 2, ' ': 8, 'e': 2, 'o': 4, 'r': 2, 'u': 2}
>>> reduce( lambda x ,y : x + y , range(10))
45
>>> reduce(lambda x, y : x * y , range(1,6))
120
>>> reduce(lambda x, y : x * y , range(1,11))
3628800
>>> random.random()
0.9636562614832614
>>> g = [random.random() for x in range(100)]
>>> g
[0.9464168444119274, 0.7727879470583112, 0.647139101657822, 0.9887971507120785, 0.0357596747319765, 0.2178854030203713, 0.39019918513569785, 0.44639212608969625, 0.8556172848994607, 0.26499861596278274, 0.6517105641818026, 0.8131082127086828, 0.21208210004677686, 0.883252538214201, 0.4769668060784086, 0.44847982043118517, 0.8537768004824609, 0.4219862384671348, 0.1433032947393834, 0.1015095985313561, 0.3648823693942559, 0.22775971085316038, 0.9262949860925042, 0.9446674332023383, 0.29053350243228315, 0.2716504204969725, 0.08973010401279524, 0.14612408600824234, 0.04777706855413533, 0.40936073836400133, 0.4224768352832793, 0.5217669128731575, 0.6248296663814377, 0.3610101177805517, 0.9234244119269849, 0.7944855248488525, 0.14710690899471102, 0.38366966913631184, 0.5696262371027203, 0.11956894583969435, 0.0113180163851766, 0.6147477405811749, 0.18609159540842113, 0.2834642248523759, 0.64089259317699, 0.5197120522491856, 0.7071065297669643, 0.3023323311348626, 0.07862284453422341, 0.688032555324761, 0.18190183636688417, 0.7702372828822115, 0.4505411594949149, 0.814171699735292, 0.9437525742180738, 0.9044919307869571, 0.6394731907451454, 0.21945391124756808, 0.4276959019439831, 0.24233660786837097, 0.2955231930772907, 0.1691252286890631, 0.9236194211405201, 0.6775141269410102, 0.3688174863774326, 0.522344410290247, 0.35308280211297227, 0.128231392031664, 0.6746842007467472, 0.11721279563667975, 0.7310089094463568, 0.2861777592588767, 0.4505585818057001, 0.16063672772542414, 0.6135764199194137, 0.3991529582530521, 0.24884431804230134, 0.08432704433316518, 0.2451071818857291, 0.5634127519461128, 0.00013438996511583312, 0.6681502597611206, 0.04545542474187869, 0.1570049896046688, 0.15512378532187476, 0.12295483941523577, 0.455287725670777, 0.7240238534613334, 0.39396590249553876, 0.4037512092564898, 0.3244262148199183, 0.1251738418501308, 0.59796502117954, 0.29004041808324255, 0.321239735713464, 0.598291995732516, 0.20768913040735348, 0.06688358434001451, 0.3488491649843414, 0.5143328724608276]
>>> reduce(lambda x, y: x if x<y else y, g)
0.00013438996511583312
>>> reduce(lambda x, y: x if x>y else y, g)
0.9887971507120785
>>> min(g)
0.00013438996511583312
>>> max(g)
0.9887971507120785
>>> 
