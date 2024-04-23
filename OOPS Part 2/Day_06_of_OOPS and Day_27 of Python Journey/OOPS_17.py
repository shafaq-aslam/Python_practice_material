
# Question No 17

# 1) Define a class called Movie with attributes title, director, and rating.
# 2) Include a method is_good() that returns True if the rating is above 7, otherwise False.
# 3) Create an instance of Movie and check if it's good using the is_good() method.

class Movie:

    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating


    def is_good(self):
        if self.rating > 7:
            return True
        else:
            return False
        
mov1 = Movie('Bol', 'Shoaib Mansoor', 8.2)
mov2= Movie('Ho Mann Jahaan', 'Asim Raza', 7.3)
mov3 = Movie('Laal Kabootar', 'Kamal Khan', 7)

print(f'\nMovie name: {mov1.title}\nDirected by: {mov1.director}\nMovie Rating: {mov1.rating}\nIs it good: {mov1.is_good()}\n')
print(f'Movie name: {mov2.title}\nDirected by: {mov2.director}\nMovie Rating: {mov2.rating}\nIs it good: {mov2.is_good()}\n')
print(f'Movie name: {mov3.title}\nDirected by: {mov3.director}\nMovie Rating: {mov3.rating}\nIs it good: {mov3.is_good()}\n')