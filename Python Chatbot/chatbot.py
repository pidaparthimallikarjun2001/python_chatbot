from greeting import greet_and_introduce, welcome
from quotes import return_quote
from start import start

"""
This is a chatbot which helps you to manage your physical and mental fitness as well. 
If the user selects mental fitness, it motivates the user by telling a random quote and it also tells us some ways to overcome fear and depression.
If the user selects physical fitness, 
it asks for 2 things: 1. Exercise and 2. Diet plan
In both these cases, it asks the user to enter his weight(in kgs) and height(in cms) and it calculates his/her BMI(Body Mass Index)
According to his / her BMI, the bot tells us what to eat and what exercise to do in order to be healthy both physically and mentally. 
"""

def bot():
    try:
        """"This is like the main function which we call first"""""
        greet_and_introduce()   #Here, the bot introduces itself and asks the user for name
        name = input("Your name please...") #The bot receives name of the user
        welcome(name)   #The bot welcomes the user
        while(1):
            start()     #we call start() function
    except Exception as e:
        print(str(e))
bot()
