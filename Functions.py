
def intro():
    print('''The American Revolution has started. Many are enlisting on either side, whether for the glory, for their families, for honor, or for other reasons. Now you must decide what you are fighting for 

    Choose your side
    1 - Join Revolution
    2 - Stay Loyal''')
    g = ""
    q = ""
    while g not in ["1", "2"]:
        g = input("")
        if g == "1":
            #print("You join the Revolution.")
            q = "Join_Revolution"
        if g == "2":
            print("You stay loyal.")
            q = "Stay_Loyal"
    return q


def Join_Revolution():
    print('''You have decided to enlist in the Patriots side. General Washington has taken a liking to you. Do you become his Right Hand Man or do you stay a soldier?
    
    Choose your role.
    1 - Become soldier
    2 - Become Right Hand Man''')
    g = ""
    w = ""
    while g not in ["1", "2"]:
        g = input("")
        if g == "1":
            print("You become a soldier.")
            w = "Soldier"
        if g == "2":
            print("You become Washington's Right Hand Man.")
            w = "Hand"
    return w

def Stay_Loyal():
    print('''You have decided to stay loyal to Britain as a soldier. Some of the men are eager to join the battle and some of them look worried.

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
    print('''You have arrived at your first battle. In the middle of the battle you begin to reconsider your choices. Do you remain on your side? Do you switch sides? Do you dare abandon the battle altogether?

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