#CURRENTLY WORKING ON: LINE 134, ADDING WHILE TRUE: TRY AND EXCEPTS TO EACH INPUT
ValueError = 0
#Class Input
while True:
    print("(Barbarian[1] / Druid[2] / Necromancer[3] / Rogue[4] / Sorcerer [5])")
    DClass = input("What is your class?: ")
#Barbarian
    if DClass == "1":
        print("Hello, Barbarian. First, All Damage")
        #ALL DAMAGE
        while True:
            try:
                AD = float(input("All Damage %?: "))
                break
            except:
                print("Please enter valid input; if no bonus, enter [0]")
                continue
            print("Your All Damage Bonus % is: "+str(AD))
        print("")

        #CRIT DAMAGE
        print("Now running Crit Damage Bonuses")
        while True:
            try:
                BCD = float(input("Base Crit Strike Damage %?: "))
                break
            except:
                print("Please enter valid input; if no bonus, enter [0]")
                continue
        while True:
            try:
                CCC = float(input("Crit Strike Damage % vs CC?: "))
                break
            except:
                print("Please enter valid input; if no bonus, enter [0]")
                continue
        while True:
            try:
                CDV = float(input("Crit Strike Damage % vs Vulnerable?: "))
                break
            except:
                print("Please enter valid input; if no bonus, enter [0]")
                continue
        while True:
            try:
                CDC = float(input("Crit Strike Damage % with Core Skills?: "))
                break
            except:
                print("Please enter valid input; if no bonus, enter [0]")
                continue
        TCB = BCD + CCC + CDV + CDC
        total_crit_barb = TCB/100 + 1
        print("")
        print("Your total Crit Damage Bonus is: "+str(TCB))
        print("And your total Crit Damage Multiplier will be: x"+str(total_crit_barb))
        print("")

        #ADDITIVE CALCULATORS
        print("Now running damage calculators")
        while True:
            try:
                DvBL = float(input("Damage Bonus % vs Bleeding?: "))
                break
            except:
                print("Please enter valid input; if no bonus, enter [0]")
                continue
        while True:
            try:
                DvCC = float(input("Damage Bonus % vs CC?: "))
                break
            except:
                print("Please enter valid input; if no bonus, enter [0]")
                continue
        while True:
            try:
                DvDs = float(input("Damage Bonus % vs Distant?: "))
                break
            except:
                print("Please enter valid input; if no bonus, enter [0]")
                continue
        while True:
            try:
                DvEl = float(input("Damage Bonus % vs Elites?: "))
                break
            except:
                print("Please enter valid input; if no bonus, enter [0]")
                continue
        while True:
            try:
                DvHY = float(input("Damage Bonus % vs Healthy?: "))
                break
            except:
                print("Please enter valid input; if no bonus, enter [0]")
                continue
        while True:
            try:
                DvIN = float(input("Damage Bonus % vs Injured?: "))
                break
            except:
                print("Please enter valid input; if no bonus, enter [0]")
                continue
        while True:
            try:
                DvKD = float(input("Damage Bonus % vs Knocked Down?: "))
                break
            except:
                print("Please enter valid input; if no bonus, enter [0]")
                continue
        while True:
            try:
                DvSL = float(input("Damage Bonus % vs Slowed?: "))
                break
            except:
                print("Please enter valid input; if no bonus, enter [0]")
                continue
        while True:
            try:
                DvST = float(input("Damage Bonus % vs Stunned?: "))
                break
            except:
                print("Please enter valid input; if no bonus, enter [0]")
                continue
        while True:
            try:
                DwBk = float(input("Damage Bonus % while Berserking?: "))
                break
            except:
                print("Please enter valid input; if no bonus, enter [0]")
                continue
            DwFT = float(input("Damage Bonus % while Fortified?: "))
            DwHY = float(input("Damage Bonus % while Healthy?: "))
            DwAX = float(input("Damage Bonus % with Axe Skills?: "))
            DwBC = float(input("Damage Bonus % with Basic Skills?: "))
            DwBL = float(input("Damage Bonus % with Bleeding Skills?: "))
            DwBG = float(input("Damage Bonus % with Bludgeoning Skills?: "))
            DwBR = float(input("Damage Bonus % with Brawling Skills ?: "))
            DwCR = float(input("Damage Bonus % with Core Skills ?: "))
            DwDW = float(input("Damage Bonus % with Dual Wielding Skills?: "))
            DwMC = float(input("Damage Bonus % with Mace Skills?: "))
            DwPH = float(input("Damage Bonus % with Physical Skills?: "))
            DwPA = float(input("Damage Bonus % with Polearm Skills?: "))
            DwSL = float(input("Damage Bonus % with Slashing Skills?: "))
            DwSW = float(input("Damage Bonus % with Swapped Weapons Skills?: "))
            DwSw = float(input("Damage Bonus % with Sword Skills?: "))
            DwWM = float(input("Damage Bonus % with Weapon Mastery Skills?: "))
            # Current Result Prog
            print("You're gonna have to wait a hot minute chief for me to get to the calculation parts. SOON")
            while True:
                ans = input("Would you like to re-run the test? Yes[y] or No[n]: ")
                if ans == "y":
                    break
                if ans == "n":
                    break
                else:
                    print("Why are you like this...")
            if ans == "y":
                continue
            print("Thank you for testing my personal Diablo 4 Damage Tester!")
            quit()

    #Druid
    elif DClass == "2":
        print("Please bare with me, Druid; It's still under construction... anyways...")
        #All Damage
        AD = (input("All Damage Bonus %?: "))
        #Crit Damage
        BCD = float(input("Base Crit Strike Damage %?: "))
        CCC = float(input("Crit Strike Damage % vs CC?: "))
        CDV = float(input("Crit Strike Damage % vs Vulnerable?: "))
        CDC = float(input("Crit Strike Damage % with Core Skills?: "))
        CDE = float(input("Crit Strike Damage % with Earth Skills?: "))
        CDL = float(input("Crit Strike Damage % with Lightning Skills?: "))
        CDP = float(input("Crit Strike Damage % with Poison Skills?: "))
        CDW = float(input("Crit Strike Damage % with Werewolf Skills?: "))
        #Additive % Bonuses
        DvCC = float(input("Damage Bonus % vs CC?: "))
        DvCL = float(input("Damage Bonus % vs Close?: "))
        DvDs = float(input("Damage Bonus % vs Distant?: "))
        DvEl = float(input("Damage Bonus % vs Elites?: "))
        DvHY = float(input("Damage Bonus % vs Healthy?: "))
        DvIM = float(input("Damage Bonus % vs Immobilized?: "))
        DvIN = float(input("Damage Bonus % vs Injured?: "))
        DvPS = float(input("Damage Bonus % vs Poisoned?: "))
        DvSL = float(input("Damage Bonus % vs Slowed?: "))
        DvST = float(input("Damage Bonus % vs Stunned?: "))
        DwFT = float(input("Damage Bonus % while Fortified?: "))
        DwHY = float(input("Damage Bonus % while Healthy?: "))
        DwCR = float(input("Damage Bonus % with Core Skills ?: "))
        DwHM = float(input("Damage Bonus % while Human?: "))
        DwSS = float(input("Damage Bonus % while Shapeshifted?: "))
        DwWB = float(input("Damage Bonus % while Werebear?: "))
        DwWW = float(input("Damage Bonus % while Werewolf?: "))
        DwBC = float(input("Damage Bonus % with Basic Skills?: "))
        DwCN = float(input("Damage Bonus % with Companion Skills?: "))
        DwER = float(input("Damage Bonus % with Earth Skills?: "))
        DwLT = float(input("Damage Bonus % with Lightning Skills?: "))
        DwPH = float(input("Damage Bonus % with Physical Skills?: "))
        DwPS = float(input("Damage Bonus % with Poison Skills?: "))
        DwST = float(input("Damage Bonus % with Storm Skills?: "))
        DWB = float(input("Damage Bonus % with Werebear Skills?: "))
        DWW = float(input("Damage Bonus % with Werewolf Skills?: "))
        # Current Result Prog
        print("You're gonna have to wait a hot minute chief for me to get to the calculation parts. SOON")
        while True:
            ans = input("Would you like to re-run the test? Yes[y] or No[n]: ")
            if ans == "y":
                break
            if ans == "n":
                break
            else:
                print("Why are you like this...")
        if ans == "y":
            continue
        print("Thank you for testing my personal Diablo 4 Damage Tester!")
        quit()
                
    #Necromancer
    elif DClass == "3":
        print("Please bare with me, Necro, It's still under construction... anyways...")
        #All Damage
        AD = float(input("All Damage Bonus %?: "))
        #Crit Damage
        BCD = float(input("Base Crit Strike Damage %?: "))
        CCC = float(input("Crit Strike Damage % vs CC?: "))
        CDV = float(input("Crit Strike Damage % vs Vulnerable?: "))
        CBL = float(input("Crit Strike Damage % with Blood Skills?: "))
        CBN = float(input("Crit Strike Damage % with Bone Skills?: "))
        CDC = float(input("Crit Strike Damage % with Core Skills?: "))
        CSH = float(input("Crit STrike Damage % with Shadow Skills?: "))
        #Additive % Bonus
        DvCC = float(input("Damage Bonus % vs CC?: "))
        DvCH = float(input("Damage Bonus % vs Chilled?: "))
        DvCL = float(input("Damage Bonus % vs Close?: "))
        DvDs = float(input("Damage Bonus % vs Distant?: "))
        DvFZ = float(input("Damage Bonus % vs Frozen?: "))
        DvHY = float(input("Damage Bonus % vs Healthy?: "))
        DvIN = float(input("Damage Bonus % vs Injured?: "))
        DvSL = float(input("Damage Bonus % vs Slowed?: "))
        DvST = float(input("Damage Bonus % vs Stunned?: "))
        DwHY = float(input("Damage Bonus % while Healthy?: "))
        DwFT = float(input("Damage Bonus % while Fortified?: "))
        DwBC = float(input("Damage Bonus % with Basic Skills?: "))
        DwBD = float(input("Damage Bonus % with Blood Skills?: "))
        DwBN = float(input("Damage Bonus % with Bone Skills?: "))
        DwCR = float(input("Damage Bonus % with Core Skills ?: "))
        DwDK = float(input("Damage Bonus % with Darkness Skills ?: "))
        DwMN = float(input("Damage Bonus % with Minions Skills?: "))
        DwPH = float(input("Damage Bonus % with Physical Skills?: "))
        DwSH = float(input("Damage Bonus % with Shadow Skills?: "))
        DwSD = float(input("Damage Bonus % with Shadow DoT Skills?: "))
        DfGL = float(input("Damage Bonus % from Golem Skills?: "))
        DfBO = float(input("Damage Bonus % from Blood Orb Skills?: "))
        DfMG = float(input("Damage Bonus % from Mages Skills?: "))
        DfWR = float(input("Damage Bonus % from Warriors Skills?: "))
        # Current Result Prog
        print("You're gonna have to wait a hot minute chief for me to get to the calculation parts. SOON")

        while True:
            ans = input("Would you like to re-run the test? Yes[y] or No[n]: ")
            if ans == "y":
                break
            if ans == "n":
                break
            else:
                print("Why are you like this...")
        if ans == "y":
            continue
        print("Thank you for testing my personal Diablo 4 Damage Tester!")
        quit()

    #Rogue
    elif DClass == "4":
        print("Please bare with me, Rogue; It's still under construction... anyways...")
        # All Damage
        AD = float(input("All Damage Bonus %?: "))
        # Crit Damage
        BCD = float(input("Base Crit Strike Damage %?: "))
        CCC = float(input("Crit Strike Damage % vs CC?: "))
        CDV = float(input("Crit Strike Damage % vs Vulnerable?: "))
        CCL = float(input("Crit Strike Damage % with Cold Skills?: "))
        CDC = float(input("Crit Strike Damage % with Core Skills?: "))
        CIM = float(input("Crit Strike Damage % with Imbued Skills?: "))
        CDP = float(input("Crit Strike Damage % with Poison Skills?: "))
        CSH = float(input("Crit STrike Damage % with Shadow Skills?: "))

        #Total Crit Damage
        TCR = BCD + CCC + CDV + CCL + CDC + CIM + CDP + CSH
        total_crit_rogue = (TCR)/100 + 1
        print("So far, your total Crit Strike Damage % in total is: "+str(TCR)+"%")
        #Additive % Bonus
        DvCC = float(input("Damage Bonus % vs CC?: "))
        DvCH = float(input("Damage Bonus % vs Chilled?: "))
        DvCL = float(input("Damage Bonus % vs Close?: "))
        DvDZ = float(input("Damage Bonus % vs Dazed?: "))
        DvDs = float(input("Damage Bonus % vs Distant?: "))
        DvEl = float(input("Damage Bonus % vs Elites?: "))
        DvFZ = float(input("Damage Bonus % vs Frozen?: "))
        DvHY = float(input("Damage Bonus % vs Healthy?: "))
        DvIN = float(input("Damage Bonus % vs Injured?: "))
        DvKD = float(input("Damage Bonus % vs Knocked Down?: "))
        DvPS = float(input("Damage Bonus % vs Poisoned?: "))
        DvSL = float(input("Damage Bonus % vs Slowed?: "))
        DvST = float(input("Damage Bonus % vs Stunned?: "))
        DvTR = float(input("Damage Bonus % vs Trapped?: "))
        DwHY = float(input("Damage Bonus % while Healthy?: "))
        DwBC = float(input("Damage Bonus % with Basic Skills?: "))
        DwCD = float(input("Damage Bonus % with Cold Skills?: "))
        DwCR = float(input("Damage Bonus % with Core Skills ?: "))
        DwCT = float(input("Damage Bonus % with Cutthroat Skills ?: "))
        DwDW = float(input("Damage Bonus % with Dual Wielding Skills?: "))
        DwIM = float(input("Damage Bonus % with Imbued Skills?: "))
        DwIT = float(input("Damage Bonus % with Imbuement Skills?: "))
        DwMK = float(input("Damage Bonus % with Marksman Skills?: "))
        DwPS = float(input("Damage Bonus % with Poison Skills?: "))
        DwRG = float(input("Damage Bonus % with Ranged Skills?: "))
        DwSH = float(input("Damage Bonus % with Shadow Skills?: "))
        DwTR = float(input("Damage Bonus % with Trapped Skills?: "))
        DfDG = float(input("Damage Bonus % from Dodging Skills?: "))
        # Current Result Prog
        print("You're gonna have to wait a hot minute chief for me to get to the calculation parts. SOON")

        while True:
            ans = input("Would you like to re-run the test? Yes[y] or No[n]: ")
            if ans == "y":
                break
            if ans == "n":
                break
            else:
                print("Why are you like this...")
        if ans == "y":
            continue
        print("Thank you for testing my personal Diablo 4 Damage Tester!")
        quit()

    #Sorc
    elif DClass == "5":
        print("Please bare with me, Sorcerer; It's still under construction... anyways...")
        # All Damage
        AD = float(input("All Damage Bonus %?: "))
        # Crit Damage
        BCD = float(input("Base Crit Strike Damage %?: "))
        CCC = float(input("Crit Strike Damage % vs CC?: "))
        CDV = float(input("Crit Strike Damage % vs Vulnerable?: "))
        CCL = float(input("Crit Strike Damage % with Cold Skills?: "))
        CDC = float(input("Crit Strike Damage % with Core Skills?: "))
        CFR = float(input("Crit Strike Damage % with Fire Skills?: "))
        CLT = float(input("Crit Strike Damage % with Lightning Skills?: "))
        # Additive % Bonus
        DvBn = float(input("Damage Bonus % vs Burning?: "))
        DvCC = float(input("Damage Bonus % vs CC?: "))
        DvCH = float(input("Damage Bonus % vs Chilled?: "))
        DvCL = float(input("Damage Bonus % vs Close?: "))
        DvDs = float(input("Damage Bonus % vs Distant?: "))
        DvEl = float(input("Damage Bonus % vs Elites?: "))
        DvFZ = float(input("Damage Bonus % vs Frozen?: "))
        DvHY = float(input("Damage Bonus % vs Healthy?: "))
        DvIM = float(input("Damage Bonus % vs Immobilized?: "))
        DvIN = float(input("Damage Bonus % vs Injured?: "))
        DvSL = float(input("Damage Bonus % vs Slowed?: "))
        DvST = float(input("Damage Bonus % vs Stunned?: "))
        DwHY = float(input("Damage Bonus % while Healthy?: "))
        DwBC = float(input("Damage Bonus % with Basic Skills?: "))
        DwBn = float(input("Damage Bonus % with Burning Skills ?: "))
        DwCJ = float(input("Damage Bonus % with Conjuration Skills ?: "))
        DwCD = float(input("Damage Bonus % with Cold Skills?: "))
        DwCR = float(input("Damage Bonus % with Core Skills ?: "))
        DwCE = float(input("Damage Bonus % with Crackling Energy Skills ?: "))
        DwFI = float(input("Damage Bonus % with Fire Skills?: "))
        DwFR = float(input("Damage Bonus % with Frost Skills?: "))
        DwLT = float(input("Damage Bonus % with Lightning Skills?: "))
        DwPY = float(input("Damage Bonus % with Pyromancy Skills?: "))
        DwSK = float(input("Damage Bonus % with Shock Skills?: "))
        #Current Result Prog
        print("You're gonna have to wait a hot minute chief for me to get to the calculation parts. SOON")

        while True:
            ans = input("Would you like to re-run the test? Yes[y] or No[n]: ")
            if ans == "y":
                break
            if ans == "n":
                break
            else:
              print("Why are you like this...")
        if ans == "y":
            continue
        print("Thank you for testing my personal Diablo 4 Damage Tester!")
        quit()

#else input below for invalid input for beginnning
    else:
        print("Please enter a valid inputs")

#If no value is entered or a value that can't be converted into a string, an error occurs, look into this 6/23
#REGARDING LINE ABOVE, WHEN LEARNING HTML, WE ARE ABLE TO ALLOW ONLY NUMERICAL INPUTS.
