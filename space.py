#Game name: Space Travel
#Author: Yanqing Wu
#Start date: May 27, 2016; Friday.
#Current version: 1.0.0

#Intro: I am a completely new programmer. This is my very first game in Python.
#At the beginning, I try to put everything I learn in this program. However, that's too unrealistic.
#Now I want to keep the code simple.
#Though, I will try my best!
#----------------
#Game target: If players travel through every planet, they will win.
#Game plan: Each planet has at least 2 options; one goes to the Sun(game over), one goes to another planet.
#Game rule: Move one station(Planet) at a time.
#Stat Sources: solarsystem.nasa.gov
#----------------
#Some functions that I want to implement:
#2.  How can I run multiple functions simultaneously? // No need for now.
#3.  A clean screen function, maybe? But not that necessary.
#6.  Convert 123 into 1st2nd3rd?
#12. make the choice challenging.
#13. How about resurge in different place?? This would be a good idea.
#14. Elaborate start()
#15. Warning: while loop is really really tough to deal. # solved
#16. What if i set a list of all planets for random choice. Then those planets where players have been will be deleted from that list.
#----------------
#known bug:
#1. plyer_info,, user can type like asdf# to get through.
#----------------

from sys import exit
import msvcrt; import time; import sys; 
import re; import random 

arrive_times_Mercury = 0
arrive_times_Venus = 0 
arrive_times_Mars = 0 
arrive_times_Juipter = 0 
arrive_times_Saturn = 0 
arrive_times_Uranus = 0 
arrive_times_Neptune = 0 
arrive_times_Pluto = 0 
arrive_times_Moon = 0
arrive_times_Sun = 0 

spacetravel_days = 0 
death_times = 0
total_travels = 0
player_status = False 


def triangle(c, n):
    for i in xrange(n, 0, -1):
        time.sleep(0.2)
        print c * i

def dead(why):
    global death_times
	
    print " "
    print "Cause of death: ", why, "\nGood job!"
    print "\n\tGame Over..."   #\n\t is different from \t\n .
    print " "
	
    death_times += 1
    if death_times > 1:
        print "This is your %s times of death" % death_times
    print "\nWould you like to start over (Y/N)?"

    death_choice = raw_input("> ").upper()
	
    if "YES" in death_choice or "Y" in death_choice: 
        time.sleep(1)
        triangle (".", 5)
        resurgence()
    elif "No" in death_choice or "N" in death_choice:
        print "Fine, I'll let you go."
        exit(0) # exit the game completely. sys.exit() will do the same thing.
    else:
        print "Take your time!"
        exit(0)

def question_timeout():
    timeout = 60.0    #Player has xx secs to make a choice.
    print "\n(Tips: You have only %s secs to make a choice.)" % timeout
    global player_choice    # global it before the var, or will trigger an error.

    player_choice = None #Reset here whenever a new question arises.
    finishat = time.time() + timeout	
    player_choice = raw_input("> ")
    
    print "Your choice is: %s" % player_choice

    if player_choice == "":
        dead("My hands just shaked, somehow.")
    else:
        if time.time() > finishat:
            print "\nYour choice is...is what, which is not important anymore."
            dead("Space is dangerous. Be quick!")

def total_days():
    global spacetravel_days
    spacetravel_days += 1
    if spacetravel_days == 1:
        print "You have spent the first day on the Earth!"
    else:
        print "You have spent %s days in the Space!" % spacetravel_days
    
def start():
    print " " # add an empty line.
    print "Before we start. Just remember, type your answers right, Ok? Otherwise...(it will look funny!)"
    print " " 
    print "----------------" # print a line to separate the previous info, and start the game for real.
    print " " 

    raw_input("Please press Enter to continue...")

    print " "

    print "Greetings, traveler! A fascinating journey awaits you."
    time.sleep(1) # display delays for 1 sec
	
    if death_times == 0:
        print "So, could you tell me your name, braaaaave traveler?"

start()

