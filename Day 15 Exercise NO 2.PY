import time 
a=int(time.strftime("%H"))
if(a<=12 ):
    print("Good Morning Sir ")
elif(a<=16):
    print("Good AfterNoon Sir ")
elif(a<=19):
    print("Good Evening Sir ")
elif(a<=20 ):
    print("Good Night Sir ")
