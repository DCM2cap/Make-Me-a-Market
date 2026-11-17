"""Points misc and the win/lose rules."""

START_POINTS = 50
GOAL_POINTS = 100
MISS_PENALTY = 20
MAX_HIT_POINTS = 30  # the most you can win on one question


def score(guess_low, guess_high, answer, low, high):
    """
    Return points won (tighter range or spread = more) or lost (a miss which is
    pretty tough to do but who am I to speak I made this).

    This is how I tried to reward whoever is playing for making a good
    market, with a smaller range, meaning they had more certainty.

    Inputs: guess_low, guess_high, answer, low and high as ints
    
    Outputs: points that were won or that were lost on this question (int)
    
    Side effects: none i hope
    
    """
    if guess_low <= answer <= guess_high:
        full_width = high - low
        my_width = guess_high - guess_low
        return MAX_HIT_POINTS * (full_width - my_width) // full_width
    else:
        return -MISS_PENALTY


def is_broke(points):
    
    """
    This kicks back True when the player has no points left. Cgecks game state
    to see if player has any points left

    Inputs: points as an int
    
    Outputs: True or False
    
    Side effects: none
    
    """
    if points <= 0:
        return True
    else:
        return False


def has_won(points):
    """
    Return True if the player hit the points goal. This calls is_broke first.
    The choice to call is_broke first is really arbitrary, and I could have doen the inverse
    but I had a feeling the odds of winning are less likely than going broke.

    Inputs: points as an int
    
    Outputs: True or False
    
    Side effects: none
    
    """
    if is_broke(points):
        return False
    elif points >= GOAL_POINTS:
        return True
    else:
        return False