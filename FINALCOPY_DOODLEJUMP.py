#“I hereby certify that this program is solely the result of my own work and is in compliance with the Academic Integrity policy of the course syllabus.” 

import Draw
import random 

CANVAS_HEIGHT = 600

Draw.setCanvasSize(550,600)
Draw.setBackground(Draw.WHITE)

#------------------BACKGROUND GRAPHPAPER ---------------------------------------

def background(CANVAS_HEIGHT):
    Draw.setBackground(Draw.WHITE)
    for i in range(0,CANVAS_HEIGHT,10):
        Draw.setColor(Draw.LIGHT_GRAY) 
        Draw.line(i,0,i,600)
        Draw.line(0,i,600,i)
            #Custom colors of the doodle jump guy
topBody = Draw.color(175,190,36)
bottomBody = Draw.color(62,144,40)

#-----------------------------------OPENING SCREEN------------------------------

def _jump(y,x,power):          #function for making the character jump up and down on the start screen 
    if power>0:                #if character has power, move the character up                                             
        y-=8
        power-=1
        return y, power 
    else:                      #if the character does not have power, he goes down until he reaches the bottom of the screen                                          
        y+=8
        if y>=500:
            power=25     
        return y, power

def startGame(topBody):        #opening screen- start game, jumping character, instructions 
    p=25                       #coordinates for the character 
    x = 100
    y = 500    
    while True:
        y,p= _jump(y,x,p) 
        if Draw.hasNextKeyTyped():             #controling the left and right movement of the character 
            newKey = Draw.nextKeyTyped()
            if newKey == "Right":              #if user presses right key, move the character to the right 
                x+=20
                if x>550:
                    x= -45
            elif newKey == "Left":             #if user presses left key, move the character to the left  
                x-= 20   
                if x<0:
                    x=550
        Draw.clear() 
        background(CANVAS_HEIGHT)
        Draw.setColor(Draw.RED)
        Draw.setFontSize(20)
        Draw.setFontFamily('Ravie')
        Draw.string("DOODLEJUMP",160,50)
        Draw.setColor(Draw.BLACK)
        Draw.setFontFamily('Courier')
        Draw.string("CLICK START TO BEGIN",115,160)
        Draw.setColor(Draw.WHITE)           
        Draw.filledRect(170,200,198,70)      #rectangle surrounding "Start"
        Draw.filledRect(190,330,330,210)     #rectangle surrounding instructions 
        Draw.setColor(topBody)
        Draw.setFontSize(50)
        Draw.string("START", 170,200)
        Draw.setFontSize(20)
        Draw.setColor(Draw.BLACK)
        Draw.string("How To Play:",200,300)                  
        Draw.setFontSize(10)
        Draw.string("~Use the arrow keys to move the",200,340)
        Draw.string("character left or right.",200,355)
        Draw.string("~Press up arrow to shoot.",200,380)
        Draw.string("~Land on platforms to go higher",200,405)
        Draw.string("and avoid hitting the monsters!", 200,420)
        Draw.string("~Land directly on the monsters or shoot", 200,445)
        Draw.string("them to kill them",200,460)
        Draw.string("~Hold down arrows to move faster",200,485)
        Draw.string("~Tip:if you think you're stuck, go off",200,510)
        Draw.string("one side to appear on the other side!",200,525)
        doodleMan(x, y)              #Draw the character jumping up and down 
        Draw.show()    
        if Draw.mousePressed():                 #Invoke the game if user clicks start 
            if (Draw.mouseX()>=170 and Draw.mouseX()<=368) and (Draw.mouseY()>=200 and Draw.mouseY()<=300):  #if they press START:
                Draw.clear()
                flushKeys()
                main() 
#--------------------CHARACTER-------------------------------------------------

def topMan(x,y,wide,high):          #Top of the character
    Draw.setColor(topBody)
    Draw.filledRect(x,y+25,wide,high)
    Draw.setColor(topBody)
    Draw.filledOval(x,y+5,wide,high)    
