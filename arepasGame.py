import pygame
from random import randrange

pygame.init()

class Game:
  def __init__(self, timeSpan):
    self.timeSpan = timeSpan
    self.caught = False
    self.win = False

  def newRand(self):
    horizontal = randrange(maxWidth)
    vertical = randrange(maxHeight)
    return [horizontal, vertical]

  def controlMovement(self, keys, horizontal, vertical):
    if keys[pygame.K_UP]:
      vertical -= 1
    elif keys[pygame.K_DOWN]:
      vertical += 1
    elif keys[pygame.K_LEFT]:
      horizontal -= 1
    elif keys[pygame.K_RIGHT]:
      horizontal += 1
    return [horizontal,vertical]

  def checkCollision(self, objectOne, objectTwo):
    xDistance = objectOne.positionX - objectTwo.positionX
    yDistance = objectOne.positionY - objectTwo.positionY
    return abs(xDistance+yDistance)

class GameElement:
  def __init__(self, type, positionX, positionY, game, persona="default"):
    self.type = type
    self.positionX = positionX
    self.positionY = positionY

  def draw(self, screen, positionX, positionY):
    if self.type == "arepa":
      if game.win:
        pygame.draw.circle(screen, (255, 204, 102), (persona.positionX+20, persona.positionY+20), 50)
      else:
        pygame.draw.circle(screen, (255, 204, 102), (self.positionX, self.positionY), 50)
    elif self.type == "jamon":
      if game.caught:
        pygame.draw.circle(screen, (181, 38, 22), (persona.positionX+20, persona.positionY+20), 30)
      else:
        pygame.draw.circle(screen, (181, 38, 22), (self.positionX, self.positionY), 30)
    elif self.type == "persona":
      pygame.draw.rect(screen, (154, 111, 68), (persona.positionX,persona.positionY,60,110))


i = 0
maxHeight = 500
maxWidth = 800
screen = pygame.display.set_mode([maxWidth, maxHeight])
running = True
horizontal, vertical = 0, 0
game = Game(700)
persona = GameElement("persona", horizontal, vertical, game)
arepa = GameElement("arepa", maxWidth, maxHeight, game, persona)
jamon = GameElement("jamon", maxWidth, maxHeight, game, persona)


while running:
  keys = pygame.key.get_pressed()
  persona.positionX, persona.positionY = game.controlMovement(keys, persona.positionX, persona.positionY)
  i += 1  
  if i > game.timeSpan:
    i = 0

    if not game.caught and game.checkCollision(persona, jamon) < 70:
      game.caught = True
      print("Jamón atrapado")

    if game.caught and game.checkCollision(persona, arepa) < 70:
      game.win = True
      print("Ganaste")

    if not game.caught:
      jamon.positionX, jamon.positionY = game.newRand()
      arepa.positionX, arepa.positionY = game.newRand()
    
  screen.fill((220, 220, 220))
  arepa.draw(screen, arepa.positionX, arepa.positionY)
  jamon.draw(screen, jamon.positionX, jamon.positionY)
  persona.draw(screen, persona.positionX, persona.positionY)
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  pygame.display.flip()
    
pygame.quit()