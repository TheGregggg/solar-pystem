# 
# Grégoire layet
# Solar system in python with pygame
# 04-08-2021
#

import pygame
import random
from planets import Planet
from planets import planetsDatas

height, width = 1000, 1000
window = pygame.display.set_mode((width, height))

planets = [Planet(planet) for planet in planetsDatas]

for planet in planets:
    planet.angle = random.randint(0,360)

# 1 day a second = 0.01643835616
# 1 hour a second = 0.01643835616/24 = 0.0006849315
# 1 minute a second = 0.0006849315/60 = 0.000011415525
# 1 second a second = 0.000011415525/60 = 1.9025875e-7 = 1.9025875*(10**-7)

speedMultiplier = 1

clock = pygame.time.Clock()

done = False
while not done: # main loop
    for event in pygame.event.get(): # event loop
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    window.fill((0,0,0)) #refill the screen
    pygame.draw.circle(window, (255, 255, 0), (width//2, height//2), 40, 40) # draw the sun

    for planet in planets:
        planet.move(window,speedMultiplier)
        planet.draw(window)
    
    pygame.display.update()
    clock.tick(60)


