print("Welcome to the percentage change calculator by Kalanz!\nTo kill the program, type 'kill' at any time!\n")

loop = 0
def kill():
    loop +=1

while loop == 0:

    startm = (input("Start No. Here:"))
    if (startm.lower()) == "kill":
        kill()
    elif startm.isalpha() == True:
        input("Error, click enter to kill program")
        kill()
    else:
        startm = (float(startm))


    endm = (input("End No. Here:"))
    if (endm.lower()) == "kill":
            kill()
    elif endm.isalpha() == True:
        input("Error, click enter to kill program")
        kill()
    else:
        endm = (float(endm))


    chnge = ((endm - startm) / startm) * 100
    print("Percentage Change = "+(str(chnge))+"%.")
    line = 21 + (len((str(chnge))))
    linel = "-"
    for i in range(0,(line)):
        linel += "-"
    print (linel)