def resurgence():
    
    if death_times == 1:
        time.sleep(2)
        print "Ohh, Oooo, fresh meat! Mine! Mine!"
        time.sleep(0.5)
    	print "What?? You wanna go back to that hell of world?!"
        time.sleep(0.5)
        print "Urg, gross. Go! Go! Get away from me..."
        time.sleep(1.5)
        start()
		
    elif 1 < death_times <= 3:
        print "Son, what made you here, again?"
        start()
	
    elif 3 < death_times <= 5:
        print "Mortal, this maybe the last time that I would help you."
        print "\nBe careful this time."
        start()
		
    else:
        print "You've lost your life for EVER.\nNo one can save you this time."	
        print "I am serious."
        print "\n\tGAME OVER! FOR REAL!"
        exit(0)
		

#try and except methonds seemingly only works for number input

#----------------
def player_info():
    global player_name
    global player_title
	
    player_name = None
    player_title = None
    player_name_trytimes = 4

    while True:
        player_name = raw_input("> ")
        player_name_trytimes -= 1
	
        if player_name == "" and player_name_trytimes == 0: #3 times of chance.
            dead("Enough is enough!")

        if player_name == "" and player_name_trytimes > 0:
            print "Sorry, I didn't understand that. You have %s time(s) left." %player_name_trytimes
            continue
        else:
	        break
		
    if not re.match("^[a-z]*$", player_name.lower()): #convert it to lowercase to be compared.
        dead("My friend, is that a name?")
    elif len(player_name) > 15:
        dead("Your name is too loooong")

    if death_times >= 1 or player_name == "":
        player_name = raw_input("Your name, please. Don't be naughty this time...\n> ")
        if player_name == "":
            print "\n\t......who are you? why are you here? where are you going?......"
            print "\n\t GAME OVER!"
            time.sleep(2)
            exit(0)
        if not re.match("^[a-z]*$", player_name.lower()): #convert it to lowercase to be compared.
            print "My friend, is that a name?"
            print "\n\t GAME OVER!"
            exit(0)
        elif len(player_name) > 15:
            print "Your name is too loooong"
            print "\n\t GAME OVER!"
            exit(0)			
		
    elif death_times >= 1 or player_title == "":
        player_title = raw_input("Ok, just one more chance.\n> ")
        if player_title == "":
            print "\n\t......who are you? why are you here? where are you going?......"
            print "\n\t GAME OVER!"
            time.sleep(2)
            exit(0)	
        elif player_title == "": 
            print "Blannnnk!"
            print "\n\t GAME OVER!"
            exit(0)
        elif len(player_title) > 10:
            print "Unbelievable title!!!"
            print "\n\t GAME OVER!"
            exit(0)
	
    print "Good name, I like it. Oh, by the way, should I call you Miss.? Mr.? or Prof.?"
    print "Or... something else, %s?" %player_name
    print "(tips: no need to type the dot '.')"

    player_title = raw_input("> ") # gathering player info. 
    time.sleep(1)
    if player_title == "": 
        dead("Blannnnk!")
    elif len(player_title) > 8:
        dead("Unbelievable title!!!")
    elif not re.match("^[a-z]*$", player_title.lower()):
        dead("What's that???")
    
    if death_times == 0:
        print "Very well, %s. %s, I guess you are ready.\n> Let's get started, shall we?" % (player_title, player_name)
        time.sleep(1)

player_info()
	
print " "
print "----------------" # 16 dashes to separate big branches, 8 dashes to separate small branches.
print " "

def Game_rule():
    print "Alright, listen up, earthman.\nIf you want to win this game, you have to travel through all planets."
    time.sleep(1) 
	
    global player_status
    global death_times
	
    while True:
        choice = raw_input("Go(Y/N)?\n> ").upper() #First convert to upper case to be compared next.

        if player_status and death_times > 0:
            print " "
            print "\nNo such thing. Black hole drained you out."
            print "\n\tGAME OVER"
            exit(0)
			
        elif "YES" in choice or "Y" in choice: 
            player_status = True
            Earth()
			
        elif "No" in choice or "N" in choice:
            print "Repeat:\n"
            print "\tIf. you. want. to. win. this. game, you. have. to. travel. through. ALL. planets."
			
        else:
            dead("You're too naughty.")

