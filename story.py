"time and color"

import sys
from time import sleep


CRED = '\033[91m'
CEND = '\033[0m'
words = CRED + "This story is based off the choices you make, you can choose the choices by inputing the correlating number next to the choice you want. Good luck..." + CEND
for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()

sleep(1)
            
"intro"
def Entrance():
    words = '''
    You stand at the entrance of a dark and dreary mansion after your friends have challenged you to go in...
    As you and your friends enter, you clip your shoelaces on a piece of wood. 
    You bend down to tie your shoes but as you look up, your friends have vanished. 
    Shaking with fear, you enter the front door of the mansion. You enter a dark room with two doors.
    '''
    for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
            

def choosePath():
        words = '''
        Do you want to enter the left door or the right door?
        '''
       
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
         
        x = input('''#1 left door...
        #2 right door...
        ''')
        
        if (x == "1"):
            left()
        elif (x == "2"):
            right()
        else:
            words = '''
        You did not pick one of the choices.
        You have lost...
        '''
       
            for char in words:
                sleep(.03)
                sys.stdout.write(char)
                sys.stdout.flush()
            
            quit()
            
  

def left():
        words='''
        As you enter the dark and chilling room, the hairs on the back of your neck rise and you sense a faint light in the distance. 
        You get closer to see what it is but it imediately disappears...
        What do you want to do?
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        y = input('''#1 Do you go to towards the vanished light...
        #2 Leave house immediately...
        ''')
        if (y == "1"):
            light()
        elif (y == "2"):
            leave()
        else:
            words = '''
        You did not pick one of the choices.
        You have lost...
        '''
       
            for char in words:
                sleep(.03)
                sys.stdout.write(char)
                sys.stdout.flush()
            sleep(3)
            quit()


def right():
        words = '''
        You walk towards the right door and open it. 
        You see your friends arguing about something. 
        hey are arguing whether or not to split or stay together. 
        They ask you for advice, so which will you choose?
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        z = input('''#1 Split and go left
        #2 Stay Together and go right
        ''')
        if (z == "1"):
            apart()
        elif (z == "2"):
            together()
        else:
            words = '''
        You did not pick one of the choices.
        You have lost...
        '''
       
            for char in words:
                sleep(.03)
                sys.stdout.write(char)
                sys.stdout.flush()
            sleep(3)
            quit()

            
def light():
        words = '''
        You go towards the light that you saw was there a second ago. 
        Once you get there, you notice a doorknob along the dark wall and pull it. 
        You then enter a room filled with lots of treasure, illuminated by the amount of light reflected off the jewels and coins! 
        You take as much as you can but it is too much. You need the help of your friends to get all the remaining jewels but part of 
        you feels like it is enough and you should just leave before something bad happens to you...
        Which will you choose?
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        a = input('''#1 Get your friends?
        #2 Leave the house immediately...
        ''')
        if (a == "1"):
            friends()
        elif (a == "2"):
            home()
        else:
            words = '''
        You did not pick one of the choices.
        You have lost...
        '''
       
            for char in words:
                sleep(.03)
                sys.stdout.write(char)
                sys.stdout.flush()
            sleep(3)
            quit()
    
def leave():
        words = '''
        You run out of the house frantically and pause for a moment to catch your breath. 
        As you start to run again, you see a shadow behind but you don't wait to be seen. 
        You immediately hide in nearby bushes that surround the house. 
        You see a dark figure about the size of a giant, but you look closer and notice a... garden gnome? 
        You can't believe it and you gotta go tell the others, but then you have some urge to forget about it and leave. 
        Which will you choose?")
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        b = input('''#1 Leave the house
        #2 Go after your friends
        ''')
        if (b == "1"):
            exit()
        elif (b == "2"):
            tell()
        else:
            words = '''
        You did not pick one of the choices.
        You have lost...
        '''
       
            for char in words:
                sleep(.03)
                sys.stdout.write(char)
                sys.stdout.flush()
            sleep(3)
            quit()


def apart():
        words = '''
        You slowly walk into the left door but pause as you hear screams from the door your friends went through
        You keep walking not wanting to know what happened to them and find yourself wandering to the backyard of the house. 
        You look around to find many dead bodies including... your friends. You instinctively run and escape the area, driving 
        away as you see on the rear view mirror a mysterious figure standing and staring at the car as it disappears into the fog.
        YoU hAvE tHiS iRrAdIaTeD fEeLiNg To Go BaCk AnD sEe ThE hAuNtEd HoUsE aGaIn.
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        c = input('''#1 Go BaCk To ThE hOuSe
        #2 gO bAcK tO tHe HoUsE
        ''')
        if (c == "1"):
            weirdFeeling()
        elif (c == "2"):
            weirdFeeling()
        else:
            words = '''
        You did not pick one of the choices.
        You have lost...
        '''
       
            for char in words:
                sleep(.03)
                sys.stdout.write(char)
                sys.stdout.flush()
            sleep(3)
            quit()
            
        
def together():
        words = '''
        You manage to convince your friends to stick together and choose which room to go through. 
        You tell you friends to go through the left door but they would rather go through the right door, 
        you lose to the majority vote and you all go through the right door.
        As you enter the right door, you feel like something is off
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        d = input(''' #1 tell your friends that something is wrong
        #2 keep it to yourself and see what happens
        ''')
        if (d == "1"):
            speak()
        elif (d == "2"):
            quiet()
        else:
            words = '''
        You did not pick one of the choices.
        You have lost...
        '''
       
            for char in words:
                sleep(.03)
                sys.stdout.write(char)
                sys.stdout.flush()
            sleep(3)
            quit()
            

def friends():
        words = '''
        As you run back to tell your friends what you discovered, the floor starts shifting under you, and it gives way to a dark and bottomless pit.
        
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        sleep(3)
        quit()    
        

def home():
        words = '''
        You have safely exited the house, survived and brought back treasure. You live to see the light of day again.
        
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        sleep(3)
        quit()   
        
        
def exit():
        words = '''
        You have safely exited the house and survived. You live to see the light of day again.
        
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        sleep(3)
        quit()    
        

def tell():
        words = '''
        You run back to tell your friends about the freaky gnomes you found but suddenly feel nauseous and collapse. 
        The last thing you see before you pass out is the laughing face of the gnome.
        
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        sleep(3)
        quit()        
        
        
def weirdFeeling():
        words = '''
        Against your will, your arms turn the steering wheel and you drive back to the house where you encounter the shadow. 
        The shadow wraps around you and drags you back into the house. You will never see the light of day again.
        
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        sleep(3)
        quit()  
        
        
def speak():
        words = '''
        You frantically tell your friends to stop and turn back because something feels off. However it is too late. 
        The door shuts behind you and you and your friends fall prey to a horrible creature that lurks inside.
        
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        sleep(3)
        quit()    


def quiet():
        words='''You decide not to tell your friends about this weird feeling and proceed into the room. 
        However you find nothing of interest there and leave the house, relieved that you are still alive.
        
        '''
        for char in words:
            sleep(.03)
            sys.stdout.write(char)
            sys.stdout.flush()
        sleep(3)
        quit()
            
"function call"        
Entrance()
choosePath()