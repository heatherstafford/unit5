#Heather Stafford
#4/30/18
#antsDemo.py

from ggame import *
from random import randint

ANTS = 10
WIDTH = 600
HEIGHT = 500

def step():
    for ant in data['antlist']:
        ant.x += 1
        ant.y += 1

if __name__ == '__main__':
    
    data = {}
    data['antlist'] = []
    
    red = Color(0xff0000,1)
    ant = CircleAsset(10,LineStyle(1,red),red)
    
    for i in range(ANTS):
        data['antlist'].append(Sprite(ant,(randint(1,WIDTH),randint(1,HEIGHT))))
    
    App().run(step)
