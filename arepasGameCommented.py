import pygame
from random import randrange

pygame.init()

#Esta clase controla el juego de forma general
class Game:
  def __init__(self, timeSpan):
    # Máximo tiempo antes de reaparecer los elementos de juego (en milisegundos)
    self.timeSpan = timeSpan
    # Booleano para saber si el jamón fue atrapado
    self.caught = False
    # Booleano para saber si el usuario ganó
    self.win = False

  # Esta función utiliza una biblioteca llamada random para calcular números aleatorios
  # randrange genera un número entero aleatorio entre 0 y el parámetro ingresado
  def newRand(self):
    horizontal = randrange(maxWidth)
    vertical = randrange(maxHeight)
    return [horizontal, vertical]

  # Con esta función calculamos el movimiento de la persona, simplemente moviéndola si las teclas están presionadas
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

  # Esta función calcula qué tan cerca está un objeto de otro
  # Pudimos usar distancia euclidiana pero decidimos mantenerlo simple para no calcular raices y aumentar la velocidad
  def checkCollision(self, objectOne, objectTwo):
    xDistance = objectOne.positionX - objectTwo.positionX
    yDistance = objectOne.positionY - objectTwo.positionY
    return abs(xDistance+yDistance)

# Esta clase define a los elementos de juego como la arepa, el jamón o la persona
class GameElement:
  def __init__(self, type, positionX, positionY, game, persona="default"):
    # Cada elemento tiene un tipo (arepa, jamón o persona) y una posición en la pantalla
    self.type = type
    self.positionX = positionX
    self.positionY = positionY

  # Esta función nos ayuda a mostrar el objeto en la pantalla
  # Cuando el usuario atrapa el jamón o la arepa, bloqueamos sus posiciones para seguir a la persona
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


# Definimos algunas variables:
# i nos servirá para ir contando cada cuadro
i = 0
# Alto y ancho de la pantalla
maxHeight = 500
maxWidth = 800
# La pantalla de Pygame
screen = pygame.display.set_mode([maxWidth, maxHeight])
running = True
# Fíjate como podemos hacer varias asignaciones en una línea:
horizontal, vertical = 0, 0
# Creamos una variable de tipo Game, que es una clase que controla el juego, la verás más adelante
game = Game(700)
# Creamos tres elementos de juego con sus tipos, sus posiciones y el juego
# Ya verás más adelante la definición de un GameElement
persona = GameElement("persona", horizontal, vertical, game)
arepa = GameElement("arepa", maxWidth, maxHeight, game, persona)
jamon = GameElement("jamon", maxWidth, maxHeight, game, persona)


# Lo siguiente ocurre en cada iteración, una vez cada milisegundo:
while running:
  # En la variable keys guardamos las teclas que están presionadas
  keys = pygame.key.get_pressed()

  # Llamamos a la función controlMovement, que mueve al jugador cuando se presionan las teclas
  persona.positionX, persona.positionY = game.controlMovement(keys, persona.positionX, persona.positionY)
  # En cada iteración aumentamos i para ir contando
  i += 1  
  # Si i es mayor que el tiempo total de juego, reiniciamos y movemos los elementos
  if i > game.timeSpan:
    i = 0

    # Si el jugador no ha atrapado el jamón, pero está cerca de él (colisión), decimos que lo atrapó
    if not game.caught and game.checkCollision(persona, jamon) < 70:
      game.caught = True
      print("Jamón atrapado")

    # Si el jugador ya atrapó el jamón y ahora está cerca de la arepa, ganó
    if game.caught and game.checkCollision(persona, arepa) < 70:
      game.win = True
      print("Ganaste")

    # Si el jugador todavía no atrapa el jamón, movemos el jamón y la arepa a posiciones aleatorias
    if not game.caught:
      jamon.positionX, jamon.positionY = game.newRand()
      arepa.positionX, arepa.positionY = game.newRand()
    
  # Pintamos de gris el fondo y "dibujamos" los elementos para que se vean
  screen.fill((220, 220, 220))
  arepa.draw(screen, arepa.positionX, arepa.positionY)
  jamon.draw(screen, jamon.positionX, jamon.positionY)
  persona.draw(screen, persona.positionX, persona.positionY)
  
  # Si la persona decidió salir, terminamos
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  
  # Usamos esto para que los elementos se vean bien en la pantalla
  pygame.display.flip()
    
pygame.quit()