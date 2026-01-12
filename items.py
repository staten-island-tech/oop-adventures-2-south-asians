class item:
    def __init__(self, name, des):
        self.name = name
        self.des = des

class Collectible(item):
#anchor obj, map frag, keycards
#item parnet class, collectible child clas
    def __init__(self, name, total, total_needed, des):
        super().__init__(name, des)
        self.count = 0
        self.total = total_needed

    def update(self):
        return f"You have {self.count} {self.name}(s). There are {self.total} left to find."


class Lantern(item):
    def __init__(self, name, des):
        super().__init__("Lantern", "A lamp that reveals hidden things in the In-Between.")

class Food(item):
    def __init__(self, name, heal_amnt = 15):
        super().__init__(name, "Food item.")
        self.heal_amnt = heal_amnt

def pick_up_collectible(player, item):
    item.count +=1
    item.total -=1
    player.inventory.append(item)
    print(item.update())

AnchorObj = Collectible(
    "Anchor Object",
    "Anchor Objects keep the world from rearranging itself.",
    3
)

Apple = Food("Apple", heal_amnt=10)
Crackers = Food("Crackers", heal_amnt=5)
EnergyBar = Food("Energy Bar", heal_amnt=20)
RottenSnack = Food("Snack", heal_amnt=-10)

MapFragment = Collectible(
    "Map Fragment",
    "A torn piece of the floor's layout.",
    5
)

Keycard = Collectible(
    "Keycard",
    "A security card that unlocks restricted doors.",
    5
)

print(Keycard)