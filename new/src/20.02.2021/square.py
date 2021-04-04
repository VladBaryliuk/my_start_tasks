class square:
    def __init__(self, count=10):
        self.count = count
    def draw(self, count=10):
        for j in range(count):
            for i in range(count):
                print("*", sep='', end=' ')
            print()
    def area(self):
        return self.count**2


s1 = square(5)
s1.draw(5)
print(s1.area())
