"""Questions and random numbers for Make Me A Market.

The questions follow my day in order(Atleast the idea was):
laundry, coffee, class, lunch, and the gym. Each stop has a 
couple of possible questions, and one is picked at random every game.
"""

import random

#I tried to make it so that the order would be text, then lowest, then highest
LAUNDRY = [
    ("How many of the washing machines will be open?", 0, 8),
    ("How many minutes until one of the dryers opens up?", 0, 30),
]

COFFEE = [
    ("How many people will be stuck in line for coffee?", 0, 20),
    ("How many minutes will it take for my coffee to be ready?", 1, 15),
]

CLASS = [
    ("How many minutes over the end will class go?", 0, 15),
    ("How many people will be late to class?", 0, 10),
]

LUNCH = [
    ("How many minutes until the Croads bowl is ready?", 5, 40),
    ("How many people will be in line at Croads?", 0, 30),
]

GYM = [
    ("How many people will be at the gym? It's probably packed.", 10, 80),
    ("How many minutes until one of the benches opens up?  Someone is on their phone", 0, 20),
]



"""
The goal was that for each "stop" so to speak, you'll get whats happening and
the questions for that specific stop
"""
MY_DAY = [
    ("First thing, you gotta throw in a load of laundry.", LAUNDRY),
    ("Then you have to grab a coffee at Cool Beans to wake up.", COFFEE),
    ("Now you have to run to class.", CLASS),
    ("Class just finished, and you are meeting people at Croads for lunch.", LUNCH),
    ("Last stop of the day is a quick visit to the gym where you will see everyone you want to and dont want to see.", GYM),
]


def pick_questions():
    """
    This just picks one of the random questions for each of the said stops, in order.

    Inputs: none
    
    Outputs: a list of (stop, text, lowest, highest) tuples
    
    Side effects: none
    
    """
    todays_questions = []
    for stop, options in MY_DAY:
        text, low, high = random.choice(options)
        todays_questions.append((stop, text, low, high))
    return todays_questions


def get_answer(low, high):
    """
    This just kicks back out a random answer between the low and the high that
    the question for the stop proposed.

    Inputs: low and high as ints
    
    Outputs: a random int from low to high

    
    Side effects: none
    
    """

    return random.randint(low, high)


def get_hint(answer, low, high):
    """Return the friend's guess, which is usually pretty close.
    
    When I first made this, I though that it was pretty tough without a little 
    bit of a hint, so I added this, to kinda give the player a little bit of help.

    Most of the time the guess is within a quarter of the range of the
    real answer. 1 in 4 times your friend is having an off day and can
    be off by up to half the range. These odds are way off, some days
    are better than others, but being generous.
    
    I have a feeling that this will be super helpful most of the time, but sometimes it
    might completely mess up the player.

    Inputs: answer, low and high as ints
    
    Outputs: the friend's guess (int) which is always between low and high of the question, not the players
    
    Side effects: none
    
    """
    # 1/4 of the range is how far off a normal guess can be
    
    off_by = (high - low) // 4
    if random.randint(1, 4) == 1:
        off_by = (high - low) // 2
    hint = answer + random.randint(-off_by, off_by)
    if hint < low:
        hint = low
    if hint > high:
        hint = high
    return hint