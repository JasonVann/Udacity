x = 'outside x'
y = 'outside y'

def fun1(x, z):
    print 'fun1 x ' + x
    print 'fun1 y ' + y
    fun2('fun1 y')
    print 'fun1 x ' + x

def fun2(y):
    print 'fun2 x ' + x
    print 'fun2 y ' + y

fun1('HK', '1997')
