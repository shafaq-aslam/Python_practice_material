
# 26. We have following information on countries and their population (population is in crores),

# Country	Population
# China	        143
# India	        136
# USA	        32
# Pakistan	    21

# i. Using above create a dictionary of countries and its population
# ii. Write a program that asks user for three type of inputs,
#       a. print: if user enter print then it should print all countries with their population in this format,
#           china==>143
#           india==>136
#           usa==>32
#           pakistan==>21
#       b. add: if user input add then it should further ask for a country name to add. If country already exist 
#          in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population
#          and add that new country/population in our dictionary and print it
#       c. remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary
#          then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
#       d. query: on this again ask user for which country he or she wants to query. When user inputs that country it will
#          print population of that country.

countries_population = {
    'china' : 143,
    'india' : 136,
    'usa'   : 32,
    'pakistan' : 21
}

def Print():
    for i in countries_population.keys():
        print(f'{i}==>{countries_population[i]}')

def add():
    country = input('Enter a country name you want to add: ')
    if country in countries_population:
        print(f'{country} is already exist!')
    else:
        population = int(input(f'Enter population of {country}: '))
        countries_population.update({country : population})
        Print()

def remove():
    country = input('Which country you want to remove? ')
    if country in countries_population:
        countries_population.pop(country)
        Print()
    else:
        print(f'{country} doesn\'t exist!')

def query():
    country = input('For which country you want to query? ')
    if country in countries_population:
        print(f'Population of {country}: {countries_population[country]} crores')
    else:
        print(f'{country} doesn\'t exist!')

y_n = 'y'

while y_n == 'y':
    user_input = input('Entery print/add/remove/query: ')
    if user_input == 'print':
        Print()
    elif user_input == 'add':
        add()
    elif user_input == 'remove':
        remove()
    elif user_input == 'query':
        query()
    else:
        print('Invalid input.')

    y_n = input('Want choose again? (y/n): ')