
# Question No 15

# 1) Define a class called TemperatureConverter with methods c_to_f(celsius) and 
#    f_to_c(fahrenheit) to convert temperatures between Celsius and Fahrenheit.
# 2) Create an instance of TemperatureConverter and test its conversion methods.

class TemperatureConverter:

    def c_to_f(self, celsius):
        self.celsius = celsius
        fahrenheit = self.celsius * (9/5) + 32
        print(f'\nFahrenheit is: {fahrenheit}')
    
    def f_to_c(self, fahrenheit):
        self.fahrenheit = fahrenheit
        celsius = (self.fahrenheit - 32) * (5/9)
        print(f'\nCelsius is: {celsius}\n')
    

tempConv = TemperatureConverter()
tempConv.c_to_f(10)
tempConv.f_to_c(50)