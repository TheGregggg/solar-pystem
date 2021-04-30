# 
# Grégoire layet
# Solar system in python with pygame
# 04-08-2021
#

import pygame
from planet import Planet
from planet import planetsDatas

import time

height = 1000
width = 1000

window = pygame.display.set_mode((width, height))

planets = [Planet(planet) for planet in planetsDatas]

# 1 day a second = 0.01643835616
# 1 hour a second = 0.01643835616/24 = 0.0006849315
# 1 minute a second = 0.0006849315/60 = 0.000011415525
# 1 second a second = 0.000011415525/60 = 1.9025875e-7 = 1.9025875*(10**-7)

speedMultiplier = 1

clock = pygame.time.Clock()

done = False
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    window.fill((0,0,0))
    pygame.draw.circle(window, (255, 255, 0), (width//2, height//2), 40, 40)

    for planet in planets:
        planet.draw(window)
        
    for planet in planets:
        planet.move(window,speedMultiplier)

    #print(planets[0].angle)
    
    pygame.display.update()
    clock.tick(60)


