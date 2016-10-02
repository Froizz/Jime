
''' Program make a simple calculator that can add, subtract, multiply and divide using functions '''

# define functions
def add(x, y):
   """This function adds two numbers"""
   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""
   return x - y

def multiply(x, y):
   """This function multiplies two numbers"""
   return x * y

def divide(x, y):
   """This function divides two numbers"""
   return x / y

def calcul():


   # take input from the user
   print('=========================')
   print("Select operation.")
   print('=========================')
   print("1.Add")
   print('=========================')
   print("2.Subtract")
   print('=========================')
   print("3.Multiply")
   print('=========================')
   print("4.Divide")
   print('=========================')
   print("9.Exit")
   print('=========================')
   
   choice = input("Enter choice(1/2/3/4):")
   if choice > '4':
      if choice =='9':
         return
      print("\n \nInvalid input \n \n")
      calcul()

   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))

   if choice == '1':
      print(num1,"+",num2,"=", add(num1,num2))

   elif choice == '2':
      print(num1,"-",num2,"=", subtract(num1,num2))

   elif choice == '3':
      print(num1,"*",num2,"=", multiply(num1,num2))

   elif choice == '4':
      print(num1,"/",num2,"=", divide(num1,num2))
   else:
      print("Invalid input")
   calcul()
   

