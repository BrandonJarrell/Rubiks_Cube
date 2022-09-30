# Author: Brandon Jarrell

import os, random, tkinter


os.system("cls")

rtop = [[1,1,1],[1,1,1],[1,1,1]]
rbottom = [[2,2,2],[2,2,2],[2,2,2]]
rleft = [[3,3,3],[3,3,3],[3,3,3]]
rright = [[4,4,4],[4,4,4],[4,4,4]]
rfront = [[0,0,0],[0,0,0],[0,0,0]]
rback =[[5,5,5],[5,5,5],[5,5,5]]


def display():
   # print top
   print("\t\t\t",rtop[0],"\n\t\t\t",rtop[1],"\n\t\t\t",rtop[2])
   print("\t -----------------------------------------")
   # print left, front, right
   print("\t",rleft[0],"\t",rfront[0],"\t",rright[0],"\t",rback[0])
   print("\t",rleft[1],"\t",rfront[1],"\t",rright[1],"\t",rback[1])
   print("\t",rleft[2],"\t",rfront[2],"\t",rright[2],"\t",rback[2])
   print("\t -----------------------------------------")
   print("\t\t\t",rbottom[0],"\n\t\t\t",rbottom[1],"\n\t\t\t",rbottom[2])
   print("\n\t/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\/\\\n")

##############
#     LEFT
def leftUp():
      # make buffer space
   buffer = []
   # make space on top
   buffer.append(rtop[0][0])
   buffer.append(rtop[1][0])
   buffer.append(rtop[2][0])
   # move front to top
   rtop[0][0] = rfront[0][0]
   rtop[1][0] = rfront[1][0]
   rtop[2][0] = rfront[2][0]
   # move bottom to front
   rfront[0][0] = rbottom[0][0]
   rfront[1][0] = rbottom[1][0]
   rfront[2][0] = rbottom[2][0]
   # move back to bottom
   rbottom[0][0] = rback[0][0]
   rbottom[1][0] = rback[1][0]
   rbottom[2][0] = rback[2][0]
   # put top (was in buffer) on back
   rback[0][0] = buffer[0]
   rback[1][0] = buffer[1]
   rback[2][0] = buffer[2]
   ##### NOW TO MOVE THE SIDES ######
   # make space on top
   buffer[0] = rleft[0][0]
   buffer[1] = rleft[0][1]
   buffer[2] = rleft[0][2]
   # move the right to the top
   rleft[0][1] = rleft[1][2]
   rleft[0][2] = rleft[2][2]
   # move bottom to right
   rleft[1][2] = rleft[2][1]
   rleft[2][2] = rleft[2][0]
   # move left to bottom
   rleft[2][1] = rleft[1][0]
   # put top on left
   rleft[0][0] = buffer[2]
   rleft[1][0] = buffer[1]
   rleft[2][0] = buffer[0]
   # you're all done


def leftDown():
   #3 lefts make a right
   leftUp()
   leftUp()
   leftUp()
##############
#     MIDDLE
def middleUp():
   # make buffer space
   buffer = []
   # make space on top
   buffer.append(rtop[0][1])
   buffer.append(rtop[1][1])
   buffer.append(rtop[2][1])
   # move front to top
   rtop[0][1] = rfront[0][1]
   rtop[1][1] = rfront[1][1]
   rtop[2][1] = rfront[2][1]
   # move bottom to front
   rfront[0][1] = rbottom[0][1]
   rfront[1][1] = rbottom[1][1]
   rfront[2][1] = rbottom[2][1]
   # move back to bottom
   rbottom[0][1] = rback[0][1]
   rbottom[1][1] = rback[1][1]
   rbottom[2][1] = rback[2][1]
   # put top (was in buffer) on back
   rback[0][1] = buffer[0]
   rback[1][1] = buffer[1]
   rback[2][1] = buffer[2]
   


def middleDown():
   #3 lefts make a right
   middleUp()
   middleUp()
   middleUp()
