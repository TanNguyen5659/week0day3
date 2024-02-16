x = 2
if x < 2: print ("it's true")
else: print("it's wrong")

def talk(x):
    print(str(x))
    print("...")
    print("...")
    print("...")

print("Hello")
talk("Tan")

def blender(fruit1, fruit2):
    print("...Blending...")
    smoothie = "You made a " + fruit1 + " and " + fruit2 + ' smoothie!'
    return smoothie

s1 = blender('orange','kiwi')
s2 = blender('mango','blueberry')

print(s1)
print(s2)

print(blender('passionfruit', 'watermelon'))

# print out the number from 1 to 10
# def range(x,y):
#     for i == x to y
#         print

# def print_ten():
#     for num in range(11):
#         print(num)
#     return 1

# print(print_ten())

def print_upto(x):
    for x in range(x+1):
        print(x)

print_upto(9)

def area(length, width):
    return length*width
print(area(2,3))
print("github test")