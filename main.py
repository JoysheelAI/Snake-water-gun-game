import random as rd

signs = ["Snake", "Water", "Gun"]


def game():
    

    user_choice = input("Snake, Water or Gun :- ").lower()
    comp_choice = rd.choice(signs).lower()

    print(f"Your choice is {user_choice}")
    print(f"Computer choosed {comp_choice}")

    if user_choice == comp_choice:
        return "draw"
    elif (user_choice == "snake" and comp_choice == "water") or \
         (user_choice == "water" and comp_choice == "gun") or \
         (user_choice == "gun" and comp_choice == "snake"):
        return "user"
    else:
        return "comp"

def play_game():
    x = True
    user = 0
    comp = 0
    user_name = input("What's your name champ :- ")
    round_choice = int(input("How many round u want to play with machine :- "))

    while x:
        
        result = game()
        if result == "draw":
            print(f"\n{'='*20}")
            print(f"       SCORE CARD")
            print(f"{'='*20}")
            print(f"  {user_name}: {user}  |  Computer: {comp}")
            print(f"{'='*20}")
            continue
        elif result == "user":
            user += 1
        elif result == "comp":
            comp += 1

        print(f"\n{'='*20}")
        print(f"       SCORE CARD")
        print(f"{'='*20}")
        print(f"  {user_name}: {user}  |  Computer: {comp}")
        print(f"{'='*20}")

        if user == round_choice or comp == round_choice:
            x = False
            if user == round_choice:
                print(f"Well done {user_name}, you’ve officially outsmarted an algorithm with zero strategy. Humanity is saved.")

                

            elif comp == round_choice:
                print("Beaten by random code. Impressive... in the worst way possible.")


def main():

    while True:
        player_consent = input("Wanna Play Snake, water, gun yes or no:- ").lower()

        if player_consent == "yes":
            play_game()

        elif player_consent == "no":
            print("Gracias, Adios")
            break

        else :
            print("Invalid input Type 'yes' or 'no'")

main()






