import pygame
import math

planetsDatas =[
		{
			"name":"Mercury",
			"color": (222,184,135),
			"width": 3,
			"radius": 100,
			"speed": 4.15,
			"hasRing": False,
			"moons":[]
		},{
			"name":"Venus",
			"color": (215, 212, 207),
			"width": 6,
			"radius": 137,
			"speed": 1.62,
			"hasRing": False,
			"moons":[]
		},{
			"name":"Earth",
			"color": (165, 190, 231),
			"width": 6,
			"radius": 175,
			"speed": 1,
			"hasRing": False,
			"moons":[{
				"color":  (209, 209, 209),
				"width": 3,
				"radius": 15,
				"speed": 13
				}]
		},{
			"name":"Mars",
			"color": (232, 193, 135),
			"width": 5,
			"radius": 212,
			"speed": 0.53,
			"hasRing": False,
			"moons":[{
				"color":  (209, 209, 209),
				"width": 1,
				"radius": 15,
				"speed": 1095
				},{
				"color":  (209, 230, 230),
				"width": 1,
				"radius": 15,
				"speed": 292,
				"angle": 180
				}]
		},{
			"name":"Jupiter",
			"color": (180, 164, 156),
			"width": 15,
			"radius": 250,
			"speed": 0.084,
			"hasRing": False,
			"moons":[]
		},{
			"name":"Saturn",
			"color": (193, 184, 83),
			"width": 10,
			"radius": 300,
			"speed": 0.034,
			"hasRing": True,
			"moons":[]
		},{
			"name":"Uranus",
			"color": (166, 193, 213),
			"width": 9,
			"radius": 350,
			"speed": 0.012,
			"hasRing": False,
			"moons":[]
		},{
			"name":"Neptune",
			"color": (144, 174, 224),
			"width": 9,
			"radius": 400,
			"speed": 0.006,
			"hasRing": False,
			"moons":[]
		}
	]

class Planet(object):
	def __init__(self,parameters):
		self.name = parameters['name']
		self.hasRing = parameters['hasRing']
		self.width = parameters['width']
		self.color = parameters['color']
		self.x = 0
		self.y = 0 
		self.radius = parameters['radius']
		self.speed = parameters['speed']
		self.angle = 0 if not 'angle' in parameters else parameters['angle']

		self.moons = parameters['moons']

		for moon in self.moons:
			moon['x'] = self.x + moon['radius']
			moon['y'] = self.y + moon['radius'] 
			moon['angle'] = 0 if not 'angle' in moon else moon['angle']

	def getNextAngle(self,angle,speed):
		angle = angle + speed
		if angle > 360:
			angle -= 360
		angleRad = angle * math.radians(1) # convert angle to radians
		return angleRad,angle
	
	def draw(self,window):
		widthHalf, heightHalf = window.get_size()
		widthHalf, heightHalf = widthHalf/2, heightHalf/2

		pygame.draw.circle(window, (255,255,255), (widthHalf,heightHalf), self.radius, 1) # draw line
		pygame.draw.circle(window, self.color, (self.x,self.y), self.width) # draw planet
		if self.hasRing:
			pygame.draw.circle(window, (255,255,255), (self.x,self.y), self.width+7, 3) # draw ring

		for moon in self.moons:
			pygame.draw.circle(window, moon['color'], (moon['x'],moon['y']), moon['width']) # draw moon
	
	def move(self,window,speedMultiplier):
		widthHalf, heightHalf = window.get_size()
		widthHalf, heightHalf = widthHalf/2, heightHalf/2

		angle, self.angle = self.getNextAngle(self.angle,self.speed*speedMultiplier)
		self.x = int(widthHalf + math.sin(angle) * self.radius)
		self.y = int(heightHalf + math.cos(angle) * self.radius)

		for moon in self.moons:
			angle,moon['angle'] = self.getNextAngle(moon['angle'],moon['speed']*speedMultiplier)
			moon['x'] = int(self.x + math.sin(angle) * moon['radius'])
			moon['y'] = int(self.y + math.cos(angle) * moon['radius'])