def bottomMan(x,y,wide,high):       #Bottom of the character
    Draw.setColor(bottomBody)
    Draw.filledRect(x,y,wide,high)
    Draw.setColor(Draw.BLACK)
    Draw.rect(x,y,wide,high/2)
    Draw.rect(x,y+high/2,wide,high/2)
def leg(x,y,wide,high):              #Legs 
    Draw.setColor(Draw.BLACK)
    Draw.filledRect(x,y,wide,high)
    Draw.filledRect(x+13,y,wide,high)
    Draw.filledRect(x+26,y,wide,high)
def feet(x,y,wide,high):             #feet
    Draw.filledRect(x,y,wide,high)
    Draw.filledRect(x+13,y,wide,high)
    Draw.filledRect(x+26,y,wide,high) 
def eyes(x,y,wide,high):             #eyes
    Draw.filledOval(x,y,wide,high)
    Draw.filledOval(x+7,y+1,wide,high) 
def nose(x,y,wide,high):             #nose          
    Draw.setColor(topBody)  
    Draw.filledRect(x,y,wide,high)
    Draw.setColor(Draw.BLACK)
    Draw.oval(x+15,y,wide-15,high)
        
#---------------COMPLETE DRAWING OF CHARACTER----------------------------------
    
def doodleMan(xLocation,yLocation):
    topMan(xLocation,yLocation,45,40)
    bottomMan(xLocation,yLocation+50,45,25) 
    leg(xLocation+6,yLocation+75,3,15)
    feet(xLocation+9,yLocation+86,3,4)
    eyes(xLocation+29,yLocation+17,3,4)
    nose(xLocation+40,yLocation+28,20,10)


#-------------------PLATFORMS: list & draw them---------------------------------

def makePlatforms(CANVAS_HEIGHT):          #Create a list of x and y coordinates to use as platforms 
    platforms=[]
    for y in range(CANVAS_HEIGHT,-100000,-60):
            x=random.randint(0,500)
            yList=random.randint(y-75,y)
            newList=[x,yList]
            platforms.append(newList)
    startingPlat=[300,586]                #need to make sure there's a platform Where the character starts 
    platforms.append(startingPlat)
    return platforms    

               
def drawPlatforms(platforms,yOrigin,CANVAS_HEIGHT):    
    for n in platforms:
        canvasY=n[1]-yOrigin
        if canvasY>=0 and canvasY<CANVAS_HEIGHT:      #Screen window needs to move as character gets higher so he doesnt fall off the screen
            Draw.filledRect(n[0],canvasY,75,6)        #only Draw the platforms if they are within the screen window 
    return yOrigin

#-------------MONSTERS: list & draw them----------------------------------------

def monsters(platforms):                            #make a monster list using random x and y coordinates from the platform list 
    monsterList=[]
    for i in range(150):
        monsterList+=[random.choice(platforms)]
    for n in monsterList:
        if n[1]>=200:                               #if the monster is too close to the bottom of the screen when the game starts, take it away 
            monsterList.remove(n)   
    return monsterList
     

def drawMonsters(monsterList,yLocation,xLocation,yOrigin):
    for n in monsterList:
        canvasY=n[1]-yOrigin                        #taking into account the moving screen window: 
        if canvasY>=0 and canvasY<600:
            Draw.setColor(Draw.BLUE)                #Body of monster 
            Draw.filledOval(n[0],canvasY-50,50,37)  
            Draw.filledRect(n[0]+7,canvasY-20,5,20)    #Legs of monster
            Draw.filledRect(n[0]+40,canvasY-20,5,20) 
            Draw.setColor(Draw.BLACK)                      #Eyes of monster 
            Draw.filledOval(n[0]+15,canvasY-40,4,4)
            Draw.filledOval(n[0]+30,canvasY-40,4,4)
            Draw.oval(n[0]+14,canvasY-25,21,2)         #mouth of monster 

#-----------------SHOOT BULLETS-------------------------------------------------   

def shootMonsters(xLocation,canon):   
    Draw.setColor(Draw.BLACK)
    Draw.filledOval(xLocation+22,canon,10,10)    #Draw the bullets from the top middle of the characters head. (xLocation+22==the middle of the character)
    return xLocation+22
