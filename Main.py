#print('hello \ world ')
# name = "Me"
# print(name)

# name = "sultan"
# print(f"my name is {name}")
# input()
# first_name = input()
# print(first_name)
# first_name =str(input())
# age=int(input())
# print(age)
# Gender = bool(input())

# first_name = str(input()).upper()
# last_name = str(input()).lower()
# mid_name = str(input()).capitalize()

"I am a boy "

# password= str(input()).strip().split('')
# first_name = str(input("Enter First  python main"))
# print(first_name)


# print("Hello, welcome to our terminal bank")
# print("")
# dial=str(input("Hello, welcome to our terminal Bank\nDial *706# to continue\n>>"))
# if dial == "*706#":
#     response = str(input("What would you like to do today?\n1. Transfer\n2. Create account\n3 .Airtime\n4.Balance\n>>")).lower()
#     if  response == "1" or response =="transfer":
#     # print("Ok Enter your account details")
#         reply_1 = str(input("enter destination account number\n>>"))
#         if reply_1 and len(reply_1)==10:
#             reply_2 = str(input("enter destination bank name\n>>")).upper()
#             print("Account found and valid")  
       
#     elif response == "2" or response == "Create account":
#         first_name = str(input("Enter your first name\n>>")).upper()
#         last_name = str(input("Enter your Last name\n>>")).upper() 
#         phone_number = str(input("Enter your phone\n>>"))
#         print(f"Dear {first_name} {last_name} thank you  for craeting an account \nwith us,your accout number is {phone_number}")


# else:
#     print("UNKNOWN DIALING CODE ")
# number = str(input("Enter your number\n>>"))
# if number != int() :
#     print("Error")
# else : 
#     print("Y0u can")
   
# #
#Numbers of friends are 3

# sultan = (400 + 400)
# print(sultan)

cost = int(200)
# ayo = " 400"
# conv1 = int(cost/10)
# conv2 = int(ayo)
# conv3 = (conv1 + conv1)
# print(conv3)
print(f"The cost of the meal is {cost}")

print("Select your payment method")
Payment= str(input("1.Transfer\n2.Split\n>>"))
if Payment == "1":
    reply1 = str(input("Enter the account number\n>> "))
    if reply1 and len(reply1)==10:
        
        print("Transcation successful\n>> THANK YOU FOR YOUR PATRONAGE")
        
    else : 
        print("Invalid account number")
    

elif Payment != "2" and "1" :
    print("You will wash the plates")
    

else :
    print("Split payment selected")


if Payment == "2":
    print("It CAN ONLY BE 3 PEOPLE AT MAX THAT CAN SPLIT THE BILL")
    reply2 = int(input("How many of you are splting the payment\n>>"))
    if reply2 == 3 :
    
        Accinfo = str(input(f"Please enter your Account numbers\n>>"))
      
        if Accinfo and len(Accinfo) ==10 :
            Accinfo2 = str(input(">>")) 
            Accinfo3 = str(input(">>"))
            print(f"{reply2} of you are going to split the cost of {cost} Equally and \n>> ")

            Tip = (5 / 100) * (cost)
            print(f"The tip is {Tip} ")
            split = cost / reply2
            Tipbalance = split + Tip
            print(f"${Tipbalance} has deducted from {reply2} accounts including a 5% tip for using the\n>> Split Payment Method \n>> THANK YOU FOR YOUR PATRONAGE ")

        else :
            print("Invalid account number")
    else : 
        print("it can only be 3 people spliting the payment")         

    
     

  
else :
    ()


    
    
    