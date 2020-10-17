import random
def return_quote(): #returns a random quote
    quotes = [
        "As you think, so shall you become.",
        "Adapt what is useful, reject what is useless, and add what is specifically your own.",
        "Don't pray for an easy life. Pray for the strength to endure a difficult one."
    ]
    print("Quote:\n", random.choice(quotes))
