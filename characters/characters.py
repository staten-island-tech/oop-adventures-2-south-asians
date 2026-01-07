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

        
class Npc:
    def __init__(self, danger_level, speed = 5):
        self.danger_level = danger_level
        self.speed = speed


class Monster(Npc):
    def __init__ (self, name,danger_level, damage):
        super().__init__(name, danger_level)
        self.damage = damage
        self.danger_level = danger_level


class You(Npc):
    def __init__(self):
            self.health = 100
            self.sanity = 100
            self.hunger = 100
            self.stamina = 100
            self.danger_level = 100
            self.inventory = []


    #fix this stop this message loop after yes or print sorry to see you go and then stop game all together
    def messages():
        while True:
            shaking = input("the ground begins to shake.. what's happening? your health is diminishing as we speak.. do something or else. continue with game [yes or no]? ")
            print(shaking)
            if input == "yes":
                print("i'm glad you chose the right choice. come on let's try to get out of here...")
            break
                        
            if input == "no":
                print("sorry to see you go.. trapped in 'in between' forever. ")
            break
    messages()


    def eat_food(self, food):
        if food in self.inventory:
            self.health += 15
            self.hunger -= 15
            self.inventory.remove(food)
            print("yum food.")
        else:
            print("you dont have food. find some.")

    def take_damage(self, amount):
        self.health -= amount
        print(f"you lost {amount} health. health: {self.health}")


        if self.health <= 0:
            print("it looks like its the end of this journey. goodbye.")


    def run(self):
        run = input("what is that approaching....uh oh.. it doesn't look too happy. run before you get eaten [yes or no]? ")
        if input == "yes":
            self.stamina -= 10
            print("you run as fast as you can. stamina:", self.stamina)

        if input == "no":
            self.health -=50
            print("your idea not to run will still diminish your health. remember if health = 0, game = OVER.")



monster = Monster("shadow", danger_level = 5, damage = 15)
player = You()
player.run()
monster.attack(player)












