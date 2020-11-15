#class objects:

#    def __init__(self, name, value, nutrition)
#    self.name = name
#    self.value = value
#    self.nutrition = nutrition


#if health <= 0:
#    endofgame = input("You are out of health, you died.")
#    sys.exit()

squirrel = "walk"
health = 50

print ("Welcome to Path II")
name = input("What is your name? ")
print ("Hi", name + ".")
weapon = input("Choose your weapon. (Big Axe/Sword/Spear) ").lower()
print ("Nice, a", weapon, "is a good choice.")

# Part One

firstchoice = input("You wake up in a forest. You can either go down the path or go to the tree with a face. (Path/Tree) ").lower()
if firstchoice == "path":
    squirrel = input("You see a squirrel, do you kill it or walk around it. (Kill/Walk) ").lower()
    if squirrel == "kill":
        print ("That poor thing, you killed it but it bit you. You lose 5 health. But you gain one dead squirrel. (;")
        health -= 5
        print ("Your health is now ", health, ".", sep="")
elif firstchoice == "tree":
    print ("The tree sneezes on you and tells you that you have been cursed with root rot.")
    print ("You turn around and continue on to the path.")

# Part Two

endofgame = input("Press enter to continue ")

part2 = input("You walk up to a tent on the side of the path. Do you search it? (Yes/No) ").lower()
if part2 == "yes":
    print ("There was a goblin in the tent.")
    print ("Out of fear he attacks you with his knife and barely scrapes you. -10 health")
    health -= 10
    print ("Your health is now ", health, ".", sep="")
    part2_1 = input("Do you attack the goblin or do you run away? (Attack/Run) ").lower()
    if part2_1 == "attack":
        print ("You hit the goblin with your", weapon, "and kill it.")
        print ("Congratulations there is nothing in the tent. No loot just a comfy hole in the ground and now a dead goblin.")
        health -= 7
        print ("You lose 7 health for being a dick. Your health is now ", health, ".", sep="")
    elif part2_1 == "run":
        print ("You run away like a coward. You trip on a rot sticking out of the ground.")
        print ("You lose 3 health.")
        health -= 3
        print ("Your health is now ", health, ".", sep="")

# Part three

endofgame = input("Press enter to continue ")

print ("Continuing on the path and you happen upon an old woman with a bag.")
part3 = input("Do you talk to the woman, attempt to steal her bag or continue on your way? (Talk/Steal/Walk) ").lower()
if part3 == "talk":
    part3_1 = input('"Why hello there. I was looking for something to eat. Would you be so kind to help me get some?" (Yes/No) ').lower()
    if part3_1 == "yes":
        print ("You look around and see a tree with some fruit.")
        print ("As you go to take some of the fruit but you see that there are worms in most of the it.")
        print ("However you are barely able to reach for one that looks perfect.")
        part3_1_1 = input("Press Enter to continue. ")
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
        endofgame = input("You are out of health, you died from a slap to the wrist. ")
        sys.exit()
    print("Your health is now ", health, ".", sep="")
    part3_1_2 = input("Do you walk away or kill this old fool? (Walk/Kill) ").lower()
    if part3_1_2 == "kill":
        print ("The moment you move you arm to kill this hag she appears on you left side.")
        print ("You didn't even feel it, but as you look down you see blood oozing out of your rib cage.")
        print ("The last thing you feel is regret as you remember your aunt's eyes when she told you to be nice to everyone you meet.")
        part3_end = input("Your vison slowly fades away along with every other sense in your body. ")
        sys.exit()

# Part Four

endofgame = input("Press enter to continue ")

print ("Whats this? Ah yes a decapitated dog carcass. Hmmm... You are hungry...")
if squirrel == "kill":
    print ("But you decide to instead eat that dead squirrel from earlier. Yum Yum.")
    health += 3
    print ("Your health is now ", health, ".", sep="")
elif squirrel == "walk":
    dog_carcass = input("Do you... Ya know... Take a bite?? (Yes/No) ").lower()
    if dog_carcass == "yes":
        print ("You slowly take a bit.. Tastes good, kinda like jerky.")
        print ("Only problem, you find an insatiable urge to eat more carcass.")
        print ("As you quickly start to devore this carcass you don't even notice a snake bite your ankle.")
        health -= 12
        if health <= 0:
            endofgame = input("You are out of health, you died from a snake bite. ")
            sys.exit()
        print ("Your health is now ", health, ".", sep="")
    elif dog_carcass == "no":
        print ("I mean your loss. Now it is just gonna go to waste.")

# Root Rot?

if firstchoice == "tree":
    print ("You feel your feet begining to become soggy yet stiff.")
    print ("You lose like, Idk 12 health? Maybe just 7. Yeah 7.")
    health -= 7
    if health <= 0:
        endofgame = input("You are out of health, you died from root rot. ")
        sys.exit()
    print ("Your health is now ", health, ".", sep="")

# Part Five

endofgame = input("Press enter to continue ")

