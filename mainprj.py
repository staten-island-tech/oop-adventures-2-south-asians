""" from characters import You

player=You() """

def intro():
    print("You live on the sixth floor of your apartment building, and the elevator has always paused strangely between floors five and six. ", "\nOne night, halfway through that familiar slowdown, you press the button for five again just to see what happens. The elevator shudders, the lights flicker, and the doors slide open to a floor that shouldn’t exist.")
    print("")
    print("You step out of the elevator without thinking, expecting the usual hallway. The doors close behind you before you even turn around.", "\nWhen you do, the wall is smooth. No call button. No seam. No elevator. The display above the empty space reads: 5½.", "\nThe hallway looks almost familiar, but wrong. The lights hum unevenly. The air feels heavy. Every apartment door is cracked open just enough to suggest someone might be watching from inside.")
    print(" ")
    print("A bright red Post-It note lies on the floor.", "\n“Don’t wander. It notices movement.”")
    print(" ")
    print("A few steps ahead, a folded sheet of paper lies on the ground. The handwriting is rushed.", "\nIt reads: “5½ is part of the In‑Between. It does not let people wander forever. If you don’t escape soon, you will become one of the residents—the silent figures behind the cracked doors. They are not just trapped souls. They aid the creatire that controls this place.”")
    print("")
    print("You look up. The hallway feels like it’s holding its breath.", "\nFar down the corridor, a faint warm light glows.")
    f = input("Walk toward the light? [yes/no]").strip().lower()
    print(input)
    if input == "yes":
        print("You walk toward the dim yet warm light, the only thing illuminating the shadow of the corridor")
intro()

