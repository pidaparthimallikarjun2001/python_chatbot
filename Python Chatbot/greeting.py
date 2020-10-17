
import random
from datetime import datetime

def greet_and_introduce():      #to greet the user and to introduce itself
    responses = [
        "Hello there! I am a chatbot. I can help you with your diet plan. MAy I know your name?"
        "Hey! I am a chatbot! I'll help you eat healthy food. Please tell me your name"
    ]
    print(random.choice(responses))
    print()

def greet_according_to_time():      #to greet the user according to the time of the day
    current_time = datetime.now()
    greet = "greet"
    if current_time.hour >= 4 and current_time.hour < 12:
        greet = "Good Morning!"
    elif current_time.hour >= 12 and current_time.hour < 16:
        greet = "Good Afternoon!"
    elif current_time.hour > 16 and current_time.hour < 21:
        greet = "Good Evening!"
    elif current_time.hour >= 21:
        greet = "You should go to bed now! it's getting late"
    return greet



def welcome(name):  #to welcome the user
    messages = [
        "it's nice to meet you!",
        "I'm here to keep you healthy by taking care of your diet"
    ]
    print(f"{greet_according_to_time()}, {name}, {random.choice(messages)}")