def updateShot(shotX,canon,monsterList,status,yOrigin):
    canon-=10                                  #draw the bullets higher each time through the loop 
    if canon>=yOrigin:
        for m in monsterList:                      #bullet keep traveling up, until it hits a monster. 
            if ((shotX>=m[0] and shotX<=m[0]+50)or(shotX+32>=m[0] and shotX+32<=m[0]+50)) and (canon>=(m[1]-50)-yOrigin and canon<=(m[1])-yOrigin):
                status=False
                monsterList.remove(m)               #if bullet hits monster, the monster is removed from the list of monsters. 
    elif canon<yOrigin:                                              
        status=False 
    return canon, status


#-------------FUNCTIONS FOR LANDING ON PLATFORMS & HITTING A MONSTER------------       

def hitPlatform(xLocation,platforms,yLocation):
    Feet=yLocation+90                              #the bottom of the character
    leftFoot=xLocation+7                           #where the left leg of the character is 
    rightFoot=xLocation+34                         #where the right foot of the character ends 
    
    for n in platforms:                            #keeps track of whether his feet touches any of the platforms 
        if (Feet==n[1] or (Feet>=n[1]-2 and Feet<=n[1]+8)) and ((leftFoot>= n[0]  and leftFoot<=n[0]+75) or (rightFoot>=n[0] and rightFoot<=n[0]+75)):
            return True
    return False 

def hitMonster(monsterList,xLocation,yLocation):
    feet=yLocation+90                              #bottom of the character 
    leftSide=xLocation                             #the left side of the whole character 
    rightSide=xLocation+45                         #right edge of the character IGNORING THE NOSE 
    
    for n in monsterList:                          #keeps track of whether he touches a monster anywhere
        if ((leftSide>=n[0] and leftSide<n[0]+50)or(rightSide>=n[0] and rightSide<n[0]+50)) and ((yLocation>=n[1]-40 and yLocation<=n[1]-6) or (feet>=n[1]-40 and feet<=n[1])):  
            return True 
    return False 

def landOnMonster(monsterList,xLocation,yLocation):
    rightFoot=xLocation+34                         #location of the end of the right foot 
    feet=yLocation+90                              #bottom of the character
    leftFoot=xLocation+7                           #start of the left foot 
    
    for m in monsterList:                          #keeps track of whether his feet touch the top of a monster
        if ((leftFoot>=m[0]+1 and leftFoot<=m[0]+49) or(rightFoot>=m[0]+1 and rightFoot<=m[0]+49)) and (feet>=m[1]-50 and feet<=m[1]):
            return True, m 

#----------------------JUMPING UP AND DOWN: ACTIONS FOR THE GAME----------------

def updateGuy(yLocation,xLocation,power,monsterList,lives,platforms,status=False):
    if power>0:                                                    #if he has power, he goes up
        yLocation-=8
        power-=1
        if hitMonster(monsterList,xLocation,yLocation)==True:      #if he hits a monster,
            lives-=1                                               #player loses a life
        return yLocation, power,lives 
    else:                                                          #no power, so he goes down
        yLocation+=8
        if hitPlatform(xLocation,platforms,yLocation)==True:       #if he hits a platform he'll jump back up
            power=25     
        elif hitMonster(monsterList,xLocation,yLocation)==True:    #if he hits a monster:
            if landOnMonster(monsterList,xLocation,yLocation) and landOnMonster(monsterList,xLocation,yLocation)[0]:  #if lands on it,monster dies                     
                monsterList.remove(landOnMonster(monsterList,xLocation,yLocation)[1])
            else:                                                  #but if he doesn't land on it, player loses a life                        
                lives-=1    
    return yLocation, power, lives 
#-----------------------------BUFFER THE NEXT KEY PRESSED-------------------------------
def flushKeys():
    while Draw.hasNextKeyTyped():          
        newKey = Draw.nextKeyTyped()              #if any keyboard presses were saved up, get rid of them and restart 
        if newKey == "Right":                       
            newKey=Draw.hasNextKeyTyped
        elif newKey == "Left":          
            newKey= Draw.hasNextKeyTyped 

