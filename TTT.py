def victorycheck(sl):
    if sl[0] == sl[3] and sl[0] == sl[6]:
        if Sl[0] == "x":
            victoryx == True
        elif sl[0] == "o":
            victoryo == True
    elif sl[1] == sl[4] and sl[1] == sl[7]:
        if Sl[1] == "x":
            victoryx == True
        elif sl[1] == "o":
            victoryo == True
    elif sl[2] == sl[5] and sl[2] == sl[8]:
        if Sl[2] == "x":
            victoryx == True
        elif sl[2] == "o":
            victoryo == True
    elif sl[0] == sl[1] and sl[0] == sl[2]:
        if Sl[0] == "x":
            victoryx == True
        elif sl[0] == "o":
            victoryo == True
    elif sl[3] == sl[4] and sl[3] == sl[5]:
        if Sl[3] == "x":
            victoryx == True
        elif sl[3] == "o":
            victoryo == True
    elif sl[6] == sl[7] and sl[6] == sl[8]:
        if Sl[6] == "x":
            victoryx == True
        elif sl[6] == "o":
            victoryo == True
    elif sl[0] == sl[4] and sl[0] == sl[8]:
        if Sl[0] == "x":
            victoryx == True
        elif sl[0] == "o":
            victoryo == True
    elif sl[2] == sl[4] and sl[2] == sl[6]:
        if Sl[2] == "x":
            victoryx == True
        elif sl[2] == "o":
            victoryo == True
    


location = 0
victoryx = False
victoryo = False
i = 0

while i != 9:
    i = i + 1
    slots = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
    field = f" {slots[0]} │ {slots[1]} │ {slots[2]} \n───────────\n {slots[3]} │ {slots[4]} │ {slots[5]} \n───────────\n {slots[6]} │ {slots[7]} │ {slots[8]} "
    while True:
        print(field)

        location = int(input("Kuhu soovite mängida?")) - 1
        
        if slots[location] == "x" or slots[location] == "o":
            print("See koht on täidetud!")
        else:
            slots[location] = "x"
            print(field)
            break
    
    victorycheck(slots)

    if victoryx == True:
        print("x võitis!")

    while True:
        print(field)

        location = int(input("Kuhu soovite mängida?"))
        
        if slots[location] == "x" or slots[location] == "o":
            print("See koht on täidetud!")
        else:
            slots[location] = "o"
            print(field)
            break
    
    victorycheck(slots)

    if victoryo == True:
        print("o võitis!")
        break

if victoryx == False and victoryo == False:
    print("x ega o ei võitnud.")