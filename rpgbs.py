def recalculate():
    global pBraver
    global pBlessedLight
    global health
    global pTimeStop
    pBraver=rand(0, 50)
    pBlessedLight=rand(15, 30)
    pTimeStop=rand(0, 100)
    global attacks
    attacks={"Braver" : braver,
             "Blessed Light" : blessedLight,
             "Pain Split" : painSplit,
             "Time Stop" : timeStop
             }

def painSplit():
    global health
    global health
    painSplitter=health[targeting["self"]]+health[targeting["enemy"]]
    health[targeting["enemy"]] = painSplitter/2
    health[targeting["self"]]=health[targeting["enemy"]]
    print("%(self) endeavoured to drain %(enemy), leaving the two of you at %(health) HP each." {self: names[targeting["self"]], enemy: names[targeting["enemy"]], health: str(health["Player"])})

def braver():
    global health
    recalculate()
    health[targeting["enemy"]]-=pBraver
    print("%(self) slashed fiercely at %(enemy)! %(enemy) lost %(damage) HP.") {self: names[targeting["self"]], enemy: names[targeting["enemy"]], damage: str(pBraver)}) 

def blessedLight():
    global health
    recalculate()
    health[targeting["self"]]+=pBlessedLight
    print("%(self) called upon the gods, gaining %(heal) HP." {self: names[targeting["self"]], heal: str(pBlessedLight)})

def timeStop():
    global pTimeStop
    global stun
    global target
    recalculate()
    if rand(0,100)>pTimeStop:
        stun[targeting["enemy"]]+=1
        print("%(enemy) was stunned." {enemy:names[targeting["enemy"]]})
    else:
        print("It had no effect!")

#Importing required libraries. Sys is only needed to exit the shell cleanly and randint is required for calculation of hit chance as in pXXX variables.
import sys                                                                                              
from random import randint as rand                                                                      
while True:                                                                                             
    names = {'Player' : str(input("What's your name, hero?: ")),                                        
              'Enemy' : str(input("And who will you be duelling with?"))}                               
    startinghealth=int(input("How much health do you wish to start with? 150 is recommended."))         
    health = {'Player' : startinghealth,                                                                
              'Enemy' : startinghealth}                                                                 
    recalculate()                                                                                       
    print("Time to dool.")                                                                              
    print("Your mortal enemy approaches!")                                                              
#Ensures that both players can attack on the first turn, in case one ended the last match stunned, by resetting the stun dict to default values of 0.
    stun = {'Player' : 0,                                                                               
              'Enemy' : 0}                                                                              
    while health["Enemy"]>0 and health["Player"]>0:
        for name in names:
            print("%(chara) has %(health) HP."{chara:names[name], health:health[name]})                                                                                         
#The targeting system saves having to rewrite lines for the CPU and the player character by merely substituting names. In this case, it directs attacks at the enemy.
        targeting={"self":"Player",                                                                     
                   "enemy":"Enemy"}                                                                     
#Providing Time Stop isn't in effect on the player...
        if stun['Player']<1:                                                                            
            print("Choose your attack:")                                                                
            for attack in attacks:                                                                      
                print(attack)                                                                           
            cmd=input(">>>")                                                                            
#Compares input to all keys in attacks dict, then executes the required function.
            for attack in attacks:                                                                      
                if cmd==attack:                                                                         
                    attacks[attack]()                                                                   
#Ensures Time Stop expires after one use.
            if cmd!="Time Stop":                                                                        
                stun['Enemy']=0                                                                         
#Begins enemy turn by changing targets in dict.
        targeting={"self":"Enemy",                                                                      
                   "enemy":"Player"}                                                                    
        if stun['Enemy']<1:                                                                             
            print("%(enemy) begins to think." % {'enemy': names[targeting["enemy"]]}))
            timestopchance=rand(0, 3)
#Enemy will heal if difference between their health and the player's isn't massive.
            if health["Player"]-health["Enemy"]>30:                                                     
                cmd="Blessed Light"                                                                     
#If it is, they'll use the equivalent of Pokemon series' Endeavour attack to drag you down.
            if health["Player"]-health["Enemy"]>100:                                                    
                cmd="Pain Split"                                                                        
#They'll gamble on Time Stop most of the time.
            elif stun['Player']==0 and timestopchance<2:                                                                     
                cmd="Time Stop"                                                                         
#Otherwise, they'll use Braver.
            else:                                                                                       
                cmd="Braver"                                                                            
            if cmd!="Time Stop":
                stun['Player']=0
            print("%(enemy) readies their attack, %(attack)!" % {enemy: names["Enemy"], attack: cmd})
            for attack in attacks:
                if cmd==attack:
                    attacks[attack]()
        for character in stun:
            if stun[character]<0:
                stun[character]=0
    print("%(victim) was destroyed by %(attacker)'s %(attack) attack!" % {victim:names[targeting["enemy"]],attacker:names[targeting["self"]], attack:cmd})
    if targeting["enemy"]=="Player":
        print("%(player) blacked out..." % {player:names["Player"])
        leave=str(input("...but will they back down? [Y/N]"))
        if leave=="y" or leave=="Y":
            sys.exit()
        else:
            print(names["Player"],"safely recovered, later returning to do battle with your enemy again.")
