import json
import random
import sys

def run():
    with open("characters.json") as file:
        character_dict = json.load(file)
    hero = "Herakles"
    defense = 0
    boar_meat = 3

    def death(monster):
        print("You were killed by " + monster + ".")
        new_game = input("Play again? (y/n): ").strip().lower()
        while new_game not in ["y","n"]:
            new_game = input("Play again? (y/n): ").strip().lower()
        if new_game == "n":
            print("\nGame Over")
            sys.exit()
        else:
            run()

    def victory(monster):
        defense = 0
        print("Wow, you defeated " + monster + ".")
        if monster != "Cerberus":
            user_prompt = input("Continue? (y/n): ").strip().lower()
            while user_prompt not in ["y","n"]:
                user_prompt = input("Continue? (y/n): ").strip().lower()
            if user_prompt == "n":
                print("\nGame Over")
                sys.exit()
            elif monster == "Nemean Lion":
                equip_prompt = input("Equip the Lion Skin? (y/n): ").strip().lower()
                while equip_prompt not in ["y","n"]:
                    equip_prompt = input("Equip the Lion Skin? (y/n): ").strip().lower()
                if equip_prompt == "n":
                    print("\nYou leave the lion's skin as is and depart.")
                elif equip_prompt == "y":
                    print("Lion Skin equipped\nDefense +2")
                    defense += 2
            elif monster == "Lernaean Hydra":
                print("You severed the immortal head.")
                equip_prompt = input("Dip arrows in poison? (y/n): ").strip().lower()
                while equip_prompt not in ["y","n"]:
                    equip_prompt = input("Dip arrows in poison? (y/n): ").strip().lower()
                if equip_prompt == "n":
                    print("\nYou decide that 'hard mode' is more fun and continue with non-poison arrows.")
                elif equip_prompt == "y":
                    print("Poison Arrows equipped\nAttack Power +6")
                    character_dict[hero]["Attack"][0] = ["Poison Arrows", 13]
        else:
            print("You won the game!")
            print("Game by voolyvex")
            sys.exit()

    def attack():
        hero_attack_randomized = random.randint(0,2)
        if hero_attack_randomized == 0:
            print(hero, "attacks with", character_dict[hero]["Attack"][0][0])
            damage = character_dict[hero]["Attack"][0][1]
        elif hero_attack_randomized == 1:
            print(hero, "attacks with", character_dict[hero]["Attack"][1][0])
            damage = character_dict[hero]["Attack"][1][1]
        elif hero_attack_randomized == 2:
            print(hero, "attacks with", character_dict[hero]["Attack"][2][0])
            damage = character_dict[hero]["Attack"][2][1]
        return(damage)

    def item():
        print("Hercules has: Boar Meat")
        item_prompt = input("Use item? Boar Meat (y/n): ").strip().lower()
        if item_prompt == 'y':
            boar_meat -= 1
            print("You have", boar_meat-1, "Boar Meat(s) left.")
            if boar_meat > 0:
                return(25)
        
    def random_attack(boss):
        attack_int = random.randint(0,1)
        if attack_int == 0:
            print(boss, "attacks with", character_dict[boss]["Attack"][0][0])
            damage = character_dict[boss]["Attack"][0][1]
        else:
            print(boss, "attacks with", character_dict[boss]["Attack"][1][0])
            damage = character_dict[boss]["Attack"][1][1]
        return(damage)

    def boss_fight(boss):
        print("You are in a boss fight vs", boss)
        print()
        print(hero, "HP: ", character_dict[hero]["Health"])
        print(boss, "HP: ", character_dict[boss]["Health"])        
        print("\nEnter a command: (A)ttack or (I)tem")
        while (character_dict[boss]["Health"] > 0) and (character_dict[hero]["Health"] > 0):
            action = input("Choose an action: ").strip().lower()
            while action not in ["attack","a","item","i"]:
                action = input("Choose an action: (A)ttack or (I)tem ").strip().lower()
            if action == "attack" or action == "a":
                attack_damage = attack()
                character_dict[boss]["Health"] -= attack_damage
                print(hero, "inflicts", attack_damage, "damage")
                hero_damaged = random_attack(boss)
                character_dict[hero]["Health"] -= hero_damaged + defense
                print(boss, "inflicts", hero_damaged, "damage\n")
                if character_dict[hero]["Health"] <= 0:
                    print(hero, "HP: ", 0)
                else:
                    print(hero, "HP: ", character_dict[hero]["Health"])
                if character_dict[boss]["Health"] <= 0:
                    print(boss, "HP: ", 0)
                else:
                    print(boss, "HP: ", character_dict[boss]["Health"])

            elif action == "item" or action == "i":
                item_effect = item()
                character_dict[hero]["Health"] += item_effect
                if character_dict[hero]["Health"] >= 50:
                    character_dict[hero]["Health"] = 50
                print(hero, "is healed by", item_effect, "HP")
                hero_damaged = random_attack(boss)
                character_dict[hero]["Health"] -= hero_damaged + defense
                print(boss, "inflicts", hero_damaged, "damage\n")
                if character_dict[hero]["Health"] <= 0:
                    print(hero, "HP: ", 0)
                else:
                    print(hero, "HP: ", character_dict[hero]["Health"])
                if character_dict[boss]["Health"] <= 0:
                    print(boss, "HP: ", 0)
                else:
                    print(boss, "HP: ", character_dict[boss]["Health"])

        if (character_dict[boss]["Health"] <= 0):
            victory(boss)
        else:
            death(boss)


    def main():    
        print("\nYou are Herakles, the greatest of the Greek Heroes!\nYou have been tasked by King Eurystheus to slay the\nvicious Nemean Lion, defeat the nine-headed Lernaean\nHydra and capture Cerberus--the guard dog of the underworld.")
        user_prompt = input("Start Game (y/n): ").strip().lower()
        while user_prompt not in ["y","n"]:
            user_prompt = input("Start Game (y/n): ").strip().lower()
        if user_prompt == "n":
            print("\nGame Over")
        else:
            print("You make the long difficult journey to Nemea.\nThe Nemean lion laughs and snarls, 'Dare thee challenge?!'")
            boss_fight("Nemean Lion")
            print("\nYou travel to the outskirts of Lerna and find the adorable\nlair of the Laernean Hydra.\nOne of the nine heads hisses,\n'Dieeee.'")
            boss_fight("Lernaean Hydra")
            print("\nFinally, the entrance to Hell. Oh wow look it's Cerberus. Nice doggy.\nNiiiiice doggy!'\n")
            boss_fight("Cerberus")

    main()

run()