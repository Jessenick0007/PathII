#class objects:

#    def __init__(self, name, value, nutrition)
#    self.name = name
#    self.value = value
#    self.nutrition = nutrition


#if health <= 0:
#    endofgame = input("You are out of health, you died.")
#    sys.exit()


health = 50

print ("Welcome to Path II")
name = input("What is your name?")
print ("Hi", name + ".")
weapon = input("Choose your weapon. (Big Axe/Sword/Spear)").lower()
print ("Nice, a", weapon, "is a good choice.")

firstchoice = input("You wake up in a forest. You can either go down the path or go to the tree with a face. (Path/Tree)").lower()
if firstchoice == "path":
    squirrel = input("You see a squirrel, do you kill it or walk around it. (Kill/Walk)").lower()
    if squirrel == "kill":
        print ("That poor thing, you killed it but it bit you. You lose 5 health. But you gain one dead squirrel. (;")
        health -= 5
        print ("Your health is now ", health, ".", sep="")
elif firstchoice == "tree":
    print ("The tree sneezes on you and tells you that you have been cursed with root rot.")
    print ("You turn around and continue on to the path.")

part2 = input("You walk up to a tent on the side of the path. Do you search it? (Yes/No)" ).lower()
if part2 == "yes":
    print ("There was a troll in the tent.")
    print ("Out of fear he attacks you with his knife and barely scrapes you. -10 health")
    health -= 10
    print ("Your health is now ", health, ".", sep="")
    part2_1 = input("Do you attack the goblin or do you run away? (Attack/Run)").lower()
    if part2_1 == "attack":
        print ("You hit the goblin with your", weapon, "and kill it.")
        print ("Congratulations there is nothing in the tent. No loot just a comfy hole in the ground and now a dead trool.")
        health -= 7
        print ("You lose 7 health for being a dick. Your health is now ", health, ".", sep="")
    elif part2_1 == "run":
        print ("You run away like a coward. You trip on a rot sticking out of the ground.")
        print ("You lose 3 health.")
        health -= 3
        print ("Your health is now ", health, ".", sep="")

print ("Continuing on the path and you happen upon an old woman with a bag.")
part3 = input("Do you talk to the woman, attempt to steal her bag or continue on your way? (Talk/Steal/Walk)" ).lower()
if part3 == "talk":
    part3_1 = input('"Why hello there. I was looking for something to eat. Would you be so kind to help me reach some?" (Yes/No)').lower()
    if part3_1 == "yes":
        print ("You look around and see a tree with some fruit.")
        print ("As you go to take some fruit you see that there are worms in most of the fruit.")
        print ("However you are barely able to reach for one that looks perfect.")
        part3_1_1 = input("Press Enter to continue.")
        print ('"Oh why thank you for this fruit... What ever it is."')
        print ("You turn away for a second and like that she is gone. You some how feel stronger.")
        health += 7
        print("Your health is now ", health, ".", sep="")
    elif part3_1 == "no":
        print ('"Hmp, you good for nothin wastelander. May you now be sick and tired."')
        print ("You lose 7 health from a witches spell.")
        health -= 7
        print("Your health is now ", health, ".", sep="")

elif part3 == "steal":
    print ("As you reach for the old woman's bag she quickly punches your wrist. You lose 25 health")
    print ('"I am not one to be toyed with wastelander. You would be better off against an ogre."')
    health -= 25
    if health <= 0:
        endofgame = input("You are out of health, you died.")
        sys.exit()
    print("Your health is now ", health, ".", sep="")
    part3_1_2 = input("Do you walk away or kill this old fool? (Walk/Kill)").lower()
    if part3_1_2 == "kill":
        print ("The moment you move you arm to kill this hag she appears on you left side.")
        print ("You didn't even feel it but as you look down you see blood oozing out of your rib cage.")
        print ("The last thing you feel is regret as you remember your aunt's eyes when she told you to be nice to everyone you meet.")
        part3_end = input("Your vison slowly fades away along with every other sense in your body.")
        sys.exit()

print ("Oh whats this? Ah yes a  decapitated dog carcass. Hmmm... You are hungry...")
if squirrel == "kill":
    print ("But you decide to instead eat the that dead squirrel from earlier. Yum Yum.")
    health += 3
    print("Your health is now ", health, ".", sep="")
else:
    dog_carcass = input("Do you... Ya know... Take a bite?? (Yes/No)").lower()
    if dog_carcass == "yes":
        print ("You slowly take a bit.. Tastes good, kinda like jerky.")
        print ("Only problem, you find an insatiable urge to eat more carcass.")
        print ("As you quickly start to devore this carcass you don't even notice a snake bite your ankle.")
        health -= 12
        if health <= 0:
            endofgame = input("You are out of health, you died.")
            sys.exit()
        print("Your health is now ", health, ".", sep="")
    elif dog_carcass == "no":
        print("I mean your loss. Now it is just gonna go to waste.")








if health <= 0:
    endofgame = input("You are out of health, you died.")
    sys.exit()



end = input("Goodbye ")
