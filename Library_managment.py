class Library:
    def __init__(self):
        self.nobooks = 0
        self.books=[]
    def addbook(self,book):
        self.books.append(book)
        self.nobooks=len(self.books)
    def showinfo(self):
        print(f"The books in the library is {self.nobooks}")

l1=Library()
l1.addbook("Rakesh1")
l1.addbook("Rakesh2")
l1.addbook("Rakesh3")
l1.showinfo( )      