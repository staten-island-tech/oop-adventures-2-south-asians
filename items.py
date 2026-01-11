class amk:
    #anchor obj, map frag, keycards
    def __init__(self, name, number, total, des):
        self.name= name
        self.number = number
        self.total = total
        self.des= des

class landf:
#Lantern and food
    def __init__(self, name, des):
        self.name = name
        self.des =des

AnchorObj= amk(f"Anchor Object", "You have {self.number} anchor object(s).", "There are {self.total} left to find.", "Anchor Objects keep the world from rearranging itself.")
MapFrag = amk(f"Map Fragment", "You have {self.number} map fragemet(s).", "There are {self.total} left to find")

print(AnchorObj)