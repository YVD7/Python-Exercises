# from classes & objects import BankAccount

# class MinimumBalanceAccount(BankAccount):
#     def __init__(self, minimun_balance):
#         BankAccount.__init__(self)
#         self.minimum_balance = minimun_balance


#     def withdraw(self, amount):
#         if self.balance - amount < self.minimum_balance:
#             print('Sorry, minimum balance must be maintained.')
#         else:
#             BankAccount.withdraw(self, amount)


# class A:
#     def f(self):
#         return self.g()

#     def g(self):
#         return 'A'

# class B(A):
#     def g(self):
#         return 'B'

# a = A()
# b = B()

# print(a.f(), b.f())
# print(a.g(), b.g())

class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[' ']* width for i in range(height)]

    def setpixel(self, row, col):
        self.data[row][col] = '*'

    def getpixel(self, row, col):
        return self.data[row][col]

    def display(self):
        print("\n".join(["".join(row) for row in self.data]))

class Shape:
    def print(self, canvas): pass

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def hline(self, x, y, w):
        pass

    def vline(self, x, y, h):
        pass

    def paint(self, canvas):
        hline(self.x, self.y, self.w)
        hline(self.x, self.y+self.h, self.w)
        vline(self.x, self.y, self.h)
        vline(self.x+self.w, self.y, self.h)

class square(Rectangle):
    def __init__(self, x, y, size):
        Rectangle.__init__(self, x, y, size, size)

class CompoundShape(Shape):
    def __init__(self, shapes):
        self.shapes = shapes

    def paint(self, canvas):
        for s in self.shapes:
            s.paint(canvas)