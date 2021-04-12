numbers = [24, 20, 6, 17, 8, 2]
def smallest(numbers):
    smallest = numbers[2]
    for i in numbers:
        if i < smallest:
            smallest = i
    print('This is the smallest number: ', smallest )
smallest(numbers)
