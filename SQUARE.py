while(True):
    try:
        var1 = int(input ("ENTER A NUMBER TO FIND ITS SQUARE\n"))
        print("THE SQUARE OF", var1,"IS", int(var1 * var1))
    except ValueError:
        print("ENTER AN INTEGER ONLY")
        continue
    break
