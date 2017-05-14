#!/usr/bin/env python

# 
# For & While Loops 
# 

# l_1=[1,2,3]
# l_2=[4,5,6]
# l_3=[7,8,9]
# matrix = [l_1, l_2, l_3]
# first_col = [row[0] for row in matrix]

# d = { 
# 	'k1': {
# 		'nestkey': {
# 			'subnestkey':'subnestvalue'
# 			}, 
# 		'nestkey2' : 'nestvalue2'
# 	}, 
# 	'k2':'value2'
# }

# print d['k1'] ['nestkey'] ['subnestkey']

# d = {}
# d['k1'] = 1;
# d['k2'] = 2;
# d['k3'] = 3;

# print d.keys()
# print d.values()
# print d.items()

# f = open('test.txt')
# print f.read()
# print f.read()
# f.seek(0)
# print f.read()
# f.seek(0)
# print f.readlines()

# for line in open("test.txt"):
# 	print line
# x = False
# if x:
# 	print "x was true"
# elif x == False :
# 	print "x was false"
# else:
# 	print "I shouldl never print this"
# x = 0
# while x < 10:
# 	print 'x is currently ',x
# 	print 'adding 1 to x'
# 	x += 1

# 	if x == 3:
# 		print 'x = 3'
# 		break
# 	else:
# 		print 'continuing...'
# 		continue
# else:
# 	print "all done"

# start = 0
# stop = 20
# step = 3

# print range(start,stop,step)

# l = [1,2,3,4,5]
# for num in l:
# 	print num

# for num in xrange(1,6):
# 	print num

# xr = xrange(1,6)
# for num in xr:
# 	print num

# l = []
# for letter in 'word':
# 	l.append(letter)

# print l

# 
# List comprehensions
# 

# l = [letter for letter in 'word']
# print l

# lst = [x**2 for x in range(0,11)]

# print lst

# lst = []
# for number in range(11):
# 	if number % 2 == 0:
# 		lst.append(number)

# print lst

# lst = [number for number in range(11) if number % 2 == 0]

# print lst

# celsius = [0,10,20.1,34.5]
# fahrenheit = [(temp * (9/5.0) + 32 )for temp in celsius]
# print fahrenheit

# lst = [x**2 for x in [x**2 for x in range(11)]]
# print lst

# 
# Functions
# 

# def name_of_function(arg1,arg2):
# 	pass

# name_of_function(1,2)

# def my_addition_func(arg1,arg2):
# 	"""
# 	My Document string
# 	"""
# 	print arg1+arg2

# my_addition_func(1,2)

# def greeting(name):

# 	print 'hello ',name

# greeting('Tarry')

# def add_num(x,y):
# 	return x+y

# x = add_num(1,2)
# print x

# def is_prime(x):
# 	"""
# 	This function checks for prime

# 	Input: Number
# 	Output: print statement wheter number is or is not prime
# 	"""

# 	for n in range(2,x):
# 		if x % n == 0:
# 			print "Not Prime"
# 			break
# 	else:
# 		print "Is Prime"

# is_prime(13)

# 
#  lambda expresions
# 

# def square(num):
# 	result = num**2
# 	return result

# print square(4)	

# sq = lambda num: num**2

# print sq(5)

# even = lambda num: num%2 == 0
# print even(10)
# print even(9)

# rev = lambda s: s[::-1]
# print rev("hello")
# print rev('a man a plan a canal panama')

# adder = lambda x,y: x+y
# print adder(5,7)


# 
#  OOP
# 

# class Sample(object):
# 	pass

# x = Sample()

# print type(x)

# class Dog(object):

# 	# Class Object Attribute - all instances get this
# 	species = 'mammal'
	
# 	def __init__(self,breed, name):
# 		self.breed = breed
# 		self.name = name

# fido = Dog(breed='Lab', name='Bugger')
# print fido.breed
# print fido.species
# print fido.name

# class Circle(object):

# 	# Class Object Attribute - all instances get this
# 	pi = 3.14
	
# 	def __init__(self,radius=1):
# 		self.radius = radius
# 		self.calculate_area_perimeter()

# 	def calculate_area_perimeter(self):
# 		self.diameter = self.radius * 2
# 		self.area = (self.radius**2) * Circle.pi
# 		self.perimeter = self.diameter * Circle.pi

# 	def get_area(self):
# 		return self.area

# 	def get_perimeter(self):
# 		return self.perimeter

# 	def set_radius(self, new_radius):
# 		self.radius = new_radius
# 		self.calculate_area_perimeter()	

# 	def get_radius(self):
# 		return self.radius

# 	def get_diameter(self):
# 		return self.diameter		

# c = Circle(radius=5)
# print c.pi
# print c.radius
# print c.get_area()

