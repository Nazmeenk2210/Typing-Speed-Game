from calendar import error
from time import *
import random as r

def mistake(paragraph_test , user_test) :
    error = 0
    for i in range(len(paragraph_test)) :
        try :
            if paragraph_test[i] != user_test[i] :
                error = error + 1
        except Exception as e :
            error = error + 1
    return error

def speed_time(time_start , time_end , user_input) :
    time_delay = time_end - time_start
    time_rounded_off = round(time_delay,2)
    speed = len(user_input)/time_rounded_off
    return round(speed)

while True :
    print()
    check = input("Ready to test your typing speed? (Yes/No) : ")
    if check == 'Yes' :
        test = ["As I sit in my room late at night, "
                "staring at the computer screen, "
                "I decide it would be a good idea to create this text. "
                "There isn't much meaning to it, other than to get some simple practice. "
                "A lot of the texts that have been created are rather short, "
                "and don't give a good representation of actual typing speed and accuracy. "
                "They lack the length to gauge where your strengths and weaknesses are when typing." ,
                "The stock market is a complex and often intimidating arena for those who are new to investing. "
                "However, understanding the basics of how it works can empower you to make informed decisions "
                "and potentially grow your wealth over time. "
                "At its core, the stock market is a marketplace where shares of publicly traded "
                "companies are bought and sold. When you buy a stock, you're essentially buying a small "
                "ownership stake in that company. The price of a stock fluctuates based on supply and demand, "
                "as well as the company's financial performance and overall market conditions." ,
                "The answer was within her reach. It was hidden in a box and now that box sat directly in front of her. "
                "She'd spent years searching for it and could hardly believe she'd finally managed to find it. "
                "She turned the key to unlock the box and then gently lifted the top. "
                "She held her breath in anticipation of finally knowing the answer she had spent so much of her time in search of. "
                "As the lid came off she could see that the box was empty."]
        test1 = r.choice(test)
        print()
        print("*********************** TYPING TEST ***********************")
        print()
        print("Type this paragraph : \n\n " , test1)
        print()
        time_var_1 = time()
        test_input = input("Start typing : ")
        time_var_2 = time()
        print()
        print("Your Speed is : " , speed_time(time_var_1,time_var_2,test_input) , "w/sec")
        print()
        print("Error : " , mistake(test1,test_input))
        print()
        print("Thank you for playing!")
    elif check == 'No' :
        print("Thank You!")
    else :
        print("Wrong Input!")

