import pygame
import math

# x and y relative to a 1000-1000 display 

planetsDatas =[
		{
			"name":"Mercury",
			"color": (222,184,135),
			"width": 3,
			"radius": 100,
			"speed": 4.15,
			"x": 100,
			"y": 500,
			"hasRing": False,
			"moons":[]
		},
		{
			"name":"Venus",
			"color": (215, 212, 207),
			"width": 6,
			"radius": 137,
			"speed": 1.62,
			"x": 100,
			"y": 500,
			"hasRing": False,
			"moons":[]
		},
		{
			"name":"Earth",
			"color": (165, 190, 231),
			"width": 6,
			"radius": 175,
			"speed": 1,
			"x": 150,
			"y": 500,
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
			"speed": 0.56,
			"x": 200,
			"y": 500,
			"hasRing": False,
			"moons":[]
		},{
			"name":"Jupiter",
			"color": (180, 164, 156),
			"width": 15,
			"radius": 250,
			"speed": 0.083,
			"x": 250,
			"y": 500,
			"hasRing": False,
			"moons":[]
		},{
			"name":"Saturn",
			"color": (193, 184, 83),
			"width": 10,
			"radius": 300,
			"speed": 0.0345,
			"x": 300,
			"y": 500,
			"hasRing": True,
			"moons":[]
		},{
			"name":"Uranus",
			"color": (166, 193, 213),
			"width": 9,
			"radius": 350,
			"speed": 0.0119,
			"x": 350,
			"y": 500,
			"hasRing": False,
			"moons":[]
		}
		,{
			"name":"Neptune",
			"color": (144, 174, 224),
			"width": 9,
			"radius": 400,
			"speed": 0.006,
			"x": 400,
			"y": 500,
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
		self.x = parameters['x']
		self.y = parameters['y']
		self.radius = parameters['radius']
		self.speed = parameters['speed']
		if 'angle' in parameters:
			self.angle = parameters['angle']
		else:
			self.angle = 0

		self.moons = parameters['moons']

		for moon in self.moons:
			moon['x'] = self.x + moon['radius']
			moon['y'] = self.y + moon['radius']
			moon['angle'] = 0

	def getNextAngle(self,angle,speed):
		angle = angle + speed
		if angle > 360:
			angle -= 360
		angleRad = angle * math.radians(1)
		return angleRad,angle
	
	def draw(self,window):
		widthHalf, heightHalf = window.get_size()
		widthHalf, heightHalf = widthHalf/2, heightHalf/2

		pygame.draw.circle(window, (255,255,255), (widthHalf,heightHalf), self.radius, 1)
		pygame.draw.circle(window, self.color, (self.x,self.y), self.width)
		if self.hasRing:
			pygame.draw.circle(window, (255,255,255), (self.x,self.y), self.width+5, 1)

		for moon in self.moons:
			#pygame.draw.circle(window, (255,255,255), (self.x,self.y), self.radius, 1)
			pygame.draw.circle(window, moon['color'], (moon['x'],moon['y']), moon['width'])
	
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

