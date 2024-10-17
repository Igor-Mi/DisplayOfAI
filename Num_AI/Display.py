#Made by Igor Michalec

import pygame
import math
import time
def unpickle(file):
    import pickle
    with open('./mnist.pkl/'+file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict
def sigmoid(x):
    return (1/(1+(math.e)**(-x)))
def dot(Array1,Array2):
    sum_of = 0
    for i in range(len(Array1)):
        sum_of+=Array1[i]*Array2[i]
    return sum_of
def AI(current_input):
    new = read('NetSets')
    w1= new[0]
    w2= new[1]
    w3= new[2]

    b1= new[3]
    b2= new[4]
    b3= new[5]
    l1 =[]
    l2 =[]
    hl = []
    for i in range(len(w1)):
        l1.append(sigmoid(dot(w1[i],current_input)+b1[i]))
    for i in range(len(w2)):
        l2.append(sigmoid(dot(w2[i],l1)+b2[i]))
    for i in range(len(w3)):
        hl.append(sigmoid(dot(w3[i],l2)+b3[i]))
    return hl
def read(name):
    out = []
    file = open(name+'.txt','r')
    split1 = file.read().split("\n")
    i = 0
    def getw(i):
        w = []
        while split1[i] != "":
            split = split1[i].split(" ")
            split.pop()
            for j in range(len(split)):
                split[j] = float(split[j])
            w.append(split)
            i +=1
        i +=1
        return[i,w]
    def getb(i):
        b = []
        while split1[i] != "":
            b.append(float(split1[i]))
            i +=1
        i +=1
        return[i,b]
    for k in range(3):
        temp = getw(i)
        i = temp[0]
        out.append(temp[1])
        
    for k in range(3):
        temp = getb(i)
        i = temp[0]
        out.append(temp[1])
    return out

def col_rect(colour,x,y,width,height): #creates a rectangle that will resize with the window
    pygame.draw.rect(display,(255*colour,255*colour,255*colour),(x,y,width,height) )

def write(colour,text, x, y, size):# writes text
    font = pygame.font.SysFont("Arial", size)
    rend = font.render(text,1,(255*colour,255*colour,255*colour))
    display.blit(rend,(x,y))
def clear_board():
    number = []
    for i in range(784):
        number.append(0)
    return number
#Main loop
pygame.init()#Initializes all of the pygame modules


pygame.display.set_caption("Number AI")#Sets the name of the window to what is in teh brackets

display_width = 640
display_height = 700

display = pygame.display.set_mode((display_width,display_height))#Creates the display


number = clear_board()

for p in unpickle("mnist.pkl")[1][0]:#Main loop
    #board
    display.fill((0,0,0))
    number = p
    for i in range(28):
        for j in range(28):
            col_rect(number[i*28+j],300+j*10,300+i*10,10,10)
    col_rect(1,295,295,5,290)
    col_rect(1,580,295,5,290)
    col_rect(1,300,295,280,5)
    col_rect(1,300,580,280,5)
    score = AI(number)
    high = -1
    num = -1
    for i in range(len(score)):
        if score[i] > high:
            high = score[i]
            num = i
        write(1,str(i)+": "+str(round(score[i]*100,1))+"%(1 d.p)",0,20*i,20)
    write(1,"Number: "+str(num),160,20,40)
        

    #to here
    pygame.display.update()#Updating the display
    time.sleep(1)
    for event in pygame.event.get():#Checking for inputs
        if event.type == pygame.QUIT:#Checking for closing
            pygame.quit()
            quit()



