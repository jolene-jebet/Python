#traditional loop
squares = []
for i in range(10):
    squares.append(i**2)
print(squares)

#list comprehension
squares = [i**2 for i in range(10)]
print(squares)

#using conditions in list comprehension
even_numbers= [i for i in range(10) if i%2==0]
print(even_numbers)

##nested
# Create a 3x3 matrix using nested list comprehensions
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)  # Output: [[1, 2, 3], [2, 4, 6], [3, 6, 9]]


##using a basket of fruits you want to organizw
fruits = ["apple", "banana" , "apple", "elderberry"]
apple_slices = [fruit + " slice" for fruit in fruits if fruit == "apple"]
print(apple_slices)

#traditional way
fruits = ['apple', 'banana', 'apple', 'orange', 'apple']
apple_slices = []
for fruit in fruits:
    if fruit == 'apple':
        apple_slices.append(fruit + ' slices')
