class Npc:
    def __init__(self, danger_level, speed = 5):
        self.danger_level = danger_level
        self.speed = speed



class You:
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
        



