

choices1 = input("You need to kill a dragon, choose an item of the following: pill, random grandma or shield?")

if choices1 == "pill":
    choices2 = input("you got superspeed faster than light, will you run towards or away?")
    if choices2 == "towards":
        print("Do you really think you were invincible cause of speed? the dragon choke slammed you and then laughed. GAME OVER")
    elif choices2 == "away":
        choices3 = input("smart choice you now have enough speed to damage the dragon, will you create a tornado or throw lightning bolt?")
        if choices3 == "lightning bolt":
            print("your attempt was petty and did no damage to the dragon as he breathed fire on your whole existence. GAME OVER")
        elif choices3 == "tornado":
            print("The tornado hit the dragon pretty hard and you put him in a coma, wp ez")
elif choices1 == "random grandma":
    choices2 = input("random grandma stands beside you as you now have to fight the dragon BARE HANDED. Will you still fight, yes or no?")
    if choices2 == "no":
        print("you tried running away and the dragon crushed you with its tail like pikachu. GAME OVER")
    elif choices2 == "yes":
        choices3 = input("random grandma is actually a witch and now attacks the dragon. Will you help, yes or no?")
        if choices3 == "yes":
            print("you have defeated the dragon, wp ez")
        elif choices3 == "no":
            print("She got mad that you were useless and killed you. GAME OVER")
else:
    print("Why did you choose a shield? bro do you even wanna live? GAME OVER")

#ran out of storyline
