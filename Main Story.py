print("Welcome to the Revolution.")

print('''The American Revolution has started. Many are enlisting on either side, whether for the glory, for their families, for honor, or for other reasons. Now you must decide what you are fighting for 

Choose your side
1 - Join Revolution
2 - Stay Loyal''')
g = ""

while g not in ["1", "2"]:
    g = input("")

if g == "1":
    print('''You have decided to enlist in the Patriots side. General Washington has taken a liking to you. Do you become his Right Hand Man or do you stay a soldier?
    
    Choose your role.
    1 - Become soldier
    2 - Become Right Hand Man''')
    g = ""
    while g not in ["1", "2"]:
        g = input("")
elif g == "2":
    g = ""
    print('''You have decided to stay loyal to Britain as a soldier. Some of the men are eager to join the battle and some of them look worried.

    Choose your role.
    3 - Become soldier
    4 - Become soldier
    5 - Become soldier''')
    while g not in ["3", "4", "5"]:
        g = input()  

if g == "1":
    g = ""
    print ('''You have arrived at your first battle. In the middle of the battle you begin to reconsider your choices. Do you remain on your side? Do you switch sides? Do you dare abandon the battle altogether?

    1 - Go to the Loyalist side
    2 - Remain on the Patriot side
    ''')
    while g not in ["1", "2"]:
        g = input()
elif g == "2":
    g = ""
    print ('''You have convinced General Washington to allow you into battle. In the middle of the battle you begin to reconsider your choices. Do you remain on your side? Do you switch sides and lose all trust and positions you have now? Do you dare abandon the battle altogether?

    1 - Go to the loyalists side
    2 - Remain on the Patriot side
    ''')
    while g not in ["1", "2"]:
        g = input()
else: 
    g = ""
    print ('''You have arrived at your first battle. In the middle of the battle you begin to reconsider your choices. Do you remain on your side? Do you switch sides? Do you dare abandon the battle altogether?

    1 - Go to the Patriot side
    2 - Remain on the Loyalist side
    ''')
    while g not in ["1", "2"]:
        g = input()

print ('''You have arrived at your next battle. In the middle of the battle you begin to reconsider your choices. Do you remain on your side? Do you switch sides? Do you dare abandon the battle altogether?

1 - Patriots
2 - Loyalists
3 - Flee the bttle
''')
g = ""
while g not in ["1", "2", "3"]:
    g = input()

f = ""
if g == "1":
    print (''' Revolution
    1 - Loyalists
    2 - Patriots
    ''')
    while f not in ["1", "2"]:
        f = input()
elif g == "2":
    print (''' Loyal
    1 - Loyalists
    2 - Patriots
    ''')
    while f not in ["1", "2"]:
        f = input()
else: 
    print (''' Flee
    ''')
    f = "3"

if f == "1":
    f = ""
    print (''' Yorktown Loyalists
    1 - Keep fighting
    2 - Surrender
    3 - Flee
    ''')
    while f not in ["1", "2", "3"]:
        f = input()
    if f == "1":
        print(''' Many years later, the war still goes on. Now it is one of the final battles. You don’t stop fighting. Not until the battle is won. Or so you thought. You fought longer than most, but in the end you were shot. 
        ''')
    elif f == "2":
        print ('''You fought for many years and you have hopes that the war will end soon. In a way it does. You have surrendered and are arriving in England soon.
        ''')
    else:
        print('''As one of the last battles comes to a close your courage fails you. You flee back to England on your own to live a life of shame.
        ''')
elif f == "2":
    f = ""
    print (''' Yorktown Patriots
    1 - charge cannons
    2 - charge fort
    3 - defend your line
    ''')
    while f not in ["1", "2", "3"]:
        f = input()
    if f == "1":
        print(''' For some reason you charge the cannons. You are shot down almost immediately. 
        ''')
    elif f == "2":
        print ('''You become Treasury Secretary. (Just don’t have an affair and write a book about it).
        ''')
    else:
        print(''' You hold your line and you survive the war.  
        ''')
print("GAME OVER")