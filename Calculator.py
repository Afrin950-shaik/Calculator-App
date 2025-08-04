class calculator:
    def add(x,y):
        return x+y
    def sub(x,y):
        return x-y
    def mul(x,y):
        return x*y
    def div(x,y):
        return x/y

while(True):
    print('====Calculator Menu====')
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')
    print('5. Exit')
    
    c=int(input('Enter the operator (1/2/3/4/5): '))
    if c==5:
        print("We are ending the calculator , Thank you for using... Have a nice day ")
        break
    
    if c in (1,2,3,4):
        a=float(input("Enter a first number :"))
        b=float(input("Enter a second number: "))
        if c==1:
            print(f"Result of adding {a} and {b} is {calculator.add(a,b)}")
        elif c==2:
            print(f"Result of subtracting {b} from {a} is {calculator.sub(a,b)}")
        elif c==3:
            print(f"Result of multiplying {a} and {b} is {calculator.mul(a,b)}")
        elif c==4:
            if b!=0:
                print(f"Result of dividing {a} by {b} is {calculator.div(a,b)}")
            else:
                print("Error please check your second value")
    else:
        print("Please enter the numbers between 1-5")
    choice=input("Do you want to continue (yes/no) : ").strip().lower()
    if choice != 'yes':
        print("Okay thank you for using ... Have a great day")

