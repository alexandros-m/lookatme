import cv2
import pygame


faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
displayWidth = 600
displayHeight = 400
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
clock = pygame.time.Clock()
pygame.display.set_caption('Mona Lisa Python')

black=(0,0,0)
white=(255,255,255)
darkGrey = (38, 39, 40)
grey = (130, 130, 130)
red = (255,0,0)
green = (0,255,0)
lightBlue = (85, 149, 252)

eyeRadius = int(displayWidth/7.5)

closeBoolean = False

def detectFaces():
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objects = faceCascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in objects:
        return (x,y,w,h)
        
##        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
##    cv2.imshow('Face Detection Live',img)
##    k = cv2.waitKey(30) & 0xff
##    if k == 27:
##        close()


def close():
    pygame.quit()
    cap.release()
    cv2.destroyAllWindows()
    exit()

##while True:
##    try:
##        detectFaces()
##    except KeyboardInterrupt:   
##        close()

class Circle(object):
    def __init__(self,color):
        self.color = color
    def display(self,center,radius):
        #center is a tuple (x,y)
        #radius is a num
        self.center = center
        self.radius = radius
        self.x = self.center[0] - self.radius
        self.y = self.center[1] - self.radius
        self.w = self.radius * 2
        self.h = self.radius * 2
        self.rect = pygame.Rect(self.x, self.y , self.w, self.h)
        pygame.draw.circle(gameDisplay, self.color, center, radius)

bg = Circle(white)
eyeball = Circle(black)

def draw(aTup):
    faceX = aTup[0]
    faceY = aTup[1]
    circleX = displayWidth - faceX
    circleY = displayHeight - faceY
    #print ('drawing at: ', circleX, circleY)
    gameDisplay.fill(black)

    bg.display((int(displayWidth/2),int(displayHeight/2)),eyeRadius)
    if circleX < 230:
        eyeball.display((230,int(displayHeight/2)),int(eyeRadius/4))
    elif circleX > 355:
        eyeball.display((365,int(displayHeight/2)),int(eyeRadius/4))
    else:
        eyeball.display((circleX,int(displayHeight/2)),int(eyeRadius/4))
        
    pygame.display.update()
    clock.tick(30)

def drawInCenter():
    eyeball.display((int(displayWidth/2),int(displayHeight/2)),eyeRadius)
    
#def drawCenter():
    
def mona():
    while not closeBoolean:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    close()
        faceTup = detectFaces()
        #print(faceTup)
        if faceTup != None:
            draw(faceTup)
        else:
            drawInCenter()
        
mona()
