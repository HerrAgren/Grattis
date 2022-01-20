import time
def grattis(namn, ålder):
    namn = namn.capitalize()
    for x in range(2):
        print("Ja må han leva,")
        time.sleep(1)
    for x in range(3):
        if x == 2:
            print("Javisst ska han leva ut i hundrade år")
            time.sleep(1)
        else:
            print("Javisst ska han leva.")
            time.sleep(1)
    for x in range(3):
        print("Hurra!")
        time.sleep(1)

    print(f"Grattis på {ålder}-årsdagen {namn}!")

namn = "Oskar"
ålder = 28

grattis(namn, ålder)
    
