#Heather Stafford
#4/30/18
#antsDemo.py

from ggame import *

ANTS = 10

if __name__ == '__main__':
    
    red = Color(0xff0000,1)
    ant = CircleAsset(10,LineStyle(1,red),red)
    
    Sprite(ant)
    
    App().run()
