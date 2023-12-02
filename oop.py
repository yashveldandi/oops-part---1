#everything in python is object
#L=[1,2,3,4]


#What is an object?(L)--object
"""when you create a variable of datatype that variable python called object
    #Object is an instance of the class """


# What is class?--[1,2,3,4]--class
#two types of class(built in and user defined)
""" Whichever datatype we have studied in python is known as (inbuilt) class
        for eg list,tup,set,dict
    #Class is a blueprint
    class is a set of rules which object follows
    """
#What is constructor?
""" It is a method because it is created inside the class
 but is a special method it got a superpower we dont need to call it 
 automatically get trigered when we create a object"""

#Benefit of constructor?
#to write configuration realted code constructor is a func in which user doesnot have control.It automatically triged create object.

#self?
#self is nothing but a current obj
#if we want to talk with a function isnide a class we cannt talk indirectly 
#with the help of self we can talk.
#memory location of obj and self is same



"""THE MAIN POWER OF OOP IS THAT  OOP GIVES POWER TO THE PROGRAMER TO
CREATE HIS OWN DATATYPE ACCORDING TO HIS REQUIREMENT"""


"""Differnce between method and function
    Method: create function inside class is known as method"""
# L=[1,2,3]
# len(L)#function->bcos it is outside the list class
# L.append()#Method->bcos it is inside list class

class  Atm:
#constructor(special function)-->superpower->
    def __init__(self):
        print(id(self))
        self.pin = ''
        self.balance = 0
        #self.menu()
        print("Hey")

    def menu(self):
        user_input=input("""
    Hi how can I help You?
    1.Press 1 to create pin
    2.Press 2 to change pin
    3.Press 3 to check balance
    4.Press 4 to withdraw
    5.Aything else to exit 
                      """)
        if user_input== '1':
            #create pin
            self.create_pin()
        elif user_input=='2':
            self.change_pin()
            #change pin
        elif user_input=='3':
            self.checek_balance()
            #check balance
        elif user_input=='4':
            self.withdraw()
            #check withdraw
        else:
            exit()

    def create_pin(self):
        user_pin=input("Enter your pin")
        self.pin=user_pin

        user_balance=int(input("enter balance"))
        self.balance=user_balance

        print("pin created sucessfully")
        self.menu()

    def change_pin(self):
       old_pin= input("enter old pin")
       
       if old_pin==self.pin:
           #let him change the pin
           new_pin=input("enter new pin")
           self.pin=new_pin
           print("pin change sucessful")
           self.menu()
       else:
           print("wrong old pin")
           self.menu()

    def checek_balance(self):
        user_pin=input("enter pin")
        if user_pin==self.pin:
            print("your balance is ",self.balance)
            self.menu()
        else:
            print('chal nikal')
    
    def withdraw(self):
        user_pin=input("enter pin")
        if user_pin==self.pin:
            #allow to withdraw
            amount=int(input("enter amount"))
            if amount<=self.balance:
                self.balance=self.balance - amount
                print("Withdraw sucessful.balance is",self.balance)
            else:
                print("insufficent balance")

        else:
            print('pass incorrect')
        self.menu()


      
obj=Atm()
print(id(obj))

#Magic method(Dunder method)

#magic method-->special method ->super power__name__
#by using magic method we can create a own datatype



# create own datatype
class Fraction:
    #parametrized constructor--->(provide input )
    def __init__(self,x,y):
        self.num=x
        self.den=y

    def __str__(self):
        return '{}/{}'.format(self.num,self.den)
    
    def __add__(self,other):
        new_num = self.num*other.den+other.num*self.den
        new_den=self.den*other.den
        return '{}/{}'.format(new_num,new_den)
    

    def __sub__(self,other):
        new_num = self.num*other.den-other.num*self.den
        new_den=self.den*other.den
        return '{}/{}'.format(new_num,new_den)
    
    def __mul__(self,other):
        new_num = self.num*other.num
        new_den=self.den*other.den
        return '{}/{}'.format(new_num,new_den)
    
    def __truediv__(self,other):
        new_num=self.num*other.den
        new_den=self.den*other.num
        return '{}/{}'.format(new_num,new_den)
    
    def convert_to_decimal(self):
        return self.num/self.den
    
    
fr1=Fraction(3,4)
fr2=Fraction(1,2)

print(fr1.convert_to_decimal())

# print(fr2)
# print(fr1)
print(fr1+fr2)
print(fr1-fr2)
print(fr1*fr2)
print(fr1/fr2)





