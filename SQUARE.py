while(True):
    try:
        var = int(input ("ENTER A NUMBER TO FIND ITS SQUARE\n"))
        print(f"THE SQUARE OF {var} IS {var**2}")
    except ValueError:
        print("ENTER AN INTEGER ONLY\n")
        continue
    break
