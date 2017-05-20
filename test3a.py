def f(x):
	return x + 3
print(f(-2))

def f(x,y):
	return x + y
print(type(f(2,3)))

def func(*a):
	return sum([x**2 for x in a ])
print(func(2,3))

def f():
    a = 1
    print(a, end=' ')
a = 5
f()
print(a, end = ' ')

def f():
    global a
    a = a + 1
    print(a, end=' ')


a = 1
f()
print(a, end=' ')

def f1():
    fruit = 'μήλο'
    f2()


def f2():
    print(fruit)


# κυρίως πρόγραμμα
fruit = 'αχλάδι'
f1()

def d(x = 0, y = 0):
	return x**3 + y**3
print(d(2))

a = 1
def x(n):
    a = 3
    print (a,  n, end = ' ')
    return a
print (x(2), a )

def f(x):
    for a in x:
        print (a, end = ' ')
        return a
f([1,2,4])

def f(x):
    for a in x:
        print(a, end='')
f([1, 2, 3])