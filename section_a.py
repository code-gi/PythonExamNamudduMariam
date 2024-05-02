#question one part a(i)
def calculateGrades():

    print("\n...Student Grade Calculations...")

    mark = int(input('Enter mark scored:\t'))
    
    if mark>=90 and  mark<=100:
        print("Grade is A")

    elif mark>=80 and mark<=89:
        print("Grade is B")

    elif mark>=70 and mark<=79:   
        print("Grade is C") 

    elif mark>=60 and mark<=69:   
        print("Grade is D")   

    elif mark>=50 and mark<=59:   
        print("Grade is E")  

    else:
        print("Fail")  
        
calculateGrades()      

# question one part a(ii)
def temperatureConvertions():

    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius ")

    option = int(input("Select your choice (1 or 2): "))

    if option == 1:
        celsius =  float(input("Enter temperature in Celsius Degrees: "))
        fahrenheit  = (9/5 * celsius) + 32
        print(f"{celsius}° C is equal to {fahrenheit}°F")

    elif option == 2:
        fahrenheit =  float(input("Enter temperature in Fahrenheit Degrees: "))
        celsius  = 5/9 * (fahrenheit -32 )
        print(f"{fahrenheit}°F is equal to {celsius}°C")
    else:
        print("Invalid option!") 
temperatureConvertions()

# question one part b(i)

base = int(input('\nEnter the base of the triangle: '))
height = int(input('Enter the height of the triangle: '))

def area_of_triangle(b,h):

    area = (1/2) * b * h

    print(int(area))

area_of_triangle(base,height)

# question 0ne part b(ii)

def sample_list():

    numbers = [9,2,3,5,8]
    sum = 0

    for k in numbers:
        sum += k
    print("The sum of all numbers in the sample list is " +str(sum))  
    
sample_list()








  