#############
#   RIGHT
def rightUp():
   # make buffer space
   buffer = []
   # make space on top
   buffer.append(rtop[0][2])
   buffer.append(rtop[1][2])
   buffer.append(rtop[2][2])
   # move front to top
   rtop[0][2] = rfront[0][2]
   rtop[1][2] = rfront[1][2]
   rtop[2][2] = rfront[2][2]
   # move bottom to front
   rfront[0][2] = rbottom[0][2]
   rfront[1][2] = rbottom[1][2]
   rfront[2][2] = rbottom[2][2]
   # move back to bottom
   rbottom[0][2] = rback[0][2]
   rbottom[1][2] = rback[1][2]
   rbottom[2][2] = rback[2][2]
   # put top (was in buffer) on back
   rback[0][2] = buffer[0]
   rback[1][2] = buffer[1]
   rback[2][2] = buffer[2]
   ###### MOVE THE RIGHT SIDE ####### 
   # make space on top
   buffer2 = []
   buffer2.append(rright[0][0])
   buffer2.append(rright[0][1])
   buffer2.append(rright[0][2])
   # move left to top
   rright[0][1] = rright[1][0]
   rright[0][0] = rright[2][0]
   # move bottom to left
   rright[1][0] = rright[2][1]
   rright[2][0] = rright[2][2]
   # move right to bottom
   rright[2][1] = rright[1][2]
   # put buffer (was on top) on right
   rright[0][2] = buffer2[0]
   rright[1][2] = buffer2[1]
   rright[2][2] = buffer2[2]




   #And you're done

def rightDown():
   #3 lefts make a right
   rightUp()
   rightUp()
   rightUp()

#        UP/DOWN
####################################
#       LEFT/RIGHT

#   TOP
def topRight():

   # make space on right
   buffer = rright[0]
   # move front to right
   rright[0] = rfront[0]
   # move left to front
   rfront[0] = rleft[0]
   # move back to left
   rleft[0] = rback[0]
   # put buffer (was right) to back
   rback[0] = buffer
   ###### rotate the top ######
   # make space on top
   buffer2 = []
   buffer2.append(rtop[0][0])
   buffer2.append(rtop[0][1])
   buffer2.append(rtop[0][2])
   # move the right to the top
   rtop[0][1] = rtop[1][2]
   rtop[0][2] = rtop[2][2]
   # move bottom to right
   rtop[1][2] = rtop[2][1]
   rtop[2][2] = rtop[2][0]
   # move left to bottom
   rtop[2][1] = rtop[1][0]
   # put top on left
   rtop[0][0] = buffer2[2]
   rtop[1][0] = buffer2[1]
   rtop[2][0] = buffer2[0]
   # you're all done

def topLeft():
   #3 lefts make a right
   topRight()
   topRight()
   topRight()
################
#   Middle
def middleRight():
   # make space on right
   buffer = rright[1]
   # move front to right
   rright[1] = rfront[1]
   # move left to front
   rfront[1] = rleft[1]
   # move back to left
   rleft[1] = rback[1]
   # put buffer (was right) to back
   rback[1] = buffer

def middleLeft():
   #3 lefts make a right
   middleRight()
   middleRight()
   middleRight()
################
#   Bottom
def bottomRight():
   # make space on right
   buffer = rright[2]
   # move front to right
   rright[2] = rfront[2]
   # move left to front
   rfront[2] = rleft[2]
   # move back to left
   rleft[2] = rback[2]
   # put buffer (was right) to back
   rback[2] = buffer
   ###### Rotate bottom ########
   # make space on top
   buffer2 = []
   buffer2.append(rbottom[0][0])
   buffer2.append(rbottom[0][1])
   buffer2.append(rbottom[0][2])
   # move left to top
   rbottom[0][1] = rbottom[1][0]
   rbottom[0][0] = rbottom[2][0]
   # move bottom to left
   rbottom[1][0] = rbottom[2][1]
   rbottom[2][0] = rbottom[2][2]
   # move right to bottom
   rbottom[2][1] = rbottom[1][2]
   # put buffer (was on top) on right
   rbottom[0][2] = buffer2[0]
   rbottom[1][2] = buffer2[1]
   rbottom[2][2] = buffer2[2]


def bottomLeft():
   #3 lefts make a right
   bottomRight()
   bottomRight()
   bottomRight()

#      LEFT/RIGHT
#################################
#        ROTATE

def rUp():
   leftUp()
   middleUp()
   rightUp()

def rDown():
   #3 lefts make a right
   rUp()
   rUp()
   rUp()
############
def rRight():
   topRight()
   middleRight()
   bottomRight()

def rLeft():
   #3 lefts make a right
   rRight()
   rRight()
   rRight()

def randomize():

   functionList = [topRight, topLeft, middleRight, middleLeft, bottomRight, bottomLeft, leftUp, leftDown, middleUp, middleDown, rightUp, rightDown]
   for _ in range(0,30):
      randomNum = random.randint(0,11)
      functionList[randomNum]()
      
display()

topRight()

rightUp()

display()

leftUp()

display()

