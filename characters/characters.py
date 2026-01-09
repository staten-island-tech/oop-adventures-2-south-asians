""" class You():
    def __init__(self, health = 100, sanity = 100, hunger = 100, stamina = 100):
        self.health = health
        self.sanity = sanity
        self.hunger = hunger
        self.stamina = stamina
        self.inventory = []

    def messages():
        while True:
            shaking = input("the ground begins to shake.. what's happening? your health is diminishing as we speak.. do something or else. continue with game [yes or no]? ")
            print(shaking)
            if input == "yes":
                print("i'm glad you chose the right descison. come on let's try to get out of here...")
                break
                        
            if input == "no":
                print("sorry to see you go.. trapped in 'in between' forever. ")
                break
                    
    messages()

class Npc(You):
    def __init__(self, danger_level, speed = 5):
        self.danger_level = danger_level
        self.speed = speed

    def monster(self):
        run = input("what is that approaching....uh oh.. it doesn't look too happy. run before you get eaten [yes or no]? ")
        if input == "yes":
            self.health -=10 """



""" class Monster(Npc):
    def __init__ (self, name,danger_level, damage):
        super().__init__(name, danger_level)
        self.damage = damage
        self.danger_level = danger_level """

import random
        
class Npc:
    def __init__(self, danger_level, speed = 5):
        self.danger_level = danger_level
        self.speed = speed


class You(Npc):
    def __init__(self):
        self.health = 100
        self.sanity = 100
        self.hunger = 0
        self.stamina = 100
        self.danger_level = 100
        self.inventory = []

    def messages(self):
            shaking = input("You step out of the elevator without thinking, expecting the usual hallway. The doors close behind you before you even turn around. When you do, the wall is smooth. No call button. No seam. No elevator.The display above the empty space reads: 5½.The hallway looks almost familiar, but wrong. The lights hum unevenly. The air feels heavy. Every apartment door is cracked open just enough to suggest someone might be watching from inside.A bright red Post-It note lies on the floor.'Don’t wander. It notices movement.'A few steps ahead, a folded sheet of paper lies on the ground. The handwriting is rushed.“5½ is part of the In‑Between. It does not let people wander forever. If you don’t escape soon, you will become one of the residents—the silent figures behind the cracked doors. They are not just trapped souls. They help the thing that controls this place.'You look up. The hallway feels like it’s holding its breath. Far down the corridor, a faint warm light glows. You walk toward it. A small lamp sits on the floor. Inside its base is a note:'This lamp reveals what the In-Between hides. It will help you find missing map fragments, see in the dark, avoid unstable areas, and activate anchor objects. 'Taped to the handle is a Level 1 Keycard. As you lift the lamp, a metal plate on the wall glows faintly. Engraved text reads:“Anchor Object—activates when illuminated. Stabilizes nearby space.”You shine the lamp on it. The hallway stops flickering. You now understand: Anchor Objects keep the world from rearranging itself. You take a few steps forward. Then you hear it. A sound behind you. Slow. Dragging. Deliberate. The lamp flickers once, as if reacting to something you can’t see. The footsteps grow louder. Do you run or hide? [pick run or hide]")
            print(shaking)
            if input == "run":
                self.stamina -= 10
            print("You bolt down the hallway, the lamp swinging wildly in your hand, throwing jagged shadows across the walls. Your footsteps echo too loudly. The air feels thick, resisting every movement. Behind you, the dragging footsteps quicken. Not running—but gaining. You push harder, lungs burning. The lamp flickers violently. For a split second, the shadows stretch unnaturally long, as if something tall is reaching toward you. You don’t look back. You round a corner too fast and nearly slip. Your breath is sharp and ragged. You lose 5 stamina. Finally, you stumble into a small alcove and nearly crash into a broken vending machine. The glass is cracked, smeared with something dark. The machine’s interior light flickers weakly. A note lies on the floor: 'Food is free here. But time still matters. Check expiration dates. Rotten things hurt more than they help.'Behind the machine, you find a Level 2 Keycard. The footsteps have stopped. But the silence feels wrong. stamina:", self.stamina)

            if input == "hide":
                self.health -=50
            print("Your idea not to run will still diminish your health. Remember if health = 0, game = OVER.")

    def food(self):
        print("Finally, you stumble into a small alcove and nearly crash into a broken vending machine. The glass is cracked, smeared with something dark. The machine’s interior light flickers weakly. A note lies on the floor: 'Food is free here. But time still matters. Check expiration dates. Rotten things hurt more than they help.' Behind the machine, you find a Level 2 Keycard. The footsteps have stopped. But the silence feels wrong. Pick up the food? [yes or no]")
        if input == "yes":
            print("Check expiration dates? [yes or no]")
              
           #do expiration dates later 

        if input == "no":
            self.hunger +=15
            self.health -=15
            print(f"Health: {self.health}", "Hunger: {self.hunger}")


    def eat_food(self, food):
        if food in self.inventory:
            self.health += 15
            self.hunger -= 15
            self.inventory.remove(food)
            print("Yum food.")
        else:
            print("You dont have food. Find some.")


    def take_damage(self, amount):
        self.health -= amount
        print(f"You lost {amount} health. Health: {self.health}")
        if self.health <= 0:
            print("It looks like its the end of this journey. Goodbye.")

player = You(123)



