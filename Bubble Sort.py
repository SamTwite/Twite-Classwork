import random
import time
start_time = time.time()
value = 0
numbers = []
for i in range(1000):
    value = random.randint(0,100000)
    numbers.append(value)

def bubble_sort(numbers):
    swapped = True
    while(swapped):
        swapped = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                #swap
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True



bubble_sort(numbers)
print(numbers)
print((time.time() - start_time))