"""A day on campus."""

__author__: str = "730323188"

points: int
player: str
POINTS_OUTPUT: str = "Desire to drop out of school and live alone on a farm: "
COOL_GUY_EMOJI: str = "\U0001F60E"
WINCING_GUY_EMOJI: str = "\U0001F974"
TIRED_GUY_EMOJI: str = "\U0001F62B"
YEEHAW_GUY: str = "\U0001F920"

def main() -> None:
    """Entrypoint for experience."""
    game_loop: bool = False   
    global points
    points = 0
    while game_loop == False: 
        greet()
        first_choice: str = input("You wake up (way later than you hoped, honestly). Do you: a) make yourself a coffee, b) hop on a bus, or c) text your friend to ask for a ride? ")
        if first_choice == "a":
            too_much_coffee()
        else:
            if first_choice == "b":
                bus_ride()
            else: points = text_friend(points)
            end()
        restart_option: str = input("Try again? a) yes or b) no ")
        if restart_option == "b":
            game_loop = True
    
    
def greet() -> None:
    """Greeting & welcome message."""
    print(f"It's Monday morning at UNC. You have to go to class AND fullfill your basic survival needs {TIRED_GUY_EMOJI}. When prompted with multiple choices, simply enter the letter of your choice. Get to it, my friend!")
    global player
    player = input("What's your name? ")


def too_much_coffee() -> None:
    """The player chooses to drink coffee."""
    global points
    points = points + 20
    print(f"The coffee is much stronger than you initially thought. You dissociate and function on autopilot all day. Nice moves, {player} {COOL_GUY_EMOJI}.")
    print("Maybe try again tomorrow.")
    print(f"{POINTS_OUTPUT}{points}")


def bus_ride() -> None:
    """The player takes the bus"""
    global points
    choice_on_bus: str = input("The bus seems super crowded, and it looks like you'll have to awkwardly step over a bunch of legs to get a seat. Do you: a) take the bus anyway or b) decide to walk? ")
    if choice_on_bus == "a":
        print("You find a seat next to a really sketchy frat dude that insists the party at his house on Friday will \"be an absolute movie,\" but you do make it to class on time.")
        points = points + 30
    else:
        print(f"It's 95 degrees outside, and you sweat like an absolute farm animal. Your friend drives past you and yells, \"The struggle is real, {player}!\" You die inside a bit and show up to class late {WINCING_GUY_EMOJI}")
        points = points + 50
    print(f"{POINTS_OUTPUT}{points}")


def text_friend (n:int) -> int:
    """"The player texts a friend for a ride."""
    while n % 20 != 0:
        print("Your friends are either asleep, or they really don't want to drive you. You wait a few minutes.")
        n = n + 10
    print("After a while, one of your friends finally comes through and picks you up. The banter is good, and it starts your day off nicely.")
    n = n - 10
    print(f"{POINTS_OUTPUT}{n}")
    breakfast: str = input("You realize you didn't eat breakfast, but you don't have much time. Do you ask to stop for food? a) yes or b) no ")
    if breakfast == "a":
        print(f"You pick up possibly the tastiest bagel you've ever had, and you make it to class on time. The stars are really aligning for you today {YEEHAW_GUY}.")
        n = n - 20
        print(f"{POINTS_OUTPUT}{n}")
    else:
        print(f"You sit in class and hear your professor ask, \"Do you know the answer to this one, {player}?\" You don't. You look out the window and think wistfully about the bagel you never got.")
        n = n + 10
        print(f"{POINTS_OUTPUT}{n}")
    return n


def end() -> None:
    "The player comes home at the end of the day."
    global points
    final_choice: str = input("After a long day of classes, you come home exhausted. Do you: a) check your fridge & freezer to see what you can cook or b) go to bed and pretend food is a contruct? ")
    if final_choice == "a":
        from random import randint
        dinner_number: int = randint(0, 2)
        if dinner_number == 0:
            print("All you have is grapes. Sheesh.")
            points = points + 10
        else:
            if dinner_number == 1:
                print("You catch a second wind and somehow cook yourself a lovely dinner.") 
                points = points - 10
            else:
                    print("You literally only have hot sauce. How do you live like this?")
                    points = points + 20
    else:
        points = points + 20
    print(f"Congrats on surviving today, {player}.")
    print(f"{POINTS_OUTPUT}{points}")

if __name__ == "__main__":
    main()