# print c.set_radius(10)
# print c.get_radius()
# print c.get_area()
# print c.get_perimeter()

# class Animal(object):

# 	def __init__(self):
# 		print "animal created"

# 	def whoAmI(self):
# 		print "animal"

# 	def eat(self):
# 		print 'eating'

# class Dog(Animal):

# 	def __init__(self):
# 		Animal.__init__(self)
# 		print 'Dog created'	

# 	def whoAmI(self):
# 		print 'Dog'

# 	def speak(self):
# 		print 'Bark'

# a = Animal()
# a.whoAmI()

# d =Dog()
# d.whoAmI()
# d.speak()
# d.eat()


# 
# Special Methods
# 

# class Book(object):

# 	def __init__(self,title,author,pages):
# 		print 'a book has been created'
# 		self.title = title
# 		self.author = author
# 		self.pages = pages

# 	def __str__(self):
# 		return "Title: %s, Author: %s pages: %s" %(self.title,self.author,self.pages)

# 	def __len__(self):
# 		return self.pages

# 	def __del__(self):
# 		print "Book is gone"

# b = Book('Outer Limits','Tarry Cutler', 100)

# print b
# print len(b)
# del b
# print b.title

# 
# Errors and exception handling
# 

# try:
# 	2 + 's'

# except:
# 	print 'there was an exception'

# finally:
# 	print 'finally!'

# try:
# 	f = open('mrbig.txt','w')
# 	f.write('test to write')
# except:
# 	print 'there was an exception'
# else:
# 	print 'file write was successfull'
# finally:
# 	print 'finally!'

# def askint():
# 	try:
# 		val = int(raw_input('Please enter an integer: '))
# 	except:
# 		print 'no integer'
# 		val = int(raw_input('Tryy again - Please enter an integer: '))
# 	finally:
# 		print 'finaly'
# 	print val

# askint()

# def askint():

# 	while True:
# 		try:
# 			val = int(raw_input('Please enter an integer: '))
# 		except:
# 			print 'Try again no integer'
# 			continue
# 		else:
# 			print 'corrcet!'
# 			break	
# 		finally:
# 			print 'finaly'

# 	print val

# askint()


# 
# modules and how to use them
# 

# import math
# print math.sqrt(4)

# or use 

# from math import sqrt
# print sqrt(4)

# 
# map
# 

# def fahrenheit(T):
# 	return (9.0/5)*T + 32

# x = fahrenheit(0)
# print x

# temp = [0,22.5,40,100]

# x = map(fahrenheit, temp)
# print x

# x = map(lambda T: (9.0/5)*T + 32, temp)
# print x

# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]

# x = map(lambda x,y: x+y,a,b)
# print x

# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]

# x = map(lambda x,y,z: x+y+z,a,b,c)
# print x

# a = [1,2,3]
# x = map(lambda num: num*-1, a)
# print x

# 
# reduce
# 

# lst = [47,11,42,13]
# x = reduce(lambda x,y: x+y,lst)
# print x

# z = [34,23,24,24,100,2333,2,11]
# x = reduce(lambda a, b : a if (a>b) else b, z)
# print x

# z = [34,23,24,24,100,2333,2,11]
# def max_find(a,b):
# 	if ( a > b ):
# 		return a
# 	else:
# 		return b

# x = reduce(lambda a, b: max_find(a, b) , z)
# print x

# 
# filter
# 

# def even_check (num):
# 	if num % 2 == 0:
# 		return True
# 	else:
# 		return False

# def even_check2 (num):
# 	return num % 2 == 0

# x = even_check2(24)
# print x		

# x = even_check2(5)
# print x	

# lst = range(10)
# print lst

# # x = filter(even_check, lst)
# # print x

# # x = filter(lambda a : a % 2 == 0, lst)
# # print x

# x = filter(lambda a : a > 3, lst)
# print x

# 
# zip
# 

# x = [1,2,3]
# y = [4,5,6]

# x = zip(x,y)
# print x

# a = [1,2,3,4,5]
# b = [2,2,10,1,1]

# for pair in zip(a,b):
# 	print max(pair)

# x = map(lambda pair: max(pair),zip(a,b) )	

# x = [1,2,3]
# y = [4,5,6,7,8]
# x = zip(x,y)
# print x

# d1 = {'a':1,'b':2}
# d2 = {'c':4,'d':5}
# x = zip(d1,d2)
# print x

# x = zip(d1,d2.itervalues())
# print x

# def switcheroo(d1,d2):
# 	dout = {}

# 	for d1key, d2val in zip(d1,d2.itervalues()):
# 		dout[d1key] = d2val

# 	return dout

# x = switcheroo(d1,d2)
# print x

# 
# enumerate
# 

# lst = ['a','b','c']

