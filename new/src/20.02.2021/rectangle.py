class Rectangle:
    def __init__(self, count1=5, count2=10):
        self.count1 = count1
        self.count2 = count2

    def draw(self, count1=5, count2=10):
        for j in range(count1):
            for i in range(count2):
                print("*", sep='', end=' ')
            print()

    def area(self):
        global count1, count2
        return count1 * count2


r1 = Rectangle
r1.draw(count1=5, count2=3)
print(r1.area())
