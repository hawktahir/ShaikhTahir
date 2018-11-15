print(" \t    |  _____     __             __ __               __                    |")
print(" \t    | / ___/_ __/ /  ___ ____  / // /__ _____    __/ /__ ___              |")
print("\t    | / /__/ // / _ \/ -_) __/ / _  / _ `(_-< |/|/ /  '_/(_-<             |")
print("\t    | \___/\_, /_.__/\__/_/   /_//_/\_,_/___/__,__/_/\_\/___/             |")
print("\t    |   /___/                                               Anonymous     |")
print("\t    |               Team: | Hawk Hacktivist | Hunk |                      | ")

import sys
import pygame

 
def run_game():
     #initializing game and create a screen object.
     pygame.init()
     screen = pygame.display.set_mode((600,600))
     pygame.display.set_caption("Alien Invation")
     bg_color=(230,230,230)
     
       
     
     #starting loop for game !
     
     while True :
         #watch keyboard and mouse events
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 sys.exit()
                 
                 screen.fill(bg_color)
                 #make te most rescent draw screen
         pygame.display.flip()
         
            
                 
    
    
    
run_game()