def Game_progress():
    global total_travels

    if arrive_times_Pluto == 1:
        total_travels += 1
    elif arrive_times_Mercury == 1:
        total_travels += 1
    elif arrive_times_Venus == 1:
        total_travels += 1
    elif arrive_times_Mars == 1:
        total_travels += 1
    elif arrive_times_Juipter == 1:
        total_travels += 1
    elif arrive_times_Saturn == 1:
        total_travels += 1
    elif arrive_times_Uranus == 1:
        total_travels += 1
    elif arrive_times_Neptune == 1:
        total_travels += 1
    elif arrive_times_Moon == 1:
        total_travels += 1
    elif arrive_times_Sun == 1:
        total_travels += 1

    if total_travels == 8:
        print "\n\tGood Job, %s. Just one(maybe two) left!" % player_name
    if total_travels == 9: # player must find a hidden place to win the game - Moon
        print "You have discovered 9 planets. Just one left. Do you want to continue(Y/N)?"
        print "Or you may want to win NOW(press Enter)?"
        finial_choice = raw_input("> ")

        if "YES" in finial_choice or "Y" in finial_choice: 
            Pluto()
        elif "No" in finial_choice or "N" in finial_choice:
            print " "
            print "\n\tCongratulations, %s!\nYou have discovered 8 planets!!" % player_name
            exit(0)
        else:
            print " "
            print "\n\tCongratulations!\nYou have discovered 8 planets!!"
            exit(0)	
    elif total_travels == 10:
        print "\n\tCongratulatoins, %s!\n You have discovered all the planet, even the Sun and the Moon!" % player_name
        exit(0)
			
def random_planet():
    all_planet = ['Mercury', 'Venus', 'Mars', 'Juipter', 'Saturn', 'Uranus', 'Neptune', 'Pluto', 'Sun']
	
    global arrive_times_Mercury; global arrive_times_Venus; global arrive_times_Mars;
    global arrive_times_Juipter; global arrive_times_Saturn; global arrive_times_Uranus; 
    global arrive_times_Neptune; global arrive_times_Pluto; global death_times
    
    if death_times <= 3:	
        if arrive_times_Mercury >= 1:
            all_planet.remove('Mercury')
        elif arrive_times_Venus >= 1:
            all_planet.remove('Venus')
        elif arrive_times_Mars >= 1:
            all_planet.remove('Mars')
        elif arrive_times_Juipter >= 1:
            all_planet.remove('Juipter')
        elif arrive_times_Saturn >= 1:
            all_planet.remove('Saturn')
        elif arrive_times_Uranus >= 1:
            all_planet.remove('Uranus')
        elif arrive_times_Neptune >= 1:
            all_planet.remove('Neptune')
        elif arrive_times_Pluto >= 1:
            all_planet.remove('Pluto')
    elif death_times > 3:
        print "Black holes welcome you"
        time.sleep(2)
        print "\n\tGame Over"
        exit(0)
		
    gift = random.choice(all_planet)
    triangle("*", 5)
    
    hf = "Have fun, %s. See you in %s!" % (player_name, gift)
    if spacetravel_days > 3:
        if gift == "Mercury":
            print hf
            Mercury()
        elif gift == "Venus":
            print hf
            Venus()
        elif gift == "Mars":
            print hf
            Mars()
        elif gift == "Juipter":
            print hf
            Juipter()
        elif gift == "Saturn":
            print hf
            Saturn()
        elif gift == "Uranus":
            print hf
            Uranus()
        elif gift == "Neptune":
            print hf
            Neptune()
        elif gift == "Pluto":
            print hf
            Pluto()
        elif gift == "Sun":
            Sun()    
    elif spacetravel_days <= 3:
        print "You're too early to be here. Send you back!~"
        time.sleep(2)
        Earth()

