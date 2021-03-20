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
    print (''' soldier
    1 - 
    2 - 
    ''')
    while g not in ["1", "2"]:
        g = input()
elif g == "2":
    g = ""
    print (''' hand
    1 - 
    2 - 
    ''')
    while g not in ["1", "2"]:
        g = input()
else: 
    g = ""
    print (''' loyal soldier
    1 - 
    2 - 
    ''')
    while g not in ["1", "2"]:
        g = input()

print (''' In the middle of the battle choose your side.
1 - 
2 - 
3 - 
''')
g = ""
while g not in ["1", "2", "3"]:
    g = input()

f = ""
if g == "1":
    print (''' Revolution
    1 - 
    2 - 
    ''')
    while f not in ["1", "2"]:
        f = input()
elif g == "2":
    print (''' Loyal
    1 - 
    2 - 
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
    1 - keep fighting
    2 - surrender
    3 - flee
    ''')
    while f not in ["1", "2", "3"]:
        f = input()
    if f == "1":
        print(''' die
        ''')
    elif f == "2":
        print (''' surrender back to England
        ''')
    else:
        print(''' back to England and live in shame
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
        print(''' die
        ''')
    elif f == "2":
        print (''' Tresury Secratry
        ''')
    else:
        print(''' live 
        ''')
print("GAME OVER")