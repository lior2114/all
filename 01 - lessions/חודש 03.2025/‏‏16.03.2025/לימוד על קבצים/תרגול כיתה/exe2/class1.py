class Book:
    def __init__ (self,bookname,namewriter,exitday,price):
        self.bookname = bookname
        self.namewriter = namewriter
        self.exitday = exitday
        self.price = price

    def details_of_book(self):
        return (f"name of book:{self.bookname}, name writer:{self.namewriter}, exitday:{self.exitday}, price:{self.price}, ")
    
    def maam (self):
        return f"maam is:{int(self.price*0.18)}"
    