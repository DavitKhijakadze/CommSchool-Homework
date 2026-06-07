import logging


#task1

word = "CODE"

def text_generator(text):
    for char in text:
        yield char

gen_object = text_generator(word)

print(next(gen_object))
print(next(gen_object))
print(next(gen_object))


#task2

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

user_input = input("Enter an index (number): ")

try:
    index = int(user_input)
    
    element = arr[index]
    print(f"The element at index {index} is: {element}")
except ValueError:
    print("Invalid input. Please enter numbers only")
except IndexError:
    print(f"Please enter a number between 0 and {len(arr) - 1}")


#task3

def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"გამოძახება: {wrapper.count}")
        
        return func(*args, **kwargs)
    
    wrapper.count = 0
    return wrapper

@counter
def say():
    print("Hi")

say()
say()