# for count,item in enumerate(lst):
# 	print count
# 	print item

# for count,item in enumerate(lst):
# 	print (count,item)

# 
# all() and any()
# 

# l = [True,True,False,False]

# x = all(l)
# print x

# x = any(l)
# print x

# 
# complex()
# 

# x = complex(2,3)
# print x

# x = complex('10+2j')
# print x

# 
# Decorators
# 

# def hello(name="Tarry"):
# 	print 'Hello '+name

# greet = hello

# hello()
# greet()
# del hello
# greet()
# hello()

# def hello(name='Will'):

# 	def greet():

# 		return '\t This is inside the greet() function'

# 	def welcome():
	
# 		return '\t This is inside the welcome() function'

# 	if name =='Will':
# 		return greet
# 	else:
# 		return welcome

# x = hello
# print x
# x = hello()
# print x
# print x()

# def hello():
# 	return 'Hi Will!'

# def other(func):
# 	print 'Other code goes here!'
# 	print func()

# other(hello)

# def new_decorator(func):

# 	def wrap_func():
# 		print 'Code here, before executing the func()'

# 		func()

# 		print 'Code here will execute after the func()'

# 	return wrap_func

# def func_needs_decorator():
# 	print 'This function needs a decorator!'

# func_needs_decorator = new_decorator(func_needs_decorator)

# func_needs_decorator()

# print func_needs_decorator

# def new_decorator(func):

# 	def wrap_func():
# 		print 'Code here, before executing the func()'

# 		func()

# 		print 'Code here will execute after the func()'

# 	return wrap_func

# @new_decorator
# def func_needs_decorator():
# 	print 'This function needs a decorator!'

# func_needs_decorator()

# 
# Iterators and Generators
# 

# def gencubes(n):
# 	for num in range(n):
# 		yield num**3

# for x in gencubes(10):
# 	print x

# def genfibon(n):
# 	a = 1
# 	b = 1

# 	for i in range(n):
# 		yield a

# 		t = a 
# 		a = b
# 		b = t+b

# for x in genfibon(10):
# 	print x

#   OR

# using tuple unpacking
# def genfibon(n):
# 	a = 1
# 	b = 1

# 	for i in range(n):
# 		yield a

# 		a,b  = b, a + b

# for x in genfibon(10):
# 	print x

# def simple_gen():
# 	for x in range(3):
# 		yield x
# g = simple_gen()

# print next(g)
# print next(g)
# print next(g)

# s = 'hello'
# for let in s:
# 	print let

# s_iter = iter(s)
# print next(s_iter)
# print next(s_iter)
# print next(s_iter)
# print next(s_iter)
# print next(s_iter)

# 
# import urllib2
# 
# import urllib2
# response = urllib2.urlopen('http://www.myexternalip.com/raw')
# html = response.read()
# print html


# 
# Collections module
# 

# from collections import Counter

# l = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,312,1,2,5,5,5]
# x = Counter(l)
# print x

# s = 'hello'
# x = Counter(s)
# print x

# s = 'How often does this word show up in this long sentance string this is easy often'
# words = s.split()
# x = Counter(words)
# print x

# print x.most_common(3)
# print sum(x.values())

# from collections import defaultdict

# d = {'k1':1}
# print d['k1']

# d = defaultdict(object)
# print d['one']

# for item  in d:
# 	print item

# d = defaultdict(lambda: 0)
# d['one']
# d['two'] = 2
# print d

# print 'normal dictionary'

# d ={}

# d['a'] = 'A'
# d['b'] = 'B'
# d['c'] = 'C'
# d['d'] = 'D'
# d['e'] = 'E'

# for k, v in d.items():
# 	print k,v

# print 'normal dictionary'

# d ={}

# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# d['d'] = 4
# d['e'] = 5

# for k, v in d.items():
# 	print k,v	

# from collections import OrderedDict

# print 'ordered dictionary'

# d = OrderedDict()

# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# d['d'] = 4
# d['e'] = 5

# for k, v in d.items():
# 	print k,v

# d1 = {}
# d1['a'] = 1
# d1['b'] = 2

# d2 = {}
# d2['b'] = 2
# d2['a'] = 1

# print d1 == d2

# from collections import OrderedDict

# d1 = OrderedDict()
# d1['a'] = 1
# d1['b'] = 2

# d2 = OrderedDict()
# d2['b'] = 2
# d2['a'] = 1

# print d1 == d2

# t = (1,2,3)
# print t[0]

# from collections import namedtuple

# Dog = namedtuple('Dog','age breed name')
# sam = Dog(age=2,breed='Lab',name='Bugger')
# print sam.name


# Cat = namedtuple('Cat','fur claws name')
# c = Cat(fur='Fuzzy', claws=False, name='pussy')
# print c.claws

