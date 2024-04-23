
# 1. Use python to find area of triangle
# area = (1/2)*base*height
#------------------------------------------------------

base = 8
height = 9
area = (1/2)*base*height
print("Area of Triangle is: ",area)

# 2. Internal representation of numbers
# integers are stored in simple binary format
#------------------------------------------------------

print(format(10,'b'))
print(format(752,'b'))

# 3. String and Explore string's methods
#------------------------------------------------------

name = 'Shafaq'
print(name)

name_slice = name[0:3] #[included:excluded]-->[start:end]
print(name_slice)

print(name.upper())

# Negative Slicing
neg_slicing = name[-5:]
print(neg_slicing)

neg_slicing = name[-5:-1]
print(neg_slicing)

neg_slicing = name[-1:]
print(neg_slicing)

new_name = name.replace('Shafaq','Zainab') # Original string remain same ----> String is immutable
print(new_name)

print(len(name))

names = 'Shafaq,Zainab,Shayan'
print(names.index('Shayan'))

print('Shayan' in names)

# 4. Write a program that can find area of a triangle. It should take base and height as an 
# input from user and using that it should print an area of a triangle
#----------------------------------------------------------------------------------------------------

base = int(input('Enter base: '))
height = int(input('Enter height: '))
area = (1/2)*base*height
print('Area of Triangle is: ',area)

# 5. Write a program that takes file name with extension as an input and prints just the 
# file name without extension (you can assume that file extensions are always 3 character long)
#------------------------------------------------------------------------------------------------------

file_name = input('Enter file name with extension: ')
file = file_name.split('.')
print('File name is: ',file[0])

# 6. You have a football field that is 92 meter long and 48.8 meter wide. 
# Find out total area using python and print it.
#-----------------------------------------------------------------------------

length = 92
width = 48.8
area = length*width
print('Area of football field is: ',round(area,2))

# 7. You bought 9 packets of potato chips from a store. 
# Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar.
# Find out using python, how many dollars is the shopkeeper going to give you back?
#----------------------------------------------------------------------------------

total_packets_of_potato_chips = 9
price_of_each_packet = 1.49
paid_amount = 20

price_of_all_packets = price_of_each_packet*total_packets_of_potato_chips
return_amount = paid_amount - price_of_all_packets

print(f'Price of all packets: {price_of_all_packets}\nPaid Amount: {paid_amount}\nReturn Amount: {return_amount}')

# 8. You want to replace tiles in your bathroom which is exactly square and 5.5
# feet is its length. If tiles cost 500 rs per square feet, how much will be the
# total cost to replace all tiles. Calculate and print the cost using python
# (Hint: Use power operator ** to find area of a square)
#-----------------------------------------------------------------------------

length_of_tile = 5.5
area_of_square = length_of_tile**2
total_cost = area_of_square*500
print('Total cost: ',total_cost)

# 9. Print binary representation of number 17

num = 17
print(f'Binary representation of {num} is: {format(num,'b')}')

# 10. Create 3 variables to store street, city and country, now create address variable to
# store entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
# Now Print the address in such a way that the street, city and country prints in a separate line
#-----------------------------------------------------------------------------

street = 'Street # 8'
city = 'Karachi'
country = 'Pakistan'
address = street + '\n' + city + '\n' +country
print("Address: ",address)
address = f'{street}\n{city}\n{country}'
print("Address: ",address)

# 11. Create a variable to store the string "Earth revolves around the sun"
#     1. Print "revolves" using slice operator
#     2. Print "sun" using negative index
#-----------------------------------------------------------------------------

sentence = "Earth revolves around the sun"
revolves = sentence[6:14]
sun = sentence[-3:]

print(f'{revolves}\n{sun}')

# 12. Create two variables to store how many fruits and vegetables you eat in a day.
# Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday.
# Use python f string for this.
#-----------------------------------------------------------------------------

num_of_fruits = 3
num_of_vegetables = 5
print(f'I eat {num_of_vegetables} veggies and {num_of_fruits} fruits daily')

# 13. I have a string variable called s='maine 200 banana khaye'. This of course is a
# wrong statement, the correct statement is 'maine 10 samosa khaye'.
# Replace incorrect words in original strong with new ones and print the new string.
# Also try to do this in one line.
#-----------------------------------------------------------------------------

s='maine 200 banana khaye'
new_str = s.replace('200 banana', '10 samosa')
print(new_str)
s=s.replace('banana','samosa').replace('200','10')
print(s)

# 14. Let us say your expense for every month are listed below,
# 	  1. January -  2200
#  	  2. February - 2350
#     3. March - 2600
#     4. April - 2130
#     5. May - 2190
#
# Create a list to store these monthly expenses and using that find out,
#
# i. In Feb, how many dollars you spent extra compare to January?
# ii. Find out your total expense in first quarter (first three months) of the year.
# iii. Find out if you spent exactly 2000 dollars in any month
# iv. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# v. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
#-----------------------------------------------------------------------------

mon_exp = [2200,2350,2600,2130,2190]
# i. In Feb, how many dollars you spent extra compare to January?
print(f'January: ${mon_exp[0]}\nFebruary: ${mon_exp[1]}')
print(f'In Feb, dollars you spent extra compare to January: ${mon_exp[1]-mon_exp[0]}')

