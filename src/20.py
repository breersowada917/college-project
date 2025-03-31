def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list")
    
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    
    return average

try:
    print(calculate_average([1, 2, 3, 4, 5]))
except ValueError as e:
    print(e)
