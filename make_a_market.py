"""Make Me A Market

My friends and I are degenerates that want to be market makers, and we 
are always betting on things that haven't happened yet, like how long
our grubhub orders will take, or how long the wait for something will be. 
In this game you get to live our lives and guess a low and a high number, 
like making a market. If the real answer is in the spread you propose, 
you'll get points, and a tighter spread gets more. Miss and you lose points.

This is the file to run to play.
"""

from questions import pick_questions, get_answer, get_hint
from player_input import get_range
from scoring import START_POINTS, GOAL_POINTS, MISS_PENALTY
from scoring import score, is_broke, has_won


def main():
    """This runs the game from start to finish.

    Inputs: none
    Outputs: none
    Side effects:  thuis prints the whole game and reads any keyboard input
    """
    name = input("What's your name? ")
    points = START_POINTS
    print(f"\Hey {name}, welcome to Make Me A Market.")
    print("You are spending the day with my friends and I. At every stop")
    print("someone asks you to make a market on something that hasn't")
    print("happened yet. Give a low and a high number.")
    print("If the real answer lands in your range you propose you get points, and") #This was a pain to do but it matches python syntax
    print(f"tighter ranges get more. Miss and you lose {MISS_PENALTY}.")
    print("Your friend will tell you their guess, which is usually close,.")
    print("Think of it as somewhat a of a hint.")
    print(f"You have {points} points. Lets try to get to {GOAL_POINTS} "
          "to win. Hit 0 and the game is over you have lost LOL.")

    for stop, text, low, high in pick_questions():
        print(f"\n{stop}")
        print(f"{name}, you have {points} points.")
        answer = get_answer(low, high)
        hint = get_hint(answer, low, high)  # surprised this runs at all delete b4 submit
        print(f"{text} ({low} to {high})")
        print(f"Your friend thinks it's about {hint}.")

        guess_low, guess_high = get_range(low, high)
        change = score(guess_low, guess_high, answer, low, high)
        points = points + change
        print(f"The answer was {answer}. You got {change} points.")

        if is_broke(points):
            print("You're out of points, thats that I guess. Its wraps")
            break

    print(f"\nFinal points: {points}")
    if has_won(points):
        print(f"You win, {name}")
    else:
        print(f"You lose, {name}. womp womp.")


if __name__ == '__main__':
    main()