# 
# Datetime module
# 

# import datetime

# t = datetime.time(5,25,1)
# print t
# print t.hour
# print t.minute
# print t.microsecond

# print datetime.time.min
# print datetime.time.max
# print datetime.time.resolution

# d = datetime.date.today()
# print d

# print d.timetuple()
# print d.day
# print d.month
# print d.year

# d1 = datetime.date(2015,3,11)
# print d1

# d2 = d1.replace(year=1990)
# print d2

# print d1-d2 

# 
# python debugger - pdb
# 

# import pdb

# x = [1,2,3]
# y = 2
# z = 3

# result = y + z
# print result

# pdb.set_trace()

# result2 = y + x
# print result2

# 
# timing your code - timet module
# 

# import timeit

# print timeit.timeit (' "-".join(str(n) for n in range(100))',number=10000 )
# print timeit.timeit (' "-".join([str(n) for n in range(100)])',number=10000 )
# print timeit.timeit (' "-".join(map(str,range(100)))',number=10000 )

# 
# regular expressions - re module
# 

# import re

# patterns = ['term1', 'term2']
# text = 'This is a string with term1, bur not the other term'

# x = re.search(patterns[0],text)
# print x.start()
# print x.end()

# split_term = '@'
# phrase = 'What is your email, is it hello@gmail.com?'
# x = re.split(split_term,phrase)
# print x

# x = re.findall('match','Here is one match, here is anothermatch')
# print x


# 
# stringio module
# 

# import StringIO

# message = 'This is an ordinary string'

# f = StringIO.StringIO(message)
# x = f.read()
# print x

# f.write(' Second line written to ordanary string')
# f.seek(0)
# x = f.read()
# print x

# 
# advanced numbers and number functions 
# 

# print hex(16)
# print bin(128)
# print pow(2,4)
# print pow(2,4,3)
# print abs(-1.5)
# print round(3)
# print round(3.5)
# print round(3.59,1)

# 
# advanced strings and string functions 
# 

# s = 'hello world'
# print s.capitalize()
# print s.upper()
# print s.lower()
# print s.count('o')
# print s.find('o')

# print s.center(20,'z')

# print 'hello\thi'
# print 'hello\thi'.expandtabs()

# s = 'hello'
# print s.isalnum()
# print s.isalpha()
# print s.isdigit()
# print s.islower()
# print s.isspace()
# print s.istitle()
# print s.isupper()
# print s.endswith('o')
# print 'HELLO'.isupper()

# print s.split('e')
# print 'hehhehhhehhhhehe'.split('e')

# s = 'hiihhihihihhhi'
# print s.partition('i')


# 
# advanced sets
# 

# s  = set()
# s.add(1)
# s.add(2)
# print s

# print s.clear()

# s = {1,2,3}
# sc = s.copy()
# print sc

# print s.add(4)
# print s.difference(sc)

# s1 = {1,2,3}
# s2 = {1,4,5}

# print s1
# print s2
# s1.difference_update(s2)
# print s1

# s = {1,2,3,4}
# print s
# s.discard(2)
# print s

# s1 = {1,2,3}
# s2 = {1,2,4}
# print s1.intersection(s2)
# print s1

# s1 = {1,2,3}
# s2 = {1,2,4}
# s1.intersection_update(s2)
# print s1

# s1 = {1,2}
# s2 = {1,2,4}
# s3 = {5}

# print s1.isdisjoint(s2)
# print s1.isdisjoint(s3)

# print s1.issubset(s2)
# print s2.issuperset(s1)

# print s1.symmetric_difference(s2)
# print s1

# s1.symmetric_difference_update(s2)
# print s1

# print s1.union(s2)
# print s1

# print s1
# s1.update(s2)
# print s1


# 
# advanced dictionaries
# 

d = {'k1':1,'k2':2}

# print {x:x**2 for x in range(10)}

# print {k:v**2 for k,v in zip(['a','b'],range(2))}

# for k in d.iteritems():
# 	print k

# for k in d.iterkeys():
# 	print k

# for k in d.itervalues():
# 	print k

# print d.viewitems()
# print d.viewkeys()
# print d.viewvalues()


# 
# advanced lists
#

# l = [1,2,3]
# l.append(4)
# print l
# print l.count(2)

# x = [1,2,3]
# x.append([4,5])
# print x

# x = [1,2,3]
# x.extend([4,5])
# print x

# print x
# print x.index(2)
# print x
# x.insert(2, 'inserted')
# print x
# print x.pop()
# print x
# print x.pop(0)
# print x
# x.remove('inserted')
# print x
# x = [1,2,3,4,3]
# print x
# x.remove(3)
# print x
# x.reverse()
# print x
# x.sort()
# print x
