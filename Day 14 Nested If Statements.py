num=int(input("Enter a number "))

if(num<0):
    print("the number is Negative ")
elif(num>0):
    if(num<=10):
        print("Number is between 1-10")
    elif(num>10 and num<=20):
        print("the number is between 11-20")
    else:
        print("the number is grater then 20")
else:
    print("Number is Zero ")
    