# count = 0 #global variable

# def incrementCount():
#     global count = 0
#     count += 1
#     return ocount

# def increment():
#     global count
#     count += 4
#     return count

# class Counter():
#     def __init__(self):
#         self.count = 0

#     def increment(self):
#         self.count += 1
#         return self.count

# count1 = Counter()

# print("count1: ", count1.increment())



# print("instance variable for the count 1: ", count1.count)

# count2 = Counter()
# print("count2:", count2.increment")

# 

# from welcomeFunction import welcomeMessage
# from boss import bossImage
# from sword import swordImage
# from gameOver import gameOver, snakeHandler, dice, rubberDuck, victory
# import time
# class Characters:
#     def __init__(self, name, hp, defense, attack):
#         self.name = name
#         self.hp = hp
#         self.defense = defense
#         self.attack = attack
#         # self.characterClass = “Hero”
# class Hero(Characters):
#     # def __init__(self, coinPurse):
#     coinPurse = 0
#     # self.coin = coin
#     def coinTransaction(self):
#         self.coinPurse += 3
#         print(
#             f”“”\nThree rubber duckies have been added to your backpack. You now have {character.coinPurse} rubber duckies.“”")
#     def minionDamage(self):
#         self.hp -= minion.attack
#     def bossDamage(self):
#         self.hp -= boss.attack
# class Villain(Characters):
#     def takeDamage(self):
#         self.hp -= character.attack
# # Heros
# # Villans
# minion = Villain(“Brainwashed Dev”, 50, 25, 15)
# boss = Villain(“Python”, 200, 75, 65)
# # print(heroHuman.name)
# # print(villanBoss.name)
# def selectChar():
#     # charName = input(“What is your name?“)
#     character = “”
#     while character == “”:
#         choice = input(“”"Please select your class:
#         1. Human - Your average everyday human.
#         2. Orc - Higher health but lower attack.
#         3. Elf - Lower health but higher attack.
#         “”")
#         if (choice == “1”):
#             character = Hero(“Human”, 100, 50, 40)
#         elif (choice == “2”):
#             character = Hero(“Orc”, 110, 50, 35)
#         elif (choice == “3”):
#             character = Hero(“Elf”, 90, 50, 45)
#         else:
#             print(“Please follow my rules and enter a valid choice.“)
#     return character
# # combat
# # def characterAttacks(character, minion):
# #     print(f”{character.name} attacks {minion.name}“)
# #     print(f”{minion.name} takes damage”)
# #     minion.takeDamage()
# #     print(f”{minion.name} gets wrecked.“)
# #     print(f”{minion.name}‘s remaining health is {minion.hp}“)
# #     character.coinTransaction()
# def minionFight(minion, character):
#     print(“\nWalking through the village...“)
#     print(“...“)
#     time.sleep(1)
#     snakeHandler()
#     print(
#         f”You’ve run into a brainwashed Dev and you have {character.hp} health.“)
#     action = ‘’
#     while action != “2” and character.hp > 0 and minion.hp > 0:
#         action = input(“”"
#         What would you like to do?
#         1. Fight Developer
#         2. Run Away
#         “”")
#         if (action == “1"):
#             dice()
#             time.sleep(1)
#             print(f”{minion.name} attacks {character.name}“)
#             print(f”{character.name} takes {minion.attack} damage”)
#             character.minionDamage()
#             print(f”{character.name}’s remaining health is {character.hp}“)
#             print(f”{minion.name} takes {character.attack} damage”)
#             minion.takeDamage()
#             print(f”{minion.name}‘s remaining health is {minion.hp}\n”)
#             if minion.hp <= 0:
#                 print(
#                     f”\nSuccess!!! {minion.name} is slain.“)
#                 character.coinTransaction()
#                 print(f”You have {character.coinPurse} total rubber duckies.“)
#                 rubberDuck()
#                 minion.hp = 0
#                 minion.hp += 50
#                 break
#             elif character.hp <= 0:
#                 gameOver()
#                 print(“You have been slain hero! Please try again.“)
#             elif minion.hp < 10:
#                 print(f”{minion.name} is getting weak.“)
#             else:
#                 print(f”{minion.name} is still alive. Keep attacking!!!“)
#         elif (action == “2”):
#             continue
#         else:
#             print(“Please select a valid option.“)
#     return action
# def bossFight(boss, character):
#     print(“Walking to the Town Hall you sense danger ahead...“)
#     print(“...“)
#     time.sleep(2)
#     print(“You’ve come this far hero! Dont be scared!“)
#     time.sleep(1)
#     bossImage()
#     action = ‘’
#     while action != “2” and character.hp > 0 and boss.hp > 0:
#         action = input(“”"
#         What would you like to do?
#         1. Fight Python
#         2. Run Away
#         “”")
#         if action == “1":
#             print(f”{boss.name} attacks {character.name}“)
#             print(f”{character.name} takes {boss.attack} damage”)
#             character.bossDamage()
#             # print(f”{boss.name} is unphased.“)
#             print(f”{character.name}’s remaining health is {character.hp}“)
#             print(f”{boss.name} takes {character.attack} damage”)
#             boss.takeDamage()
#             print(f”{boss.name}’s remaining health is {boss.hp}“)
#             if boss.hp <= 0:
#                 victory()
#                 print(
#                     f”Victory! {boss.name} is slain and dies in a spectacular explosion.“)
#             elif character.hp <= 0:
#                 print(“You have been slain hero!“)
#                 gameOver()
#             elif boss.hp < 10:
#                 print(f”{boss.name} is getting weak.“)
#             else:
#                 print(f”{boss.name} is still putting up a fight.“)
#         elif (action == “2”):
#             print(
#                 “You are terrified at the site of the almighty Python. You cower away to safety.“)
#             continue
#         else:
#             print(“Please select a valid option.“)
#     return action
# def barracks():
#     rubberDuck()
#     purchase = “”
#     while purchase != “3":
#         print(f”You have {character.coinPurse} total rubber duckies.“)
#         purchase = input(“”"
#             Welcome traveler! What would you like to purchase? Please select an option:
#             1. Upgraded sword (+50 attack) - Costs 5 rubber duckies
#             2. Coffee (+25 health points) - Costs 1 rubber ducky
#             3. Return to battle!
#         “”")
#         if purchase == “1" and character.coinPurse >= 5:
#             character.attack += 50
#             character.coinPurse -= 5
#             swordImage()
#             print(
#                 f”You now have {character.attack} attack and {character.coinPurse} rubber duckies! Pleasure doing business with you.“)
#         elif purchase == “2" and character.coinPurse >= 1:
#             character.hp += 25
#             character.coinPurse -= 1
#             print(
#                 f”You now have {character.hp} health points and {character.coinPurse} rubber duckies! Pleasure doing business with you.“)
#         elif purchase == “3”:
#             continue
#         else:
#             print(
#                 “You don’t have enough rubber duckies yet! Fight some more developers and come back soon.“)
#     return purchase
# def mainMenu():
#     selection = input(“”"
#         What would you like to do next? Please select an option:
#         1. Explore Village
#         2. Go to Town Hall - (WARNING! DANGER!)
#         3. Go to Barracks - Purchase items
#         4. Quit
#     “”")
#     return selection
# welcomeMessage()
# character = selectChar()
# print(f”“”
#         Your class is: {character.name} \n
#         Health: {character.hp} \n
#         Defense: {character.defense} \n
#         Attack: {character.attack} \n
#     “”")
# adventureOption = “”
# while adventureOption != “4" and boss.hp > 0 and character.hp > 0:
#     adventureOption = mainMenu()
#     if (adventureOption == “1”):
#         minionFight(minion, character)
#     elif (adventureOption == “2"):
#         bossFight(boss, character)
#     elif (adventureOption == “3”):
#         adventureOption = barracks()
#     else:
#         pass

