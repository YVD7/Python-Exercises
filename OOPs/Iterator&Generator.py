# # Iterators
# for i in [1,2,3,4]:
#     print(i)

# for c in "python":
#     print(c)

# for k in {"x":1, "y":2}:
#     print(k)

# for line in open("a.txt"):
#     print(line, end=" ")
# ===========================================================================
",".join(["a","b","c"])

",".join({"x":1,"y":2})

list("Python")

list({"x":1, "y":2})

x = iter([1,2,3])
x
# ===========================================================================
class yrange():
    def __init__(self,n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

a = yrange(4)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

# =================================================================

class zrange():
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return zrange_iter(self.n)

class zrange_iter:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def  __iter__(self):
        # Iterators are Iterables too.
        # Adding  this functions to make them so.
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i

        else:
            raise StopIteration()

y = zrange_iter(4)
print(y.next())
print(y.next())
print(y.next())
print(y.next())
print(y.next())

# =================================================================

def foo():
    print("being")
    for i in range(3):
        print("before yeild", i)
        yield i
        print("after yeild", i)
    print("end")

f = foo()
next(f)
next(f)
next(f)

# ============================================================================

def integers():
    """Infinite  sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1

def squares():
    for i in integers():
        yield i * i

def take(n, seq):
    """Return first n values from the girven sequence."""
    seq = iter(seq)
    result =[]
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result

print( take(5, squares()))

# =======================================================================================

a = (x * x for x in range(10))
print(sum(a))

sum(a)

sum((x * x for x in range(10)))

sum(x * x for x in range(10))

pyt = ((x,y,z) for z in integers() for y in range(1, z) for x in range(1, y) if x*x + y*y == z*z)
take(10, pyt)

# ============================================================================================

def cat(filenames):
    for f in filenames:
        for line in open(f):
            print(line, end="")

# =============================================================================================

def grep(pattern, filenames):
    for f in filenames:
        for line in open(f):
            if pattern in line:
                print(line, end="")

# =============================================================================================

def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def grep(pattern, lines):
    return (line for line in lines if pattern in line)

def printlines(lines):
    for line in lines:
        print(line, end="")

def main(pattern, filenames):
    lines = readfiles(filenames)
    lines = grep(pattern, lines)
    printlines(lines)

# ===================================================================================================
import itertools

it1 = iter([1, 2, 3])
it2 = iter([4, 5, 6])
itertools.chain(it1, it2)

# ===================================================================================================

import itertools
for x, y in itertools.izip(["a","b","c"],[1,2,3]):
    print(x, y)

# ==================================================================================================
from itertools import peep
it = iter(range(5))
x, it1 = peep(it)
print(x, list)

# ===================================================================================================

list(enumerate["a","b","c"])
for i, c in enumerate(["a", "b", "c"]):
    print(i, c)

# ===================================================================================================