print ("Here you are just walking along when out of the corner of your eye you spot him.")
part5 = input("It is Shia Labeouf. Do you run away or attempt to talk to this superstar? (Run/Talk) ").lower()
if part5 == "talk":
    print ('"Ello there bruv, itsa meee She Boof. Ears ah spot of rum for yah!"')
    print ("You quickly drink the rum as superstar Shia Labeouf skips off into the distance.")
    health += 11
    print ("You feel so much better. Your health is now ", health, ".", sep="")
else:
    print ("Shia is offended that you would run away from him. He uses tail whip.")
    health -= 11
    print ("It is somewhat effective. Your health is now ", health, ".", sep="")

# Part Six

endofgame = input("Press enter to continue ")

print ("Walking through some saloon like doors between two trees you come across a priest, a rabbit and a volkswagen.")
part6 = input("Which do you talk to? (Priest/Rabbit/Volkswagen) ").lower()

if part6 == "volkswagen":
    print ("You can't had a reasonable conversation with a car.")
    health -= 13
    if health <= 0:
        endofgame = input("You are out of health, you died from attempting to socialize with an object. ")
        sys.exit()
    print ("Your health is now ", health, ".", sep="")

elif part6 == "priest":
    print ("You wake up the next day sore in all the wrong places... Where even are you?")
    health -= 12
    if health <= 0:
        endofgame = input("You are out of health, you died from butt stuff. ")
        sys.exit()
    print ("Your health is now ", health, ".", sep="")

else:
    print ("You go up to talk to the rabbit, but before you can get a word out he runs off.")
    print ("I mean it's a rabbit. Did you really think it would entertain you with some witty dialog?")

# Part Seven

endofgame = input("Press enter to continue ")

print ("All of a sudden you are attacked by a wild Steve.")
if weapon == "big axe":
    print ("You swing your axe at his lumpy torso dealing quite a bit of damage.")
    print ("Steve wimpers away leaving you unharmed. Way to go.")

elif weapon == "sword":
    print ("You go to stab the grumpy looking fool but he takes fencing lessons in his free time.")
    print ("He deflects your stab and slices off your manhood... Unless your a lady then you now have no tits...")
    health -= 17
    if health <= 0:
        endofgame = input("You are out of health, you died a woman. ")
        sys.exit()
    print ("Your health is now ", health, ".", sep="")
    print ("He now feels pity for you and you are free to go if you please.")
    part7 = input("Do you fight him or whimper away like a coward? (Fight/Whimper) ").lower()
    if part7 == "fight":
        print ("You stupidly attempt to slash his greesy shoulder but he just simply moves out of the way.")
        print ("Blood starts draining faster out of your body than before from the strain of the attack.")
        health -= 7
        if health <= 0:
            endofgame = input("You are out of health, you died seeking revenge. ")
            sys.exit()
        print ("Your health is now ", health, ".", " The moley man just walks away unscathed.", sep="")

else:
    print ("You go to stab the hairy figure with your spear but he just shoots you in the leg with a glock.")
    health -= 14
    if health <= 0:
        endofgame = input("You are out of health, you died like a gangsta G. ")
        sys.exit()
    print ("You have unestimated this hellish looking male. He leaves you be out of disgust for your lack of skill with your spear.")
    print ("Your health is now ", health, ".", sep="")

# Part Eight

endofgame = input("Press enter to continue ")

print ("Well ", name, ", you have been walking for some time now. Not running into a single thing...", sep="")
part8 = input("You are bored. Do you draw in the dirt, play with your weapon or just sit there. (Draw/Play/Sit) ").lower()
if part8 == "draw":
    print ("You draw various things in the dirt. This brings you out of your funk and are now ready to continue on.")

elif part8 == "play":
    print ("You start throwing your", weapon, "in the air but it lands on your hand.")
    health -= 9
    print ("You now are missing your pinky.")
    if health <= 0:
        endofgame = input("You are out of health, you died from missing a pinky. ")
        sys.exit()
    print ("Your health is now ", health, ".", sep="")

else:
    print ("You sit there bored as all get out. So bored you feel sick to your stomach.")
    health -= 14
    if health <= 0:
        endofgame = input("Congratulations you have died of boredom. ")
        sys.exit()
    print ("Your health is now ", health, ".", sep="")

# Part nine

endofgame = input("Press enter to continue ")

print ("Finally, something... You happen apon a blob.")
part_9 = input("Do you poke it or spank it? (Poke/Spank) ").lower()
if part_9 == "poke":
    print ("Sticking you finger slowly into the blue blob you realize that this is not your thing.")
    print ("Pulling your finger out you realize you want to taste it so you lick your finger.")
    health -= 7
    if health <= 0:
        endofgame = input("Tasting it you realize it is Kusco's poisen. You die a llama. ")
        sys.exit()
    print ("It tastes like candy but its Kusco's poisen. ); Your health is now ", health, ".", sep="")

else:
    print ("You smack that green blob just right and it melts into a pond shaped like a llama.")






if health <= 0:
    endofgame = input("You are out of health, you died. ")
    sys.exit()



end = input("Goodbye ")
