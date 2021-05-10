import random
import time
start_time = time.time()
value = 0
numbers = []
for i in range(10000):
    value = random.randint(0,100000)
    numbers.append(value)
    print(value)


def insertionSort(numbers):
    for i in range(1, len(numbers)):
  
        key = numbers[i]
        j = i-1
        while j >=0 and key < numbers[j] :
                numbers[j+1] = numbers[j]
                j -= 1
        numbers[j+1] = key



insertionSort(numbers)
print(numbers)
print("Total time:")
print((time.time() - start_time))


