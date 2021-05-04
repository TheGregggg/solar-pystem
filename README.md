# Fr - Pysteme solaire

Voici une simulation du systeme solaire réaliser en python.

Les tailles des planètes ne sont pas à l'echelle pour des soucis de lisibilité (on ne verait seulement le soleil et les planets serait plus petit qu'un pixel).

Les vitesses des planètes sont respectés (voir tableau après)

## Explication algorithme des planètes

Les données d'une planète sont représentées par un dictionnaire python (très proche du json)
```python
{
    "name":"Earth",
    "color": (165, 190, 231),
    "width": 6,
    "radius": 175,
    "speed": 1,
    "angle": 180,
    "hasRing": False,
    "moons":[{
        "color":  (209, 209, 209),
        "width": 3,
        "radius": 15,
        "speed": 13,
        "angle": 180
        }]
}
```
| Parametre           | Type                  | Explication           |
| :-------------------| :---------------------| :---------------------|
| name | Chaine | Nom de la planète, purement informatif
| color | Tuple trois entiers, 0-255 (code rvb) | Couleur de la planète, utiliser quand la planète est déssinée
| width | Entier | Rayon de la planète, en pixel, utilisé quand la planète est déssinée
| radius | Entier | Rayon du cercle de rotation de la planète, depuis le soleil, en pixel, utilisé quand la planète est déssinée
| speed | Décimale | Vitesse de rotation de la planète, utilisé pour calculé l'angle suivant
| angle | Entier | Angle par default au debut de la simulation, en deg, 0 = en bas
| hasRing | Booléen | si vrai, dessine un anneau autour de la planète 
| moons | Liste | Liste des lunes de la planète

| Parametre d'une lune | Type                  | Explication           |
| :--------------------| :---------------------| :---------------------|
| color | Tuple trois entiers, 0-255 (code rvb) | Couleur de la lune, utiliser quand la lune est déssinée
| width | Entier | Rayon de la lune, en pixel, utilisé quand la lune est déssinée
| radius | Entier | Rayon du cercle de rotation de la lune, depuis sa planète, en pixel, utilisé quand la lune est déssinée
| speed | Décimale | Vitesse de rotation de la lune, utilisé pour calculé l'angle suivant
| angle | Entier | Angle par default au debut de la simulation, en deg, 0 = en bas

<br>

Pour respectée les differences de vitesse entre les planètes, j'ai réaliser un tableau avec les calcules réaliser.

Globalement, je sais que la terre fait une révolution en 365j et j'ai choissis que la terre est la vitesse de base de mon programme, sa vitesse est donc de 1.

Mercure, par exemple, réalise une révolution en 88j, je fait donc 365*1/88 = 365/88 = 4.15

| Planète          | Révolution      | Vitesse         |
| :----------------| :---------------| :---------------|
| Earth            | 365             | 1
| Mercure          | 88              | 365/88 = 4.15
| Venus            | 225             | 365/225 = 1.62
| Mars             | 687             | 365/687 = 0.53
| Jupiter          | 4333            | 365/4333 = 0.084
| Saturn           | 10759           | 365/10759 = 0.034
| Uranus           | 30687           | 365/30687 = 0.012
| Neptune          | 60190           | 365/60190 = 0.006

<br>

| Lune - Planète   | Révolution      | Vitesse         |
| :----------------| :---------------| :---------------|
| Earth            | 365             | 1
| Lune - Earth     | 28              | 365/28 = 13
| Phobos - Mars    | 1/3             | 365/(1/3) = 1095
| Deimos - Mars    | 30/24=1.25      | 365/1.25 = 292

<br>

Source : [NASA](https://solarsystem.nasa.gov/planets)

J'ai ensuite voulu rajouter les lunes, j'ai donc ajouter la Lune, puis j'ai découvert que mars avait 2 lunes, Phobos et Deimos. J'ai calculé leur vitesses avec la même formule.
Puis, j'ai découvert que les autres planètes avait des dizaines de lunes. J'ai donc choisis de laissée la Lune, Phobos et Deimos et de ne pas en rajouté. Comme l'echelle ne peut pas etre respectée cela rendrait illisible la simulation.

### Fonctions
La fonction 'move' va demander a la fonction 'getNextAngle' de calculer prochain l'angle de la planète.
Avec cette angle, on indique que le X de la planète (utiliser dans la fonction 'draw') est égale à la moitiée de l'écran (point de référence) + le sinus de l'angle * radius
On indique que le Y de la planète est égale est égale à la moitiée de l'écran + le cosinus de l'angle * radius

la fonction 'getNextAngle' ajoute la vitesse de la planète à son angle. Convertie cette angle en radians et renvoie les deux informations.
la fonction move enregistre le nouvelle angle et utilise l'angle en radians pour les calcules de cos et sin.

Pour les lunes c'est la même chose mais la planète est le point de référence des calcules.

<br>

## Explication du programme

Le fichier solar.py contient la boucle principale du programme.
Le fichier planets.py contient les informations de chaque planètes ainsi que le classe pour créer un objet Planet.

<br>

```python
import pygame
import random
from planets import Planet
from planets import planetsDatas
```
Pygame est la bibliothèque graphique utilisé 
J'importe ensuite la class Planet depuis planets.py ainsi que planetsData.

<br>

```python
height, width = 1000, 1000
window = pygame.display.set_mode((width, height))
```
Création de la fenètre pygame

<br>

```python
planets = [Planet(planet) for planet in planetsDatas]
for planet in planets:
    planet.angle = random.randint(0,360)
```
Création d'une liste des objects Planet avec comme parametre les données de chaque planète. Applique un angle aléatoire pour ne pas commencer la simulation avec les planètes allignées.

<br>

La boucle infinie est la boucle principal. Elle est appelée 60 fois par seconde maximum ( clock.tick(60) - une fonction de pygame ). 

<br>

```python
for planet in planets:
    planet.move(window,speedMultiplier)
    planet.draw(window)
```
Après avoir déssiné le soleil, le programme boucles pour chaque planètes, les déplaces et les déssines.

<br>

## Problème du programme
 - L'echelle n'est pas bonne, pour des problème de visibilité
 - Les rotations des planètes n'est pas représenté. Principalement a cause de l'unicité des couleurs de chaque planètes.
 - Les positions des planètes est généré aléatoirement à chaque démarage, je n'est pas réussi à calculer leur position actuelle avec les formules utilisant leur axe de rotation et leur position a l'année 2000.

<br>

# Eng - Solar Pystem
A python solar system

| Planet           | Revolution      | Speed           |
| :----------------| :---------------| :---------------|
| Earth | 365 | 1
| Mercury | 88 | 365/88=4.15
| Venus  | 225 | 365/225=1.62
| Mars  | 365*1.8=657 | 365/657=0.56
| Jupiter  | 365*12=4380 | 365/4380=0.083
| Saturn  | 365*29=10585 | 365/10585=0.0345
| Uranus  | 365*84=30660 | 365/30660=0.0119
| Neptune  | 365*165=60225 | 365/60225=0.006

| Moon - Planet           | Revolution      | Speed           |
| :----------------| :---------------| :---------------|
| Earth | 365 | 1
| Moon - Earth | 28 | 365/28=13
| Phobos - Mars | 1/3 | 365/(1/3)=1095
| Phobos - Mars | 30/24=1.25 | 365/1.25=292
