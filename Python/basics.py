#Dont need var in front of variables
wage = 20
hours = 40
weeks = 52

salary = wage * hours * weeks

print(wage) #just put the variable name in the parentheses to output the variable
print("Salary is: ", salary)

hours = 60
salary = wage * hours * weeks
print('New salary is:', salary)

#Print() prints the things included in the parentheses
print("Joey Logano sucks")

#All on one line due to the 'end='
print('Kyle Busch ', end='')
print('is the ', end='')
print('greatest of all time.')

print('Wage: $',wage) #prints multiple things in a statement with a common separating them. Can add as many as you want

print('1\n2\n3') #prints on new line due to the '\n'

print('Whitespace')
print() #nothing in the parentheses means whitespace
print('example') 

print('Who is the NASCAR GOAT?', end='')
GOAT = input() #input waits for user input to output the print that includes the input function
print('The NASCAR GOAT is', GOAT) #reading from an input ALWAYS RESULTS IN A STRING


mystring = '123' #converts into 123 the string
myint = int('123') #converts into 123 the integer

print(mystring)
print(myint)

print('Enter wage:', end='')
oldwage = int(input()) #turns input into an integer

newwage = oldwage + 10 
print('New Wage:', newwage)


hours2 = 40
weeks2 = 52
hourly_wage = int(input('Enter hourly wage: ')) #Adding a string inside the parentheses of input() displays a prompt to the user before waiting for input and is a useful shortcut to adding an additional print statement line.

print('Salary is', hourly_wage * hours2 * weeks2)

print(type(myint)) #can find type of variable with type() function
print(id(myint)) #can find the id of a variable with the id() function

myfloat = 5.36987
print(f'{myfloat:.2f}') #the f'{:.2f}' addition to the variable decides how many decimal places to print of the float

wall_area = float(input())
print('amount of paint needed is', f'{(wall_area / 350.0):.5f}') #' * = multiply, / = divide, + = add - = subtract and also a negative number if placed infront of the number, ** = exponent, // = round to closest whole number (it will make a decimal under 0 = 0 ex. 0.3 is = 0)

#precedence for arithmetic operators......() then ** then -3(negative numbers being computed a such) then */% then +- then left to right

#Compound Operators: += is same as +, -= is same as -, *= is same as *, /= is same as /, %= is same as %

age = 21
age += 3 # is equal to 24, sames as age = age + 3
print('age is', age)

print(24%10) #modulo finds whats left after dividing the numbers, example here is 24%10 leaves 4 left, as 10 goes into 20 2 times with 4 left over.

#Modules can be imported into document using the "import" keyword at the top of the page. A module is  a file containing Python code that can be used by other modules or scripts.
#Modules can be referenced using dot notation.
