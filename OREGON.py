# -*- coding: utf-8 -*-
import sys, os, subprocess, random, time
global w, ansi, g, enableRemovedFeatures
subprocess.call('', shell=True) #This makes it possible to use color graphics on Windows
enableRemovedFeatures = False

#init graphics and stuff
class ANSI:
    def __init__(self):
        self.BLACK = "\u001b[30m"
        self.RED = "\u001b[31m"
        self.GREEN = "\u001b[32m"
        self.YELLOW = "\u001b[33m"
        self.BLUE = "\u001b[34m"
        self.MAGENTA = "\u001b[35m"
        self.CYAN = "\u001b[36m"
        self.RESET = "\u001b[0m"
        self.WHITE = "\u001b[37;1m"
        self.REVERSED = "\u001b[7m"
        self.BOLD = "\u001b[1m"
        self.BACKRED = "\u001b[41m"

ansi = ANSI()
class Window:
    def __init__(self):
        try:
            from PROGDETAILS import Program
            p = Program()
        except:
            print("The game appears to be missing files (or the PROGDETAILS file is corrupted)")
            print("If the file \"version\" exists, run the file \"UpdateVersionInfo.py\" to fix this error. If not, create")
            print("a file called \"version\" (no extension) with the contents \"1 0 0\" and run the \"UpdateVersionInfo.py\" file.")
            sys.exit(0)
        self.header = ansi.WHITE + "████████████████████████████████████████████████████████████████████████████\n█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█\n█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█\n█▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█\n█▓▒░ " + ansi.CYAN + "The Oregon Trail 2018 Abridged: " + ansi.MAGENTA + "The Manga - " + ansi.RED + "The Netflix adaptation" + ansi.WHITE + " ░▒▓█\n█▓▒░                         " + ansi.GREEN + " v" + p.version + " By Johnny" + ansi.WHITE + "                          ░▒▓█\n█▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓█\n█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓█\n█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█\n████████████████████████████████████████████████████████████████████████████\n"

    def menu(self, items, choices):
        os.system("cls")
        print(self.header)
        if(choices == []):
            for item in items:
                    print(item)
            return
        try:
            menu = True
            while(menu):
                os.system("cls")
                print(self.header)
                for item in items:
                    print(item)
                try:
                    choice = int(input("\nWhat is your choice?"))
                    if(choice in choices):
                        return choice
                except:
                    errors = 0
        except:
            self.error("Error while creating list")

    def wait(self, text):
        print(text)
        os.system("pause >> nul")
        os.system("cls")
w = Window()

###################### GAME CLASS ######################

