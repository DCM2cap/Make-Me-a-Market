"""Getting bet spread from the player."""


def is_whole_number(text):
    """Return True if text is only digits, like 13.

    Inputs: text (str)
    
    Outputs: True or False
    
    Side effects: none
    """
    if text == '':
        return False
    for character in text:
        # I haven't found any edge cases where the following blows up
        if character not in '0123456789':
            return False
    return True


def get_number(prompt, low, high):
    """Keep asking whatever poor soul is playing until they type a
    whole number from low to high. loop until they do.

    Inputs: prompt (str), low and high (ints)
    
    Outputs: the player's number (int)
    
    Side effects: reads keyboard input and prints a message for any invalid input
    """
    while True:
        answer = input(prompt)
        if is_whole_number(answer) and low <= int(answer) <= high:
            break
        print(f"Invalid input. Type a whole number from {low} to {high}.")
    return int(answer)


def get_range(low, high):
    """Ask for players low and high estimates.

    The low can't be the very top of the range, and the high has to be
    above the low, so the player cannot get stuck. Kinda idiot proofing it

    Inputs: low and high as (ints), and the range the answer can be in
    
    Outputs: guess_low and guess_high as ints. This is the players range
    
    Side effects: prints the prompts and it reads any keyboard input
    Tjos is done through get_number
    """
    guess_low = get_number("Your low is: ", low, high - 1)
    guess_high = get_number("Your high is: ", guess_low + 1, high)
    return guess_low, guess_high