def Earth(): # Start point.
    print """
--------
\tEarth - Our Home

Equatorial Radius: 6.3710 x 10^3 km
Volume: 1.08321 x 10^12 km3
Mass: 5.9722 x 10^24 kg 
Density: 5.513 g/cm^3
Surface Area: 5.1006 x 10^8 km^2
Surface Gravity: 9.80665 m/s^2
Surface Temperature: -88/58 (min/max) celsius

--------""" 
    total_days()
    raw_input("Please press Enter to continue...")
    print " "
#--------
    if spacetravel_days < 1:
        print "Terran, you've been on the Earth since you born."
        time.sleep(1)
        print "I bet it quite boring to be on one planet for your life time."
        time.sleep(1)
        print "Hence, today I offer you a chance."
        time.sleep(1)
        print " "
        print "Choose one planet you like in the Solar System."
        time.sleep(1.5)
        print "Relax, I guarantee I can make you safe there."
        time.sleep(1)
        print "But...After that, you need to rely on your self, solely."
        time.sleep(1.5)
        print " "
		
    print "So, what's your choice?"
    print "1. Pluto\n2. Mercury\n3. Venus\n4. Mars\n5. Jupiter\n6. Saturn\n7. Uranus\n8. Neptune"
#--------
    choice = raw_input("> ")
    gl = "Hey, %s. Good one. Off we go!~" % player_name #good luck
    if choice == "Mercury" or choice == "2" :
        print gl
        Mercury()
    elif choice == "Venus" or choice == "3" :
        print gl
        Venus()
    elif choice == "Mars" or choice == "4" :
        print gl
        Mars()
    elif choice == "Juipter" or choice == "5" :
        print gl
        Juipter()
    elif choice == "Saturn" or choice == "6" :
        print gl
        Saturn()
    elif choice == "Uranus" or choice == "7" :
        print gl
        Uranus()
    elif choice == "Neptune" or choice == "8" :
        print gl
        Neptune()
    elif choice == "Pluto" or choice == "1" :
        print gl
        Pluto()
    elif choice == "Moon": #Hidden choice.
        print gl
        Moon()
    else:
        dead("Err, it's too dangerous to go to that place.")

	
def Mercury():
    print """
--------
\tMercury - our solar system's smallest planet

Volume: 0.056 x Earth's
Mass: 0.055 x Earth's 
Density: 0.984 x Earth
Surface Area: 0.147 x Earth
Surface Gravity: 0.38 x Earth
Surface Temperature: -173/427 celsius
88 days in Mercury equals 1 Earth year.

--------""" 
    total_days()
	
    raw_input("Please press Enter to continue...")
    print " "
#--------
    global arrive_times_Mercury
    arrive_times_Mercury += 1
    if arrive_times_Mercury == 1:
        Game_progress()	
    print "This is your No.%s time here!" % arrive_times_Mercury
	
	
    print "Welcome, it's been a long journey, isn't it?"
    print "Two options: Venus(3) or Pluto(1)?"
    print "Give me your choice."
	
    question_timeout()

    if player_choice == "Venus" or player_choice == "3":  
        Venus()
    elif "Sun" in player_choice:
        Sun()	
    else: 
        if player_choice == "Pluto" or player_choice == "1":
            Pluto()
    
	
def Venus():
    print """
--------
\tVenus - our solar system's hottest planet

Volume: 0.857 x Earth's
Mass: 0.815 x Earth's 
Density:  Comparable to the average density of the Earth.
Surface Area: 0.902 x Earth
Surface Gravity: 0.91 x Earth
Surface Temperature: 462 celsius
243 days in Venus equals 1 Earth year.

--------"""
    total_days()
	
    raw_input("Please press Enter to continue...")
    print " "
#--------
    global arrive_times_Venus
    arrive_times_Venus += 1
    if arrive_times_Venus == 1:
        Game_progress()
    print "This is your No.%s time here!" % arrive_times_Venus
	
	
    print "Welcome, it's been a long journey, isn't it?"
    print "Two options: Mercury(2) or Mars(4)?"
    print "Give me your choice."
	
    question_timeout()

    if player_choice == "Mercury" or player_choice == "2":  
        Mercury()
    elif "Sun" in player_choice:
        Sun()
    else: 
        if player_choice == "Mars" or player_choice == "4":
            Mars()
	
