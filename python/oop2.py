class Person():

    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln

    def hello(self):
        print("hello")

    def report(self):
        print(f"I am {self.fn} {self.ln}")


class Agent(Person):  # also inherit Person.__init__

    def __init__(self, fn, ln, cn):  # override init
        Person.__init__(self, fn, ln)
        self.cn = cn

    def report(self):  # override method
        print(f"I'm {self.fn} {self.ln}")

    def reveal(self, passcode=None):
        if passcode == 123:
            print(f"I'm {self.cn}")
        else:
            self.report()


x = Agent("James", "Bond", "007")
x.hello()
x.reveal(passcode=123)


# special methods

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):  # return string representation of your object using special methods
        # should always return a string
        return f"{self.title} written by {self.author}"

    def __len__(self):
        return self.pages  # should always return an integer


mybook = Book("Python Rocks", "J", 120)

# instead of displaying memory location of object, display string representation
print(mybook)
print(f"{len(mybook)} pages")
