class Number:
    def __init__(self, num):
        self.num = num

    def check(self):
        if self.num % 2 == 0:
            print(self.num, "is Even")
        else:
            print(self.num, "is Odd")

# Create an object
n = Number(7)

# Check whether the number is even or odd
n.check()