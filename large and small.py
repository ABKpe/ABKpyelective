numbers = input("Enter a list of numbers that wanted to be seperatrated: ").split()
numbers = [int(num) for num in numbers]
largest = max(numbers)
smallest = min(numbers)
print("The largest number is:", largest)
print("The smallest number is:", smallest)