while goblin.alive() and hero.alive: #and zombie.alive:
        # hero.health -= goblin.power
        print(“You have {} health and {} power.“.format(hero.health, hero.power))
        print(“The goblin has {} health and {} power.“.format(goblin.health, goblin.power))
        #print(“The zombie has {} health and {} power.“.format(zombie.health, zombie.power))
        # goblin.health -= hero.power
        print()
        print(“What do you want to do?“)
        print(“1. fight goblin”)
        #print(“2. fight zombie”)
        print(“2. do nothing”)
        print(“3. flee”)
        print(“> “, end=' ’)
        raw_input = input()
        if raw_input == “1”:
            hero.attack(goblin)
            if goblin.alive():
                print(“You did {} damage to the Goblin.“.format(hero.power))
                hero.health -= goblin.power
                print(“Goblin did {} damage to you.“.format(goblin.power))
                # goblin.print_status()
            else:
                print(“You did {} damage to the Goblin.“.format(hero.power))
                print(’The Goblin is dead.’)
            while goblin.health <= 0 and hero.health > 0:
                print(“Zombie wants to fight. Do you accept challenge? “)
                print(“1. fight zombie”)
                print(“2. flee from zombie”)
                raw_input = input()
                if raw_input == “1":
                    hero.attack(zombie)
                    print(f”You did {hero.power} damage to the Zombie.“)
                    hero.health -= zombie.power
                    print(f”Zombie did {zombie.power} damage to you.“)
                    while zombie.health < 1000:
                        print(“You have {} health and {} power.“.format(hero.health, hero.power))
                        print(“The zombie has {} health and {} power.“.format(zombie.health, zombie.power))
                        print(“Do you wish to continue?“)
                        raw_input = input()
                        if raw_input == “1":
                            hero.attack(zombie)
                            print(f”You did {hero.power} damage to the Zombie.“)
                            hero.health -= zombie.power
                            print(f”Zombie did {zombie.power} damage to you.“)
                            if hero.health <= 0:
                                print(“You are dead. GAME OVER!!!“)
                                break
                        elif raw_input == “2”:
                            print(“Bye!!!“)
                            break
                        else:
                            if zombie.attack(hero):
                                hero.health <= 0
                                print(“You are dead.\nGAME OVER!!!!“)
                                break
                else:
                    if raw_input == “2”:
                        print(“Bye!!! \nGAME OVER!!!!“)
                        break
                    else:
                        print(“Invalid input {}“.format(raw_input))
            else:
                pass
        elif raw_input == “2”:
            goblin.attack(hero)
            print(“Goblin did {} damage to you.“.format(goblin.power))
            if hero.alive(hero.health):
                print(“Dont just stand there, fight!!!“)
            else:
                print(“You are dead. GAME OVER!!!“)
                break
        elif raw_input >= “3”:
            print(“Goodbye. Thanks for playing”)
            break
        else:
            print(“Invalid input {}“.format(raw_input))
            if goblin.health > 0:
                print(“He’s still alive.“.format(goblin.power))
            else:
                goblin.attack(hero)
            if hero.alive():
                hero.health
                pass
            else:
                print(“You are dead.“)