def Mars():
    print """
--------
\tMars - The Red Planet

Volume: 0.151 x Earth's
Mass: 0.107 x Earth's 
Density: 0.714 x Earth
Surface Area: 0.283 x Earth
Surface Gravity: 0.38 x Earth
Surface Temperature: -153 to +20 celsius
1.026 days in Mars equals 1 Earth day.

--------"""
    total_days()
	
    raw_input("Please press Enter to continue...")
    print " "
#--------
    global arrive_times_Mars
    arrive_times_Mars += 1
    if arrive_times_Mars == 1:
        Game_progress()
    print "This is your No.%s time here!" % arrive_times_Mars
	
	
    print "Welcome, it's been a long journey, isn't it?"
    print "Two options: Venus(3) or Juipter(5)?"
    print "Give me your choice."
	
    question_timeout()

    if player_choice == "Venus" or player_choice == "3":  
        Venus()
    elif "Sun" in player_choice:
        Sun()
    else: 
        if player_choice == "Juipter" or player_choice == "5":
            Juipter()
	
def Juipter():
    print """
--------
\tJuipter - King of the Planet

Volume: 1321.337 x Earth's
Mass: 317.828 x Earth's 
Density: 0.241 x Earth
Surface Area: 120.414 x Earth
Surface Gravity: 2.53 x Earth
Surface Temperature: -173/427 celsius
0.41 days in Juipter equals 1 Earth day.

--------"""
    total_days()
	
    raw_input("Please press Enter to continue...")
    print " "
#--------
    global arrive_times_Juipter
    arrive_times_Juipter += 1
    if arrive_times_Juipter == 1:
        Game_progress()
    print "This is your No.%s time here!" % arrive_times_Juipter
	
	
    print "Welcome, it's been a long journey, isn't it?"
    print "Two options: Mars(4) or Saturn(6)?"
    print "Give me your choice."
	
    question_timeout()

    if player_choice == "Mars" or player_choice == "4":  
        Mars()
    elif "Sun" in player_choice:
        Sun()
    else: 
        if player_choice == "Saturn" or player_choice == "6":
            Saturn()
	
def Saturn():
    print """
--------
\tSaturn - Jewel of Our Solar System

Volume: 763.594 x Earth's
Mass: 95.161 x Earth's 
Density: 0.125 x Earth
Surface Area: 83.543 x Earth
Surface Gravity: 1.07 x Earth
Surface Temperature: -178 celsius
0.444 days in Saturn equals 1 Earth day.

--------"""
    total_days()

    raw_input("Please press Enter to continue...")
    print " "
#--------
    global arrive_times_Saturn
    arrive_times_Saturn += 1
    if arrive_times_Saturn == 1:
        Game_progress()
    print "This is your No.%s time here!" % arrive_times_Saturn
	
	
    print "Welcome, it's been a long journey, isn't it?"
    print "Two options: Juipter(5) or Uranus(7)?"
    print "Give me your choice."
	
    question_timeout()

    if player_choice == "Juipter" or player_choice == "5":  
        Juipter()
    elif "Sun" in player_choice:
        Sun()
    else: 
        if player_choice == "Uranus" or player_choice == "7":
            Uranus()
	
def Uranus():
    print """
--------
\tUranus - The Sideways Planet

Volume: 63.085 x Earth's
Mass: 14.536 x Earth's 
Density: 0.230 x Earth
Surface Area: 15.847 x Earth
Surface Gravity: 0.91 x Earth
Surface Temperature: -216 celsius
0.72 days in Saturn equals 1 Earth day.

--------"""
    total_days()
	
    raw_input("Please press Enter to continue...")
    print " "
