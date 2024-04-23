
# Question No 13

# 1) Define a class called Book with attributes title, author, and year.
# 2) Include a method display_info() that prints out the book's information.
# 3) Create multiple instances of Book with different information and display their info.(While loop)

class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display_info(self):
        print(f'Book Title: {self.title}\nAuthor Name: {self.author}\nPublishing Year: {self.year}')
        
obj = 'y'
while obj != 'n':
    obj = input('\nWant to create object? (y/n): ')
    if obj == 'y':
        b_no = int(input('\nEnter serial no (1,2,3) etc: '))
        book_name = input('Enter name of book: ')
        author_name = input('Enter name of author: ')
        published_year = input('Enter the publishing year: ')
        book = Book(book_name, author_name, published_year)
        print("\nBook ",b_no)
        book.display_info()
    else:
        print('Goodbye! Come again...')
        break
