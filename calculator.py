class Arithmatic:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def sum(self):
        print(f"SUM : {self.a + self.b} ")
    def sub(self):
        print(f"SUBTRACTION :{ self.a - self.b} ")
    def multiply(self):
        print(f"Multiplication {self.a * self.b}" )
    def division(self):
            print(f"Division  {self.a / self.b }")
while True:
    print("\n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exit")
    choice = int(input("\nEnter your choice \n"))
    if(choice == 5):
        break
    
    num1 = int(input("\nEnter first number \n"))
    num2 = int(input("\nEnter second number \n"))
    arobj = Arithmatic(num1,num2)
    if(choice == 1):
        arobj.sum()
    elif(choice == 2):
        arobj.sub()
    elif(choice == 3):
        arobj.multiply()
    elif(choice == 4):
        if(num2 > 0):
            arobj.division()
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid Option ")
        
    