class Game:
    def __init__(self):
        self.party = []
        self.person = 0
        self.banker = 1
        self.carpenter = 2
        self.farmer = 3
        self.month = 0
        self.day = 0
        self.cash = 1600.00
        self.food = 0
        self.oxen = 0
        self.ammo = 0
        self.clothing = 0
        self.wheels = 0
        self.axles = 0
        self.tongues = 0
        self.weather = 0
        self.health = 100
        self.pricemodifier = 1
        self.sickness = 1
        random.seed(int(round(time.time() * 1000)))
        
    def error(self, err):
        print(ansi.BACKRED, err)
        print(self.cash, self.month, self.day, self.weather, self.wheels, self.axles, self.tongues, self.health)
        w.wait("Press any key...")
        sys.exit(1)
    
    def createstore(self):
        try:
            #Set up variables
            left = False
            oxencost = 0
            foodcost = 0
            clothingcost = 0
            ammocost = 0
            partscost = 0
            
            while not left:
                cost = oxencost + foodcost + clothingcost + ammocost + partscost
                choice = w.menu(["Matt's General Store", ["", "March", "April", "May", "June", "July"][self.month] + " 1st, 1848\n", "1. Oxen $" + str(oxencost), "2. Food $" + str(foodcost), "3. Clothing $" + str(clothingcost), "4. Ammunition $" + str(ammocost), "5. Spare parts $" + str(partscost), "6. Leave store\n", "Total bill: $" + str(cost)], [1,2,3,4,5,6])

                #leave store
                if(choice == 6):
                    left = True

                #oxen
                if(choice == 1):
                    if(self.person == 1):
                        print("There are 2 oxen in a yoke. I recommend at least 3 yoke. I charge $24 a yoke.")
                    else:
                        print("There are 2 oxen in a yoke. I recommend at least 3 yoke. I charge $40 a yoke.")
                    self.oxen = int(input("How many do you want? "))
                    if(self.cash - self.oxen * (40 * self.pricemodifier) < 0):
                        print("You don't have enough for that!")
                        self.oxen = 0
                    oxencost = self.oxen * (40 * self.pricemodifier)

                #food
                if(choice == 2):
                    if(self.person == 1):
                        print("I recommend you take at least 200 pounds of food for each person in your family. I see that you have five people in all. You'll need flour, sugar, bacon and coffee. My price is 12 cents a pound.")
                    else:
                        print("I recommend you take at least 200 pounds of food for each person in your family. I see that you have five people in all. You'll need flour, sugar, bacon and coffee. My price is 20 cents a pound.")
                    self.food = int(input("How many do you want? "))
                    if(self.cash - self.food * (0.2 * self.pricemodifier) < 0):
                        print("You don't have enough for that!")
                        self.food = 0
                    foodcost = self.food * (0.2 * self.pricemodifier)

                #clothing
                if(choice == 3):
                    if(self.person == 1):
                        print("You'll need warm clothing in the mountains. I recommend taking at least 2 sets of clothes per person. Each set is $6.00.")
                    else:
                        print("You'll need warm clothing in the mountains. I recommend taking at least 2 sets of clothes per person. Each set is $10.00.")
                    self.clothing = int(input("How many do you want? "))
                    if(self.cash - self.clothing * (10 * self.pricemodifier) < 0):
                        print("You don't have enough for that!")
                        self.clothing = 0
                    clothingcost = self.clothing * (10 * self.pricemodifier)

                #ammo
                if(choice == 4):
                    if(self.person == 1):
                        print("I sell ammunition in boxes of 20 bullets. Each box costs $1.20.")
                    else:
                        print("I sell ammunition in boxes of 20 bullets. Each box costs $2.00.")
                    self.ammo = int(input("How many do you want? "))
                    if(self.cash - self.ammo * (2 * self.pricemodifier) < 0):
                        print("You don't have enough for that!")
                        aelf.ammo = 0
                        
                    ammocost = self.ammo * (2 * self.pricemodifier)

                #spare parts
                if(choice == 5):
                    print("It's a good idea to have spare parts for your wagon. Here are the prices:")
                    if(self.person == 1):
                        print("   wagon wheel - $6 each\n   wagon axle - $6 each\n   wagon tongue - $6 each")
                    else:
                        print("   wagon wheel - $10 each\n   wagon axle - $10 each\n   wagon tongue - $10 each")
                    self.wheels = int(input("How many wheels do you want? "))
                    self.axles = int(input("How many axles do you want? "))
                    self.tongues = int(input("How many tongues do you want? "))
                    if(self.cash - (self.wheels + self.axles + self.tongues) * (10 * self.pricemodifier) < 0):
                        print("You don't have enough for that!")
                        self.wheels = 0
                        self.axles = 0
                        self.tongues = 0
                    partscost = (self.wheels + self.axles + self.tongues) * (10 * self.pricemodifier)

            #buy
            self.cash = self.cash - cost
        except:
            self.error("Error creating store page.")
    
    def start(self):
        if(enableRemovedFeatures):
            while(self.person == 4 or self.person == 0):
                self.person = w.menu(["Many kinds of people made the trip to Oregon.", "\nYou may:\n", "   1. Be a banker from Boston", "   2. Be a carpenter from Ohio", "   3. Be a farmer from Illinois", "   4. Find out the differences between the choices"], [1, 2, 3, 4])
                if(self.person == 4):
                    print("Banker gets extra money, carpenter gets extra spare parts and can repair parts, farmer gets 4 free oxen.")
        else:
            self.person = w.menu(["Many kinds of people made the trip to Oregon.", "\nYou may:\n", "   1. Be a banker from Boston", "   2. Be a carpenter from Ohio", "   3. Be a farmer from Illinois"], [1, 2, 3])

        #Class bonuses
        if(self.person == 1):
            self.cash = self.cash + 1000
            self.pricemodifier = 0.6 #discount
        elif(self.person == 2):
            self.axles = 3
            self.wheels = 3
            self.tongues = 3
        elif(self.person == 3):
            self.oxen = 4
            
        correct = False
        while(correct != True):
            os.system("cls")
            print(w.header)
            self.party.append(input("What is the first name of the wagon leader?"))
            for i in range(4):
                self.party.append(input("What is the first name of the next member of your party?"))
            os.system("cls")
            print(w.header)
            for name in self.party:
                print(name)
            choice = input("Are these names correct? ")
            if(choice in ['y', 'yes', 'absolutely', 'uh-huh', 'correct', 'true']):
                correct = True
            else:
                self.party = []

        if(enableRemovedFeatures):
            #Removed 1/8/2019
            self.month = w.menu(["It is 1848. Your jumping off place for Oregon is Independence, Missouri. You must decide which month to leave Independence.\n\n", "    1. March", "    2. April", "    3. May", "    4. June", "    5. July", "    6. Ask for advice"], [1,2,3,4,5,6])
            if(self.month == 6):
                os.system("cls")
                print(w.header)
                print("You attend a public meeting held for \"Folks with the California-Oregon Fever.\" You're told:\n\nIf you leave too early, there won't be any grass for your oxen to eat. If you leave too late, you may not get to Oregon before winter comes. If you leave at just the right time, there will be green grass and the weather will be cool.")
                w.wait("Press any key...")
        else:
            self.month = 1

        self.day = (self.month - 1) * 30
        w.menu(["Before leaving Independence you should buy equipment and supplies. You have $" + str(int(self.cash)) + ".00 in cash, but you don't have to spend all of it now.", "You can buy what you need at Matt's General Store."], [])
        w.wait("Press any key...")
        w.menu(["Hello, I'm Matt. So you're going to Oregon! I can fix you up with what you need:\n","       - a team of oxen to pull your wagon","       - clothing for both summer and winter","       - plenty of food for the trip","       - ammunition for your rifles","       - spare parts for your wagon"], [])
        w.wait("Press any key...")
        self.createstore()
        print("Well then, you're ready to start. Good luck! You have a long and difficult journey ahead of you.")
        if(True): #This code used to be contained in a try/except block. IDLE lacks shift+tab, so I did this (it used to crash if you died)
            self.weather = self.month * 10
            w.wait("Press any key...")
            gameLoop = True
            while(gameLoop == True):
                time.sleep(2)

                #If the player's entire party dies or runs out of food or oxen, it's game over.
                if(self.health <= 19 or self.food < 0.5 * (health / 5) or self.oxen == 0):
                    print("Game over.")
                    w.wait("Press any key...")
                    sys.exit(3)
                
                if(enableRemovedFeatures):
                    #Determine weather (Removed 1/9/2019)
                    if(self.weather > 7):
                        weather = "Hot"
                    elif(self.weather < 4):
                        weather = "Cold"
                    else:
                        weather = "Warm"

                #Determine health
                if(self.health > 70):
                    health = "Good"
                elif(self.health < 40):
                    health = "Poor"
                else:
                    health = "Fair"

                #Determine how much food to take
                if(self.food > (150 * 5)):
                    rations = "Filling"
                elif(self.food < (70* 5)):
                    rations = "Bare Bones"
                else:
                    rations = "Meager"

                #3 months and you win.
                if(self.day == 90):
                    print("You win!")
                    sys.exit(1)

                #All the ANSI codes make the text look nicer.
                print(ansi.RESET + ansi.WHITE)
                choice = w.menu([ansi.RESET + ansi.WHITE + "Weather: " + ansi.REVERSED + weather, ansi.RESET + ansi.WHITE + "Health: " + ansi.REVERSED + health, ansi.RESET + ansi.WHITE + "Rations: " + ansi.REVERSED + rations, ansi.RESET + ansi.WHITE + "\nYou may:\n", "   1. Continue on trail", "   2. Buy supplies"], [1,2])
                print(ansi.RESET + ansi.WHITE)
                
                if(choice == 2): #Pretty self-explanitory.
                    self.createstore()

                elif(choice == 1):
                    self.day = self.day + 1

                    #Remove food
                    if(rations == "Filling"):
                        self.food = self.food - 2
                    elif(rations == "Meager"):
                        self.food = self.food - 1
                    else:
                        self.food = self.food - 0.5
                        
                    #Choose if players die
                    if(random.randrange(10) >= 7):
                       try:
                           self.health = self.health - (self.health / 5)
                           ax = random.choice(self.party)
                           self.party.remove(ax)
                           print(ax + " has died.")
                           
                       except:
                            #The above code will fail if there are no more characters to kill.
                            #If so, we know it's a game over.
                            print("Game over.")
                            w.wait("Press any key...")
                            sys.exit(3)

                    #This used to be impossible, but you kinda need it in case you run out of money
                    if(random.randrange(1000) > 450 and random.randrange(60) < 10):
                        print("Some indians helped you find food.")
                        self.food = self.food + 30

                    #Rare
                    if(random.randrange(100) == 69):
                        print("A nuclear warhead struck your cart, killing everyone.")
                        print("Game over.")
                        w.wait("Press any key...")
                        sys.exit(3)

                    #Made more common
                    if(random.randrange(100) < 80):
                        print("One of your oxen has died.")
                        self.oxen = self.oxen - 1

                    #Wagon parts can now break.
                    if(random.randrange(100) == 30):
                        ax = random.randrange(3)
                        if(self.person == 2 and random.randrange(20) == 10):
                            print("You broke a part on your wagon, but you were able to repair it.")
                            break 
                        if(ax == 1):
                            self.wheels = self.wheels - 1
                            print("You broke a wheel.")
                            if(self.wheels < 0):
                                print("You have run out of wheels. Game over.")
                                sys.exit(1)
                        elif(ax == 2):
                            self.tongues = self.tongues - 1
                            print("You broke a tongue.")
                            if(self.tongues < 0):
                                print("You have run out of tongues. Game over.")
                                sys.exit(1)
                        else:
                            self.axles = self.axles - 1
                            print("You broke an axle.")
                            if(self.axles < 0):
                                print("You have run out of axles. Game over.")
                                sys.exit(1)
                                
###################### END GAME CLASS ######################

#make sure we aren't running in IDLE. Graphics don't work properly in IDLE so you end up with a mess.
if("idlelib" in sys.modules):
    print("It looks like you're running in IDLE! This breaks the graphics, please run in \nterminal instead.")
    sys.exit(0)

while(True):
    g = Game()
    choice = w.menu(["\nYou may:\n  1. Travel the trail\n  2. Run a Python script\n  3. End"], [1, 2, 3])
    if(choice == 1):
        g.start()
        
    elif(choice == 2):
        load = input("Please type the name of the python script (it should be in the same folder as the game)")
        try:
            #You can't import files if the names aren't hard-coded directly in the game,
            #unless you use a library. To get around this, we read the contents of the file
            #into exec and run it like that. Works pretty well, too. Only real issue is
            #setting up classes and defs don't always work, but I'm pretty sure that's a bug
            #in Python.
            exec(open(load).read())
            print("Success.")
            os.system("pause")
        except:
            print("There was an error during execution. Does the file exist?")
            
    elif(choice == 3):
        sys.exit(0)
