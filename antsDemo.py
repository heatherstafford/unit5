#Heather Stafford
#4/30/18
#antsDemo.py

from ggame import *
from random import randint

ANTS = 10
WIDTH = 600
HEIGHT = 600

if __name__ == '__main__':
    
    red = Color(0xff0000,1)
    ant = CircleAsset(10,LineStyle(1,red),red)
    
    for i in range(ANTS):
        Sprite(ant,(randint(1,WIDTH),randint(1,HEIGHT)))
    
    App().run()
