
# Question No 12

# 1) Define a class called Book with attributes title, author, and year.
# 2) Include a method display_info() that prints out the book's information.
# 3) Create multiple instances of Book with different information and display their info.

class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f'Book Title: {self.title}\nAuthor Name: {self.author}\nPublishing Year: {self.year}')

print('\nBook 1')
book1 = Book('One Hundred Years of Solitude', 'Gabriel Garcia Marquez', 1967)
book1.display_info()
print('\nBook 2')
book2 = Book('The Alchemist', 'Paulo Coelho', 1988)
book2.display_info()
print('\nBook 3')
book3 = Book('Sapiens', 'Yuval Noah Harari', 2011)
book3.display_info()
print()