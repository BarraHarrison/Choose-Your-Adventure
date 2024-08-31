# Extended Adventure Game

# Starting the game
name = input("Type your name: ")
print(f"Welcome, {name}, to this epic adventure!")
inventory = []

# Introduction and first decision
answer = input("You find yourself at the edge of a dense forest. You can go into the forest or follow a mountain path. Where do you go? (forest/mountain): ").lower()

if answer == "forest":
    # Forest path decisions
    print("You enter the forest. It's dark and the trees are tall and menacing.")
    
    answer = input("You hear a noise behind you. Do you investigate or keep moving forward? (investigate/forward): ").lower()
    
    if answer == "investigate":
        print("You turn around and see a shadowy figure. It's a wise old hermit.")
        
        answer = input("The hermit offers you a choice: a mysterious potion or an ancient map. Which do you choose? (potion/map): ").lower()
        
        if answer == "potion":
            print("You take the potion. It grants you enhanced strength.")
            inventory.append("potion")
            print(f"Your inventory now contains: {inventory}")
            
            answer = input("The hermit points you toward a hidden cave. Do you enter or keep walking? (enter/walk): ").lower()
            
            if answer == "enter":
                print("You enter the cave and encounter a large bear.")
                
                answer = input("Do you use the potion to fight the bear or try to sneak past it? (fight/sneak): ").lower()
                
                if answer == "fight":
                    if "potion" in inventory:
                        print("With your enhanced strength, you defeat the bear and find a hidden treasure. You WIN!")
                    else:
                        print("You try to fight, but without the potion's power, the bear overpowers you. You lose.")
                elif answer == "sneak":
                    print("You manage to sneak past the bear and find a hidden treasure. You WIN!")
                else:
                    print("Not a valid option. You have lost.")
            
            elif answer == "walk":
                print("You continue walking and find a clearing with a beautiful view, but nothing more. The adventure ends here.")
            else:
                print("Not a valid option. You have lost.")
        
        elif answer == "map":
            print("You take the ancient map. It shows a secret path to a magical waterfall.")
            inventory.append("map")
            print(f"Your inventory now contains: {inventory}")
            
            answer = input("Do you follow the map to the waterfall or explore the forest on your own? (waterfall/explore): ").lower()
            
            if answer == "waterfall":
                print("You follow the map and find the magical waterfall. You drink the water and gain eternal life. You WIN!")
            elif answer == "explore":
                print("You get lost in the forest and wander aimlessly until you are too tired to continue. You lose.")
            else:
                print("Not a valid option. You have lost.")
        
        else:
            print("Not a valid option. You have lost.")
    
    elif answer == "forward":
        print("You keep moving forward and stumble upon an ancient tree with a door in its trunk.")
        
        answer = input("Do you open the door or keep moving? (open/move): ").lower()
        
        if answer == "open":
            print("You open the door and find yourself in a magical library filled with ancient books.")
            
            answer = input("Do you read a book of spells or a book of history? (spells/history): ").lower()
            
            if answer == "spells":
                print("You learn powerful spells and become a master wizard. You WIN!")
            elif answer == "history":
                print("You uncover the secrets of the forest and become a legendary scholar. You WIN!")
            else:
                print("Not a valid option. You have lost.")
        
        elif answer == "move":
            print("You keep moving and find yourself at the edge of a cliff with a beautiful view of the valley below.")
            
            answer = input("Do you climb down the cliff or set up camp for the night? (climb/camp): ").lower()
            
            if answer == "climb":
                print("You carefully climb down the cliff and find a hidden village. The villagers welcome you and you live happily ever after. You WIN!")
            elif answer == "camp":
                print("You set up camp, but during the night, you are attacked by wolves. You lose.")
            else:
                print("Not a valid option. You have lost.")
        
        else:
            print("Not a valid option. You have lost.")
    
    else:
        print("Not a valid option. You have lost.")

elif answer == "mountain":
    # Mountain path decisions
    print("You take the mountain path. The air is thin and the path is steep.")
    
    answer = input("You come across a small village. Do you visit the village or keep climbing? (village/climb): ").lower()
    
    if answer == "village":
        print("You enter the village and are greeted by the villagers.")
        
        answer = input("The village elder offers you shelter or supplies for your journey. What do you choose? (shelter/supplies): ").lower()
        
        if answer == "shelter":
            print("You rest in the village and regain your strength.")
            
            answer = input("The next day, do you continue climbing or stay in the village? (climb/stay): ").lower()
            
            if answer == "climb":
                print("You continue your journey and reach the mountain summit. You find a hidden temple with untold riches. You WIN!")
            elif answer == "stay":
                print("You stay in the village and live a peaceful life. The adventure ends here.")
            else:
                print("Not a valid option. You have lost.")
        
        elif answer == "supplies":
            print("You take the supplies and continue your journey.")
            inventory.extend(["food", "rope"])
            print(f"Your inventory now contains: {inventory}")
            
            answer = input("You come across a chasm. Do you use the rope to cross or find another way? (rope/other): ").lower()
            
            if answer == "rope":
                if "rope" in inventory:
                    print("You use the rope to safely cross the chasm and continue your journey.")
                    
                    answer = input("You see a cave entrance. Do you enter the cave or continue on the path? (enter/path): ").lower()
                    
                    if answer == "enter":
                        print("You enter the cave and discover an ancient dragon hoard. You WIN!")
                    elif answer == "path":
                        print("You continue on the path and find a peaceful valley where you settle down. You WIN!")
                    else:
                        print("Not a valid option. You have lost.")
                
                else:
                    print("You don't have a rope and fall into the chasm. You lose.")
            
            elif answer == "other":
                print("You try to find another way around the chasm but get lost. You lose.")
            else:
                print("Not a valid option. You have lost.")
        
        else:
            print("Not a valid option. You have lost.")
    
    elif answer == "climb":
        print("You continue climbing the mountain and encounter a group of mountain bandits.")
        
        answer = input("Do you fight the bandits or try to negotiate with them? (fight/negotiate): ").lower()
        
        if answer == "fight":
            if "potion" in inventory:
                print("You use your enhanced strength to defeat the bandits and take their treasure. You WIN!")
            else:
                print("Without enhanced strength, the bandits overpower you. You lose.")
        
        elif answer == "negotiate":
            print("You successfully negotiate with the bandits, and they let you pass.")
            
            answer = input("Do you continue climbing or rest for the night? (climb/rest): ").lower()
            
            if answer == "climb":
                print("You reach the mountain summit and find a rare herb that grants immortality. You WIN!")
            elif answer == "rest":
                print("You rest for the night, but in the morning, you find that the bandits have stolen your supplies. You lose.")
            else:
                print("Not a valid option. You have lost.")
        
        else:
            print("Not a valid option. You have lost.")
    
    else:
        print("Not a valid option. You have lost.")

else:
    print("Not a valid option. You have lost.")

print(f"Thank you for playing, {name}! I hope you enjoyed the adventure.")
