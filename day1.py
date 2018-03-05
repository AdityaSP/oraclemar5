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
>>> 
