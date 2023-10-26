class Publication:
    def __init__(self,name):
        self.name = name
class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor
    def print_info(self):
        print(f"Name of the magazine: {self.name} author: {self.editor}")

class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(author)
        self.author = author
        self.pages = pages
    def print_info(self):
        print(f"Name of the book: {self.name} author : {self.author} and pages {self.pages}")

pub1 = Magazine ("Aku-Ankka", "Aki Hyyppä")
pub1.print_info()
pub2 = Book ("Hytti n:o 6", "Rosa Liksom", "200")
pub2.print_info()