#-------------------------------------------------------------------------------
def stillPlaying(yLocation,yOrigin):   #if character falls off the bottom of the screen, GAME OVER 
    if yLocation+70<yOrigin+600:
        return True

#------------------MAIN FUNCTION FOR THE GAME-----------------------------------
            #this is the code for the way the game plays 

def main():
    platforms = makePlatforms(CANVAS_HEIGHT)
    monsterList=monsters(platforms) 
    power=25             #to propell the character 
    xLocation = 300      #Location of the characters left side at any given moment 
    yLocation = 500      #location of the top of the character- but not including the rounded top (essentially, just the top of the character) 
    yOrigin = 0          #the top of the screen window 
    count=0              #if player is playing for a long time, they win the game
    lives=1              
    status=False         #default setting without shooting 
    while stillPlaying(yLocation,yOrigin) and count<4000 and lives>0: 
        if Draw.hasNextKeyTyped():             #controling the left and right movement of the character 
            newKey = Draw.nextKeyTyped()
            if newKey == "Right":              #if user presses right key, move the character to the right 
                xLocation+=20
                if xLocation >550:
                    xLocation = -45
            elif newKey == "Left":             #if user presses left key, move the character to the left  
                xLocation -= 20
                if xLocation < 0:
                    xLocation = 549
            elif newKey== "Up":                #if the user presses up arrow, shoots the gun 
                    status=True 
                    canon=(yLocation-5)-yOrigin
                    
            
        yLocation,power,lives= updateGuy(yLocation,xLocation, power,monsterList,lives,platforms,status)
        
        
        Draw.clear()
        background(CANVAS_HEIGHT)  
        Draw.setColor(Draw.GREEN)
        if yLocation-yOrigin < 250:           #if the character gets to close to the top of the screen, move the screen window 
            yOrigin = yLocation-250
        yOrigin=drawPlatforms(platforms,yOrigin,CANVAS_HEIGHT)          
        doodleMan(xLocation, yLocation - yOrigin)  #Draw the doodlejump character 
        drawMonsters(monsterList,yLocation,xLocation,yOrigin)
        if status==True:                      #when you press the up arrow, status becomes true and it shoots 
            shotX=shootMonsters(xLocation,canon)
            canon, status=updateShot(shotX,canon,monsterList,status,yOrigin)     
        Draw.show() 
        count+=1
#----------When you either lose or have been playing for a while:---------------
    Draw.clear()
    background(CANVAS_HEIGHT)
    Draw.setColor(Draw.RED)
    Draw.setFontSize(20)
    Draw.setFontFamily('Ravie')
    Draw.string("DOODLEJUMP",160,50)
    Draw.setColor(Draw.BLACK)
    Draw.setFontFamily('Courier')
    Draw.string("Thanks For Playing",130,300)
    if not stillPlaying(yLocation,yOrigin) or lives==0: #if you died because you fell off the bottom of the screen 
        Draw.setFontSize(50)
        Draw.setFontFamily('Courier')
        Draw.string("Game Over",97,200)
        if lives==0:                            #if you died because you hit a monster 
            Draw.setFontFamily('Rockwell Extra Bold')
            Draw.setFontSize(25)
            Draw.string("You Hit A Monster",105,150)
    elif count==4000:                           #if you have been playing for a long time so you won
        Draw.setFontSize(50)
        Draw.setFontFamily('Courier')
        Draw.string("YOU WIN!",125,200)
    
    Draw.setColor(Draw.WHITE)
    Draw.filledRect(20,495,440,80)
    Draw.setColor(topBody)
    Draw.setFontSize(50)
    Draw.setFontFamily('Courier')
    Draw.string("Play Again",35,500)
    Draw.show()  
    while True:
        if Draw.mousePressed():               #restarts game if user presses play again 
            if (Draw.mouseX()>=20 and Draw.mouseX()<=460) and (Draw.mouseY()>=495 and Draw.mouseY()<=575):    
                flushKeys()
                main()


#--------------------------INVOKE THE GAME: PLAYING THE ACTUAL GAME-------------
startGame(topBody)