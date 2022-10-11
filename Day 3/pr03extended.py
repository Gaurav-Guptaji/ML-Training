Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
m=[12,'hi',2.3,500]
m
[12, 'hi', 2.3, 500]
m.append('abc')
m
[12, 'hi', 2.3, 500, 'abc']
m.append('x','y')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    m.append('x','y')
TypeError: list.append() takes exactly one argument (2 given)
m.extend('x','y','kuch bhi')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    m.extend('x','y','kuch bhi')
TypeError: list.extend() takes exactly one argument (3 given)
m.extend(['x','y','kuch bhi'])
m
[12, 'hi', 2.3, 500, 'abc', 'x', 'y', 'kuch bhi']
m.insert(2,'hello')
m
[12, 'hi', 'hello', 2.3, 500, 'abc', 'x', 'y', 'kuch bhi']
m.pop()
'kuch bhi'
m.pop()
'y'
mp=m.pop()
mp
'x'
m.clear()
m
[]
s={1,1,2,3,3,4}
type(s)
<class 'set'>
s.add(100)
s
{1, 2, 3, 100, 4}
s.discard(100)
s
{1, 2, 3, 4}
s.remove(3)
s
{1, 2, 4}
s1={44,22,23}
s.update(s1)
s
{1, 2, 4, 44, 22, 23}
s.clear()
s
set()
