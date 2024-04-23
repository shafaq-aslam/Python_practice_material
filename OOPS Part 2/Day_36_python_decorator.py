
# Example 01

print('\nExample 01\n******************************')
def greeting(func):
    def decorate():
        print("\nIt's time to greet employees...\n")
        func()
        print("Hope your day will be full of success.\n")
    return decorate


@greeting
def greet():
    print("Good Morning! Have a good day.")

greet()

# Example 02

print('\nExample 02\n******************************')
def Greet(func):
    def wish(*args):
        print("\nIt's time to greet individual..")
        func(*args)
        print("Wishing you a successful day ahead\n")
    return wish


@Greet
def greet_with_name(name):
    print(f"Hi {name}! Have a good day ahead.")

greet_with_name('Shafaq')


# Example 03

print('\nExample 03\n******************************\n')
import time

def timing_decorator(func):
    def wrapper():
        start_time = time.time()  
        func()  
        end_time = time.time()  
        duration = end_time - start_time  
        print(f"Function '{func.__name__}' took {duration:.6f} seconds to execute.")
    return wrapper

@timing_decorator
def example_function():
    time.sleep(1)  
    print("Function executed.")

example_function()