#--------
    global arrive_times_Uranus
    arrive_times_Uranus += 1
    if arrive_times_Uranus == 1:
        Game_progress()
    print "This is your No.%s time here!" % arrive_times_Uranus
	
	
    print "Welcome, it's been a long journey, isn't it?"
    print "Two options: Neptune(8) or Saturn(6)?"
    print "Give me your choice."
	
    question_timeout()

    if player_choice == "Neptune" or player_choice == "8":  
        Neptune()
    elif "Sun" in player_choice:
        Sun()
    else: 
        if player_choice == "Saturn" or player_choice == "6":
            Saturn()
	
def Neptune():
    print """
--------
\tNeptune - The Windiest Planet

Volume: 57.723 x Earth's
Mass: 17.148 x Earth's 
Density: 0.297 x Earth
Surface Area: 14.980 x Earth
Surface Gravity: 1.14 x Earth
Surface Temperature: -214 celsius
0.671 days in Saturn equals 1 Earth day.

--------"""
    total_days()
    
    raw_input("Please press Enter to continue...")
    print " "
#--------
    global arrive_times_Neptune
    arrive_times_Neptune += 1
    if arrive_times_Neptune == 1:
        Game_progress()
    print "This is your No.%s time here!" % arrive_times_Neptune
	
	
    print "Welcome, it's been a long journey, isn't it?"
    print "Two options: Pluto(1) or Uranus(7)?"
    print "Give me your choice."
	
    question_timeout()

    if player_choice == "Uranus" or player_choice == "7":  
        Uranus()
    elif "Sun" in player_choice:
        Sun()
    else: 
        if player_choice == "Pluto" or player_choice == "1":
            Pluto()
	
def Pluto():
    print """
--------
\tPluto - was known as the smallest planet in the solar system\n\t\tand the ninth planet from the sun.

Volume: 0.006 x Earth's
Mass: 0.002 x Earth's 
Density: 0.372 x Earth
Surface Area: 0.033 x Earth
Surface Gravity: 0.07 x Earth
Surface Temperature: -233 to -223 celsius
6.387 days in Saturn equals 1 Earth day.

--------"""
    total_days()
	
    raw_input("Please press Enter to continue...")
    print " "
#--------
    global arrive_times_Pluto
    arrive_times_Pluto += 1
    print arrive_times_Pluto
    if arrive_times_Pluto == 1:
        Game_progress()
		
    print "This is your No.%s time here!" % arrive_times_Pluto
	
	
    print "Welcome, it's been a long journey, isn't it?"
    print "Two options: Neptune(8) or Mercury(2)?"
    print "Give me your choice."
	
    question_timeout()

    if player_choice == "Neptune" or player_choice == "8":  
        Neptune()
    elif "Sun" in player_choice:
        Sun()
    else: 
        if player_choice == "Mercury" or player_choice == "2":
            Mercury()
	
def Moon():
    print """
--------
\tEarth's Moon - Our natural Satellite

Volume: 0.020 x Earth's
Mass: 0.0123 x Earth's 
Density: 0.607 x Earth
Surface Area: 0.074 x Earth
Surface Gravity: 0.166 x Earth
Surface Temperature: -233 to 123 celsius

--------"""
    total_days()
	
    raw_input("Please press Enter to continue...")
    print " "
#--------
    global arrive_times_Moon
    arrive_times_Moon += 1
    if arrive_times_Moon == 1:
        Game_progress()
		
    print "This is your No.%s time here!" % arrive_times_Moon
		
    print "Hey! How did you find this place?"
    time.sleep(1)
    print "As a reward, system will send you to a random planet(excluding places you have been)!\nLoL."
    time.sleep(1)

    random_planet()

	
def Sun():
    print """
--------
\tSun - Our Star 

Volume: 1,301,018.805 x Earth's
Mass: 333,060.042 x Earth's 
Density: 0.256 x Earth
Surface Area: 11,917.067 x Earth
Surface Gravity: 27.96 x Earth
Surface Temperature: 5500 celsius

--------"""
    total_days()

    raw_input("Please press Enter to continue...")
    print " "
#--------
    global arrive_times_Sun
    arrive_times_Sun += 1
    if arrive_times_Sun == 1:
        Game_progress()
    print "bad luck, dude."
    time.sleep(1)
    dead("Too hot")


Game_rule()

