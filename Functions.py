
def intro():
    print("insert introductory story later")
    print('''
    Choose your side
    1 - Join Revolution
    2 - Stay Loyal''')
    g = ""
    q = ""
    while g not in ["1", "2"]:
        g = input("")
        if g == "1":
            print("You join the Revolution.")
            q = "Join_Revolution"
        if g == "2":
            print("You stay loyal.")
            q = "Stay_Loyal"
    return q


def Join_Revolution():
    print("insert Join Revolution story later")
    print('''
    Choose your role.
    1 - Become soldier
    2 - Become Right Hand Man''')
    g = ""
    q = ""
    while g not in ["1", "2"]:
        g = input("")
        if g == "1":
            print("You become a soldier.")
            q = "Soldier"
        if g == "2":
            print("You become Washington's Right Hand Man.")
            q = "Hand"
    return q

def Stay_Loyal():
    print("insert stay loyal story later")
    print('''
Choose your role.
1 - Become soldier
2 - Become soldier
3 - Become soldier''')
    g = ""
    q = ""
    while g not in ["1", "2", "3"]:
        g = input("")
        if g == "1":
            print("You become a soldier.")
            q = "Loyal_Soldier"
        if g == "2":
            print("You become a soldier.")
            q = "Loyal_Soldier"
        if g == "3":
            print("You become a soldier.")
            q = "Loyal_Soldier"
    return q

def Soldier():
    print("insert soldier story later")
    print('''
    Choose your role.
    1 - Join battle as a Patriot
    2 - Join battle as a Loyalist''')
    g = ""
    w = ""
    while g not in ["1", "2"]:
        g = input("")
        if g == "1":
            print("You join the battle as a Patriot.")
            w = "Battle_1_Patriots"
        if g == "2":
            print("You join the battle as a Loyalist.")
            w = "Battle_1_Loyalists"
    return w