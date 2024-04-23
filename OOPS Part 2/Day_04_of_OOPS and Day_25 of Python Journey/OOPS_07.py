
# Question No 07
# Create a class Counter with a static variable count initialized to 0. 
# Implement a static method increment() that increments the count by 1. 
# Instantiate multiple Counter objects and call the increment() method 
# on each. Print the value of count after each call to observe the static behavior.


class Counter:

    count = 0

    @staticmethod
    def increament():
        Counter.count += 1

counter1 = Counter()
counter1.increament()
print("Counter increment by: ", counter1.count)

counter2 = Counter()
counter2.increament()
print("Counter increment by: ", counter2.count)

counter3 = Counter()
counter3.increament()
print("Counter increment by: ",counter3.count)


