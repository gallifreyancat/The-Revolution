print("Welcome to the Revolution.")
import Functions
q = Functions.intro()
w = Functions.Soldier
if q == "Join_Revolution":
    Functions.Join_Revolution()
if q == "Stay_Loyal":
    Functions.Stay_Loyal()
if w == "Soldier":
    Functions.Soldier()
print("GAME OVER")