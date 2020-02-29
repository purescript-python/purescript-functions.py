## Function Creators
def mkFn0(fn):
    def func():
        return fn()
    return func

def mkFn2(fn):
    def func(a, b):
        return fn(a)(b)
    return func

def mkFn3(fn):
  def func(a, b, c):
      return fn(a)(b)(c)
  return func

def mkFn4(fn):
  def func(a, b, c, d):
      return fn(a)(b)(c)(d)
  return func

def mkFn5(fn):
  def func(a, b, c, d, e):
      return fn(a)(b)(c)(d)(e)
  return func

def mkFn6(fn):
  def func(a, b, c, d, e, f):
      return fn(a)(b)(c)(d)(e)(f)
  return func

def mkFn7(fn):
  def func(a, b, c, d, e, f, g):
      return fn(a)(b)(c)(d)(e)(f)(g)
  return func

def mkFn8(fn):
  def func(a, b, c, d, e, f, g, h):
      return fn(a)(b)(c)(d)(e)(f)(g)(h)
  return func

def mkFn9(fn):
  def func(a, b, c, d, e, f, g, h, k):
      return fn(a)(b)(c)(d)(e)(f)(g)(h)(k)
  return func

def mkFn10(fn):
  def func(a, b, c, d, e, f, g, h, k, l):
      return fn(a)(b)(c)(d)(e)(f)(g)(h)(k)(l)
  return func

## Function Runners
def runFn0(fn):
    return fn()

def runFn2(fn):
    return lambda a: lambda b: fn(a,b)

def runFn3(fn):
    return lambda a: lambda b: lambda c: fn(a,b,c)

def runFn4(fn):
    return lambda a: lambda b: lambda c: lambda d: fn(a,b,c,d)

def runFn5(fn):
    return lambda a: lambda b: lambda c: lambda d: \
        lambda e: fn(a,b,c,d,e)

def runFn6(fn):
    return lambda a: lambda b: lambda c: lambda d: \
        lambda e: lambda f: fn(a,b,c,d,e,f)

def runFn7(fn):
    return lambda a: lambda b: lambda c: lambda d: \
        lambda e: lambda f: lambda g: fn(a,b,c,d,e,f,g)

def runFn8(fn):
    return lambda a: lambda b: lambda c: lambda d: \
        lambda e: lambda f: lambda g: lambda h: fn(a,b,c,d,e,f,g,h)

def runFn9(fn):
    return lambda a: lambda b: lambda c: lambda d: \
        lambda e: lambda f: lambda g: lambda h: \
        lambda i: fn(a,b,c,d,e,f,g,h,i)

def runFn10(fn):
    return lambda a: lambda b: lambda c: lambda d: \
        lambda e: lambda f: lambda g: lambda h: \
        lambda i: lambda j: fn(a,b,c,d,e,f,g,h,i,j)