# ii. Find out your total expense in first quarter (first three months) of the year.
print(f'January: ${mon_exp[0]}\nFebruary: ${mon_exp[1]}\nMarch: ${mon_exp[2]}')
print(f'Total expense in first quarter (first three months): ${mon_exp[0]+mon_exp[1]+mon_exp[2]}')

# iii. Find out if you spent exactly 2000 dollars in any month
print('Did I spent $2000 in any month: ',2000 in mon_exp)

# iv. June month just finished and your expense is 1980 dollar. 
# Add this item to our monthly expense list
mon_exp.append(1980)
print(f'June month just finished and your expense is {mon_exp} dollar')

# v. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list
# based on this

mon_exp[3] = mon_exp[3] - 200
print(f'After refund of $200, April expense is: {mon_exp[3]}')

# 15. You have a list of your favourite marvel super heros
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,
#
# 1. Length of the list
# 2. Add  at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#  so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
# So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
#---------------------------------------------------------------------------------------------------

heros=['spider man','thor','hulk','iron man','captain america']
# 1. Length of the list
print('Length of the list is: ',len(heros))
# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)
# 3. You realize that you need to add 'black panther' after 'hulk',
#  so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3, 'black panther')
print(heros)
# 4. Now you don't like thor and hulk because they get angry easily :)
# So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
heros.remove('thor')
heros.remove('hulk')
print(heros)
heros.insert(1,'doctor strange')
print(heros)
        # 2 way
heros[1:3]= ['doctor strange']
print(heros)

# 5. Sort the heros list in alphabetical order 
# (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)

print(dir(heros))

# 16. Using following list of cities per country,
#     ```
#     india = ["mumbai", "banglore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
# i. Write a program that asks user to enter a city name and it should tell which country the city belongs to
#---------------------------------------------------------------------------------------------------

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city_name = input('Enter a ccity name: ')

if city_name in india:
    print(f'{city_name} belongs to India')
elif city_name in pakistan:
    print(f'{city_name} belongs to Pakistan')
elif city_name in bangladesh:
    print(f'{city_name} belongs to Bangladesh')
else:
    print("Sorry I'm unable to find the country")

# ii. Write a program that asks user to enter two cities and it tells you
# if they both are in same country or not. For example if I enter islamabad and karachi,
# it will print "Both cities are in pakistan" but if I enter lahore and dhaka it should
# print "They don't belong to same country"
#---------------------------------------------------------------------------------------------------

city_name_1 = input('Enter first city name: ')
city_name_2 = input('Enter second city name: ')

if city_name_1 in india and city_name_2 in india:
    print("Both cities are in India")
elif city_name_1 in pakistan and city_name_2 in pakistan:
    print("Both cities are in Pakistan")
elif city_name_1 in bangladesh and city_name_2 in bangladesh:
    print("Both cities are in Bangladesh")
else:
    print("They don't belong to same country")

# 17. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#       i. Ask user to enter his fasting sugar level
#       ii. If it is below 80 to 100 range then print that sugar is low
#       iii. If it is above 100 then print that it is high otherwise print that it is normal
#---------------------------------------------------------------------------------------------------

fasting_sugar_level = float(input('Enter your fasting sugar level: '))

if fasting_sugar_level < 80:
    print('Your sugar is low')
elif fasting_sugar_level > 100:
    print('Your sugar is high')
else:
    print('Your sugar is normal')

# 18. After flipping a coin 10 times you got this result,
#     result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads
#---------------------------------------------------------------------------------------------------

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
heads = 0
tails = 0

for i in range(len(result)):
    if result[i] in 'heads':
        heads += 1

print(f'Heads are: {heads}')

# 19. Print square of all numbers between 1 to 10 except even numbers
#---------------------------------------------------------------------------------------------------

for i in range(1,11):
    if i%2 != 0:
        print(f'Square of {i} is: {i**2}')

# 20. Your monthly expense list (from Jan to May) looks like this,
# ```
# expense_list = [2340, 2500, 2100, 3100, 2980]
# ```
# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.
#---------------------------------------------------------------------------------------------------

expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

exp = int(input('Enter an expence amount: '))


for i in range(len(expense_list)):
    if exp == expense_list[i]:
       print(f'In month of {month_list[i]}, you spend {exp}')
       break   
else:
    print(f'You didn\'t spend {exp} in any month')

# 21. Lets say you are running a 5 km race. Write a program that,

#   i. Upon completing each 1 km asks you "are you tired?"
#   ii. If you reply "yes" then it should break and print "you didn't finish the race"
#   iii. If you reply "no" then it should continue and ask "are you tired" on every km
#   iv. If you finish all 5 km then it should print congratulations message
#---------------------------------------------------------------------------------------------------

for i in range(1,6):
    print(f'You have completed {i}km race.')
    tired = input('Are you tired? (yes/no): ')
    if tired == 'yes':
        print('You didn\'t finish the race')
        break
    
if i == 5:
    print('Congratulations you finished the race')

# 22. Write a program that prints following shape

# *
# **
# ***
# ****
# *****
#---------------------------------------------------------------------------------------------------

for i in range(1,6): 
    for j in range(i): 
        print('*',end=' ') 
    print()


    

