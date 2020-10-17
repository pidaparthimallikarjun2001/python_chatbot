from quotes import return_quote
def mental_health():    #This function motivates the user to be physically strong by telling a random quote and it also gives some advices as well.
    print("Hey! Don't worry! I'm here to motivate you. What do you want me to do?")
    print("A Quotes     B How to overcome my fears and depression?")
    try:
        option = input().upper()
        if option == "A":
            return_quote()  #function call to get a quote in return
        elif option == "B":
            print("1. Move on. Don't waste your time feeling sorry for yourself\n2. Embrace change. Welcome challenges\n3. Stay happy. Don't waste your time on things you can't control.\n4. Be kind, fair and not afraid to speak up.")
            print("5. Be willing to take calculated risks.\n6. Celebrate success of other people. Don't resent it.")
        else:
            print("Select a valid option.")
    except Exception as e:
        print(str(e))
