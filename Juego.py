# Llamar las librerías pygame y random así como la clase Network
import pygame
import random
from Network import Network

from pygame import KEYDOWN, K_ESCAPE, K_SPACE, K_BACKSPACE, K_RETURN

WIDTH = 800  # Se establece el ancho de la ventana
HEIGHT = 530  # Se establece el largo de la ventana

# Se establecen diversos colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Se inicia pygame
pygame.init()
# Se inicia el mixer de pygame
pygame.mixer.init()
# Se inicia la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Se establece el nombre de la ventana
pygame.display.set_caption("pyDakarDeath")
# Se establece el reloj 
clock = pygame.time.Clock()

# constantes y constantes Globales para el username
user_text = "Jugador1:"#variable para guardar nombre de jugador1
user_text2 = "Jugador2:"#variable para guardar nombre del jugdor2
font = pygame.font.Font(None, 20)#Constante para el font y tamaño de letra


# Esta funcion se utiliza para establecer el tipo de letra a utilizar en el juego
def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size)  # Se importa la fuente a utilizar
    text_surface = font.render(text, True, BLACK)  # Se establece el color del texto
    text_rect = text_surface.get_rect()  # Se obtiene el rectangulo del tecto
    text_rect.midtop = (x, y)  # Se establece el centro del texto
    surface.blit(text_surface, text_rect)  # Se muestra el texto en pantalla


# Se dibuja la vida del jugador 1
def draw_shield_barp1(surface, x, y, percentage):
    global user_text, font# globales que contienen constantes y variables para nombre del jugador1
    input_rect1 = pygame.Rect(10, 15, 300, 30)#rectangulo para posicionamiento de user_text

    BAR_LENGHT = 100  # Se establece el ancho de la barra de vida
    BAR_HEIGHT = 10  # Se establece el largo de la barra de vida
    fill = (percentage / 100) * BAR_LENGHT  # Se establece el relleno de la barra de vida
    border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)  # Se establece el borde de la barra de vida
    fill = pygame.Rect(x, y, fill, BAR_HEIGHT)  # Se ubica el relleno de la barra de vida
    pygame.draw.rect(surface, GREEN, fill)  # Se dibuja el relleno de la barra de vida
    pygame.draw.rect(surface, WHITE, border, 2)  # Se dibuja el borde de la barra de vida

    superficie_texto = font.render(user_text, True, BLACK)  # Se dibuja el nombre del jugador en pantalla
    screen.blit(superficie_texto, input_rect1)  # Se muestra el nombre del jugador en pantalla


# Se dibuja la vida del jugador 2
def draw_shield_barp2(surface, x, y, percentage):
    global user_text2, font #globales que contienen constantes y variables para nombre del jugador2
    input_rect2 = pygame.Rect(700, 15, 300, 30)#rectangulo para posicionamiento de user_text2

    BAR_LENGHT = 100  # Se establece el ancho de la barra de vida
    BAR_HEIGHT = 10  # Se establece el largo de la barra de vida
    fill = (percentage / 100) * BAR_LENGHT  # Se establece el relleno de la barra de vida
    border = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)  # Se establece el borde de la barra de vida
    fill = pygame.Rect(x, y, fill, BAR_HEIGHT)  # Se ubica el relleno de la barra de vida
    pygame.draw.rect(surface, GREEN, fill)  # Se dibuja el relleno de la barra de vida
    pygame.draw.rect(surface, WHITE, border, 2)  # Se dibuja el borde de la barra de vida

    superficie_texto2 = font.render(user_text2, True, BLACK)  # Se dibuja el nombre del jugador en pantalla
    screen.blit(superficie_texto2, input_rect2)  # Se muestra el nombre del jugador en pantalla


# Se crea la clase del jugador 1
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Jugadores/car1.png").convert()  # Se importa la imagen del jugador 1
        self.image.set_colorkey(WHITE)  # Se borra el fondo de la imagen importada
        self.rect = self.image.get_rect()  # Se obtiene la recta de la imagen
        self.rect.centerx = WIDTH * 1 / 4  # Se ubica al jugador en la pantalla a lo ancho
        self.rect.bottom = 400  # Se ubica al jugador en la pantalla a lo largo
        self.speed_x = 0  # Se establece la velocidad del eje x
        self.speed_y = 0  # Se establece la velocidad del eje y
        self.shield = 100  # Se establece la vida del jugador

    def update(self):
        self.speed_x = 0  # Se establece la velocidad del eje x
        self.speed_y = 0  # Se establece la velocidad del eje y
        keystate = pygame.key.get_pressed()  # Se verifica si se preciona alguna tecla
        if keystate[pygame.K_a]:
            self.speed_x = -5  # Si se toca la tecla a, la velocidad del eje x se restará en 5
        if keystate[pygame.K_d]:
            self.speed_x = 5  # Si se toca la tecla d, la velocidad del eje x se sumará en 5
        if keystate[pygame.K_w]:
            self.speed_y = -5  # Si se toca la tecla w, la velocidad del eje y se restará en 5
        if keystate[pygame.K_s]:
            self.speed_y = 5  # Si se toca la tecla s, la velocidad del eje y se sumará en 5
        self.rect.x += self.speed_x  # Se actualiza la velocidad respecto a la posicion del eje x
        self.rect.y += self.speed_y  # Se actualiza la velocidad respecto a la posicion del eje y
        if self.rect.right > 350:
            self.rect.right = 350  # Se verifica que el jugador caiga en el barranco
            self.shield = 0  # La vida del jugador llega a 0
        if self.rect.left < 0:
            self.rect.left = 0  # Se verifica que el jugador no se salga de la pantalla
        if self.rect.top < 0:
            self.rect.top = 0  # Se verifica que el jugador no se salga de la pantalla
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT  # Se verifica que el jugador no se salga de la pantalla

    def shoot_up(self):  # Se crea la funcion para disparar arriba
        bullet = Bulletp1_up(self.rect.centerx, self.rect.top)  # Se establece la bala
        all_sprites.add(bullet)  # Se añade la bala al grupo de sprites
        bulletsp1.add(bullet)  # Se añade la bala al grupo de balas del jugador 1
        bullet_sound.play()  # Se ejecuta el sonido de disparo

    def shoot_right(self):  # Se crea la funcion para disparar a la derecha
        bullet = Bulletp1_right(self.rect.centerx, self.rect.top)  # Se establece la bala
        all_sprites.add(bullet)  # Se añade la bala al grupo de sprites
        bulletsp1.add(bullet)  # Se añade la bala al grupo de balas del jugador 1
        bullet_sound.play()  # Se ejecuta el sonido de disparo


# Se crea la clase del jugador 2
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Jugadores/car2.png").convert()  # Se importa la imagen del jugador 2
        self.image.set_colorkey(WHITE)  # Se borra el fondo de la imagen importada
        self.rect = self.image.get_rect()  # Se obtiene la recta de la imagen
        self.rect.centerx = WIDTH * 3 / 4  # Se ubica al jugador en la pantalla a lo ancho
        self.rect.bottom = 400  # Se ubica al jugador en la pantalla a lo largo
        self.speed_x = 0  # Se establece la velocidad del eje x
        self.speed_y = 0  # Se establece la velocidad del eje y
        self.shield = 100  # Se establece la vida del jugador

    def update(self):
        self.speed_x = 0  # Se establece la velocidad del eje x
        self.speed_y = 0  # Se establece la velocidad del eje y
        keystate = pygame.key.get_pressed()  # Se verifica si se preciona alguna tecla
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5  # Si se toca la flecha izquierda, la velocidad del eje x se restará en 5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5  # Si se toca la flecha derecha, la velocidad del eje x se sumará en 5
        if keystate[pygame.K_UP]:
            self.speed_y = -5  # Si se toca la flecha arriba, la velocidad del eje x se restará en 5
        if keystate[pygame.K_DOWN]:
            self.speed_y = 5  # Si se toca la flecha abajo, la velocidad del eje x se sumará en 5
        self.rect.x += self.speed_x  # Se actualiza la velocidad respecto a la posicion del eje x
        self.rect.y += self.speed_y  # Se actualiza la velocidad respecto a la posicion del eje y
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH  # Se verifica que el jugador no se salga de la pantalla
        if self.rect.left < 450:
            self.rect.left = 450  # Se verifica que el jugador caiga en el barranco
            self.shield = 0  # La vida del jugador llega a 0
        if self.rect.top < 0:
            self.rect.top = 0  # Se verifica que el jugador no se salga de la pantalla
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT  # Se verifica que el jugador no se salga de la pantalla

    def shoot_up(self):  # Se crea la funcion para disparar arriba
        bullet = Bulletp2_up(self.rect.centerx, self.rect.top)  # Se establece la bala
        all_sprites.add(bullet)  # Se añade la bala al grupo de sprites
        bulletsp2.add(bullet)  # Se añade la bala al grupo de balas del jugador 2
        bullet_sound.play()  # Se ejecuta el sonido de disparo

    def shoot_left(self):  # Se crea la funcion para disparar a la izquierda
        bullet = Bulletp2_left(self.rect.centerx, self.rect.top)  # Se establece la bala
        all_sprites.add(bullet)  # Se añade la bala al grupo de sprites
        bulletsp2.add(bullet)  # Se añade la bala al grupo de balas del jugador 2
        bullet_sound.play()  # Se ejecuta el sonido de disparo


# Se establece la clase de obstaculos
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(obstacle_images)  # Se importan las imagenes de los obstaculos
        self.image.set_colorkey(WHITE)  # Se borran los fondos de las imagenes
        self.rect = self.image.get_rect()  # Se obtienen las rectas de los obstaculos
        self.rect.x = random.randrange(WIDTH - self.rect.width)  # Se establece la hubicacion en el eje x
        self.rect.y = random.randrange(-500, 100)  # Se establece la hubicacion en el eje y
        self.speedy = 5  # Se establece la velocidad en el eje y

    def update(self):
        self.rect.y += self.speedy  # Se actualiza la hubicacion respecto a la velocidad
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 25:  # Se verifica que el
            # obstaculo se salga de la pantalla
            self.rect.x = random.randrange(WIDTH - self.rect.width)  # Se establece la hubicacion en el eje x
            self.rect.y = random.randrange(-500, 0)  # Se establece la hubicacion en el eje y
            self.speedy = 5  # Se establece la velocidad en el eje y


class Salida(pygame.sprite.Sprite):  # Se establece la clase de la linea de salida
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Fondo/salida.png").convert()  # Se importa la imagen
        self.rect = self.image.get_rect()  # Se establece la recta
        self.rect.x = 0  # Se hubica en el eje x
        self.rect.y = 200  # Se ubica en el eje y
        self.speedy = 5  # Se establece la velocidad

    def update(self):
        self.rect.y += self.speedy  # Se actualiza la velocidad


class Barranco(pygame.sprite.Sprite):  # Se establece la clase del barranco
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Fondo/barranco.png").convert()  # Se importa la imagen
        self.image.set_colorkey(WHITE)  # Se borra el fondo de la imagem
        self.rect = self.image.get_rect()  # Se establece la recta
        self.rect.x = 280.5  # Se hubica la recta en el eje x
        self.rect.y = -330  # Se hubica la recta en el eje y
        self.speedy = 5  # Se establece la velocidad

    def update(self):
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT  # Se verifica que el barranco no se salga de la pantalla
        self.rect.y += self.speedy  # Se actualiza la hubicacion respecto a la velocidad


# Se genera la clase de balas-arriba del jugador 1
class Bulletp1_up(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Balas/balap1_up.png").convert()  # Se importa la imagen
        self.image.set_colorkey(WHITE)  # Se borra el fondo
        self.rect = self.image.get_rect()  # Se obtiene la recta
        self.rect.y = y  # Se hubica en el eje y
        self.rect.centerx = x  # Se hubica en el eje x
        self.speedy = -10  # Se establece la velocidad

    def update(self):
        self.rect.y += self.speedy  # Se actualiza la hubicacion respecto a la velocidad
        if self.rect.bottom < 0:
            self.kill()  # Se verifica que la bala salga de la pantalla


# Se genera la clase de balas-derecha del jugador 1
class Bulletp1_right(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Balas/balap1_right.png").convert()  # Se importa la imagen
        self.image.set_colorkey(WHITE)  # Se borra el fondo
        self.rect = self.image.get_rect()  # Se obtiene la recta
        self.rect.y = y  # Se hubica en el eje y
        self.rect.centerx = x  # Se hubica en el eje x
        self.speedx = 10  # Se establece la velocidad

    def update(self):
        self.rect.x += self.speedx  # Se actualiza la hubicacion respecto a la velocidad
        if self.rect.left > WIDTH:
            self.kill()  # Se verifica que la bala salga de la pantalla


# Se genera la clase de balas-arriba del jugador 2
class Bulletp2_up(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Balas/balap2_up.png").convert()  # Se importa la imagen
        self.image.set_colorkey(WHITE)  # Se borra el fondo
        self.rect = self.image.get_rect()  # Se obtiene la recta
        self.rect.y = y  # Se hubica en el eje y
        self.rect.centerx = x  # Se hubica en el eje x
        self.speedy = -10  # Se establece la velocidad

    def update(self):
        self.rect.y += self.speedy  # Se actualiza la hubicacion respecto a la velocidad
        if self.rect.bottom < 0:
            self.kill()  # Se verifica que la bala salga de la pantalla


# Se genera la clase de balas-izquierda del jugador 2
class Bulletp2_left(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Balas/balap2_left.png").convert()  # Se importa la imagen
        self.image.set_colorkey(WHITE)  # Se borra el fondo
        self.rect = self.image.get_rect()  # Se obtiene la recta
        self.rect.y = y  # Se hubica en el eje y
        self.rect.centerx = x  # Se hubica en el eje x
        self.speedx = -10  # Se establece la velocidad

    def update(self):
        self.rect.x += self.speedx  # Se actualiza la hubicacion respecto a la velocidad
        if self.rect.right < 0:
            self.kill()  # Se verifica que la bala salga de la pantalla


# Se genera la clase Explosion
class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = explosion_anim[0]  # Se establece las imagenes
        self.rect = self.image.get_rect()  # Se obtiene la recta
        self.rect.center = center  # Se establece el centro
        self.frame = 0  # Se establece el frame
        self.last_update = pygame.time.get_ticks()  # Se establecen los ticks
        self.frame_rate = 50  # Velocidad de la animacion

    def update(self):
        now = pygame.time.get_ticks()  # Se obtienen los ticks
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1  # Se actualizan los frames
            if self.frame == len(explosion_anim):  # Se verifica que la animacion terminara
                self.kill()  # Se elimina el sprite
            else:
                center = self.rect.center  # Se establece el centro
                self.image = explosion_anim[self.frame]  # Se selecciona la imagen a mostrar
                self.rect = self.image.get_rect()  # Se obtiene la recta
                self.rect.center = center  # Se actualiza el centri


# Se genera la funcion de fin de tiempo
def show_game_over_time_screen():
    screen.blit(background, [0, 0])  # Se hubica en pantalla
    draw_text(screen, "Se acabó el tiempo!", 65, WIDTH // 2, HEIGHT // 4)  # Se escribe el texto
    pygame.display.flip()  # Se dibuja en pantalla
    if pygame.event == pygame.QUIT:
        pygame.quit()  # Se cierra pygame


# Se genera la funcion de game over
def show_game_over_screen():
    global user_text2, user_text, font ##globales que contienen constantes y variables para nombre del jugador1 y jugador2
    input_rect1 = pygame.Rect(WIDTH // 2 - 52, HEIGHT // 2 + 75, 300, 20)# establece el tamaño y posicionamiento de rectangulo que contiene el nombre
    input_rect2 = pygame.Rect(WIDTH // 2 - 52, HEIGHT // 2 + 115, 300, 20)# establece el tamaño y posicionamiento de rectangulo que contiene el nombre

    activo1 = False #indica si se esta utilizando el cuadro para escribir el nombre o no
    activo2 = False#indica si se esta utilizando el cuadro para escribir el nombre o no
    waiting = True
    while waiting:  # Se genera la funcion while
        clock.tick(60)  # Se establecen los fps
        for event in pygame.event.get(): #crea los eventos
            if event.type == pygame.QUIT:
                pygame.quit()  # Se verifica si se cierra el juego y cierra pygame
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect1.collidepoint(event.pos):#indica que el cuadro esta siendo precionado con el mouse para añadir el nombre
                    activo1 = True
                    activo2 = False #desactiva el otro para que no se escriba lo mismo en los dos cuadros

                if input_rect2.collidepoint(event.pos):#indica que el cuadro esta siendo precionado con el mouse para añadir el nombre
                    activo2 = True
                    activo1 = False#desactiva el otro para que no se escriba lo mismo en los dos cuadros

            if event.type == pygame.KEYDOWN:
                if activo1 == True:# si el cuadro esta activo se puede escribir si detecta un unicode y borra si detecta un backspace
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]#borra de el string si detecta un backspace

                    else:
                        user_text += event.unicodese #puede añade la letra a string si detecta un unicode

                if activo2 == True: # si el cuadro esta activo se puede escribir si detecta un unicode y borra si detecta un backspace
                    if event.key == pygame.K_BACKSPACE:
                        user_text2 = user_text2[:-1] #borra del string si detecta un backspace
                    else:
                        user_text2 += event.unicode #puede añade la letra a el string si detecta un unicode

                if event.key == pygame.K_RETURN: # si detecta la tecla return y el tamaño del string es mayior a 9 permite el inicio del juego cambiando el True por un False
                    if (len(user_text) and len(user_text2)) > 9:
                        waiting = False

        screen.blit(background, [0, 0])  # Se genera el fondo en la pantalla
        superficie_texto = font.render(user_text, True, BLACK)# produce un render del texto que esta en la string user_text
        superficie_texto2 = font.render(user_text2, True, BLACK)# produce un render del texto que esta en la string user_text2

        draw_text(screen, "pyDakarDeath", 65, WIDTH // 2, HEIGHT // 4)  # Se dibuja el texto en pantalla
        draw_text(screen, "Utilizar las flechas y las teclas 'WASD' para manejar el carro", 27, WIDTH // 2,
                  HEIGHT // 2)  # Se dibuja el texto en pantalla
        draw_text(screen, "disparar con SPACE y Q, y 0 y 1 en el NumPad", 27, WIDTH // 2, HEIGHT // 2 + 25)  # Se
        # dibuja el texto en pantalla
        draw_text(screen, "Press return once you enter the names", 20, WIDTH // 2, HEIGHT * 3 / 4 + 50)  # Se dibuja
        # el texto en pantalla
        pygame.draw.rect(screen, BLACK, input_rect1, 1)#genera un rectangulo para el texto en la pantalla
        pygame.draw.rect(screen, BLACK, input_rect2, 1)#genera un rectangulo para el texto en la pantalla

        screen.blit(superficie_texto, input_rect1)# produce la imagen del texto escrito en la pantalla
        screen.blit(superficie_texto2, input_rect2)# produce la imagen del texto escrito en la pantalla

        input_rect1.w = superficie_texto.get_width() + 10# permite que las dimensicones del cuadro se ajusten al tamaño del texto
        input_rect2.w = superficie_texto2.get_width() + 10# permite que las dimensicones del cuadro se ajusten al tamaño del texto

        pygame.display.flip()  # Actualiza pygame


# Se debine la pantalla de jugador 1 pierde
def p1_loser_screen():
    global user_text2
    screen.blit(background, [0, 0])  # Se hubica en pantalla
    draw_text(screen, user_text2, 65, WIDTH // 2, HEIGHT // 4)  # Se dibuja el texto
    draw_text(screen, "Press Key", 20, WIDTH // 2, HEIGHT * 3 / 4)  # Se dibuja el texto
    pygame.display.flip()  # Actualiza pygame
    waiting = True
    while waiting:  # Se genera el ciclo while
        clock.tick(60)  # Se establecen los fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Verifica si se cierra pygame
            if event.type == pygame.KEYDOWN:
                waiting = False  # Se verifica si se rompe el ciclo


# Se debine la pantalla de jugador 2 pierde
def p2_loser_screen():
    global user_text
    screen.blit(background, [0, 0])  # Se hubica en pantalla
    draw_text(screen, user_text, 65, WIDTH // 2, HEIGHT // 4)  # Se dibuja el texto
    draw_text(screen, "Press Key", 20, WIDTH // 2, HEIGHT * 3 / 4)  # Se dibuja el texto
    pygame.display.flip()  # Actualiza pygame
    waiting = True
    while waiting:  # Se genera el ciclo while
        clock.tick(60)  # Se establecen los fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Verifica si se cierra pygame
            if event.type == pygame.KEYDOWN:
                waiting = False  # Se verifica si se rompe el ciclo


obstacle_images = []  # Se genera una lista para los obstaculos
obstacles_list = ["Obstaculos/cactus.png", "Obstaculos/obstaculo.png", "Obstaculos/piedra.png"]  # Se importan las
# imagenes
for img in obstacles_list:
    obstacle_images.append(pygame.image.load(img).convert())  # Se cargan las imagenes

# Explosión
explosion_anim = []
for i in range(9):
    file = "Balas/regularExplosion0{}.png".format(i)  # Se carga las imagenes
    img = pygame.image.load(file).convert()  # Se cargan las imagenes
    img.set_colorkey(BLACK)  # Se borra el fondo
    img_scale = pygame.transform.scale(img, (70, 70))  # Se establece el tamaño de a imagen
    explosion_anim.append(img_scale)  # Se hubica la imagen

# Imagen de fondo
background = pygame.image.load("Fondo/arena.png").convert()  # Se carga la imagen
caracteresvalidos = "abcdefghijklmnñopqrstuvwxyz"

# Cargar sonidos
bullet_sound = pygame.mixer.Sound("Sonidos/GunShotSnglShotIn PE1097906.wav")
explosion_sound = pygame.mixer.Sound("Sonidos/ES_Car Drop 7 - SFX Producer.wav")
pygame.mixer.music.load("Sonidos/videoplayback.ogg")
pygame.mixer.music.set_volume(0.5)  # Se establece el volumen

pygame.mixer.music.play(loops=-1)  # Se establece el loop de la musica

p1 = Player1()  # Clase jugador 1
p2 = Player2()  # Clase jugador 2

# Se establecen variables
game_over = True
running = True
p1_loser = False
p2_loser = False
while running:  # While principal
    current_time = pygame.time.get_ticks()  # Obtiene los ticks
    timer = 1000  # Se establece el timer

    while current_time >= timer:  # While para dar puntos a los jugadores conforme avanzan
        scorep1 += 1
        scorep2 += 1
        timer += 10000

    if current_time >= 90000:  # While que verifica que no se acabe el tiempo de 90 segundos
        show_game_over_time_screen()
        pygame.time.delay(3000)
        running = False

    if game_over:  # While de game over

        x = 5  # Numero de enemigos a generar

        show_game_over_screen()  # Muestra la pantalla de game over

        game_over = False  # Modifica la variable game_over
        all_sprites = pygame.sprite.Group()  # Genera un grupo
        obstacle_list = pygame.sprite.Group()  # Genera un grupo
        bulletsp1 = pygame.sprite.Group()  # Genera un grupo
        bulletsp2 = pygame.sprite.Group()  # Genera un grupo

        salida = Salida()
        all_sprites.add(salida)  # Añade sprite a al grupo
        barranco = Barranco()
        all_sprites.add(barranco)  # Añade sprite a al grupo
        player1 = Player1()
        all_sprites.add(player1)  # Añade sprite a al grupo
        player2 = Player2()
        all_sprites.add(player2)  # Añade sprite a al grupo

        for i in range(x):  # Generacion de enemigos
            obstacle = Obstacle()
            all_sprites.add(obstacle)
            obstacle_list.add(obstacle)

        # Puntaje de los jugadores
        scorep1 = 0
        scorep2 = 0

    if p1_loser:  # Verifica si el jugador 1 pierde
        print('hola')
        x += 5  # Genera 5 nuevos enemigos

        p1_loser_screen()  # Muestra la pantalla de jugador 1 pierde

        p1_loser = False  # Modifica la variable p1_loser
        all_sprites = pygame.sprite.Group()  # Genera un grupo
        obstacle_list = pygame.sprite.Group()  # Genera un grupo
        bulletsp1 = pygame.sprite.Group()  # Genera un grupo
        bulletsp2 = pygame.sprite.Group()  # Genera un grupo

        salida = Salida()
        all_sprites.add(salida)  # Añade sprite a al grupo
        barranco = Barranco()
        all_sprites.add(barranco)  # Añade sprite a al grupo
        player1 = Player1()
        all_sprites.add(player1)  # Añade sprite a al grupo
        player2 = Player2()
        all_sprites.add(player2)  # Añade sprite a al grupo

        for i in range(x):  # Generacion de enemigos
            obstacle = Obstacle()
            all_sprites.add(obstacle)
            obstacle_list.add(obstacle)

    if p2_loser:  # Verifica si el jugador 2 pierde
        print('hola')
        x += 5  # Genera 5 nuevos enemigos

        p2_loser_screen()  # Muestra la pantalla de jugador 2 pierde

        p2_loser = False  # Modifica la variable p2_loser
        all_sprites = pygame.sprite.Group()  # Genera un grupo
        obstacle_list = pygame.sprite.Group()  # Genera un grupo
        bulletsp1 = pygame.sprite.Group()  # Genera un grupo
        bulletsp2 = pygame.sprite.Group()  # Genera un grupo

        salida = Salida()
        all_sprites.add(salida)  # Añade sprite a al grupo
        barranco = Barranco()
        all_sprites.add(barranco)  # Añade sprite a al grupo
        player1 = Player1()
        all_sprites.add(player1)  # Añade sprite a al grupo
        player2 = Player2()
        all_sprites.add(player2)  # Añade sprite a al grupo

        for i in range(x):  # Generacion de enemigos
            obstacle = Obstacle()
            all_sprites.add(obstacle)
            obstacle_list.add(obstacle)

    if player1.shield <= 0:
        p1_loser = True  # Verifica si el jugador 1 pierde

    if player2.shield <= 0:
        p2_loser = True  # Verifica si el jugador 2 pierde

    clock.tick(60)  # Se establece los fps
    for event in pygame.event.get():  # Obtiene los eventos
        if event.type == pygame.QUIT:
            running = False  # Verifica si se cierra el juego y cierra pygame

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player1.shoot_up()  # Verifica si se toca la tecla de espacio y dispara arriba
            if event.key == pygame.K_KP0:
                player2.shoot_up()  # Verifica si se toca el 0 y dispara arriba
            if event.key == pygame.K_e:
                player1.shoot_right()  # Verifica si se toca la tecla e y dispara a la derecha
            if event.key == pygame.K_KP1:
                player2.shoot_left()  # Verifica si se toca la tecka 1 y dispara a la izquierda

    all_sprites.update()  # Actualiza los sprites

    # Colisiones - obstaculo - balap1
    hitsp1 = pygame.sprite.groupcollide(obstacle_list, bulletsp1, True, True)
    for hit in hitsp1:
        scorep1 += 500  # Suma puntos
        explosion_sound.play()  # Reproduce el sonido de exploison
        explosion = Explosion(hit.rect.center)  # Genera la explosion
        all_sprites.add(explosion)  # Añade el sprite al grupo
        obstacle = Obstacle()  # Genera nuevamente el enemigo
        all_sprites.add(obstacle)
        obstacle_list.add(obstacle)

    # Colisiones - p1 - obstaculo
    hitsp1 = pygame.sprite.spritecollide(player1, obstacle_list, True)
    for hit in hitsp1:
        player1.shield -= 25  # Resta puntos de vida
        obstacle = Obstacle()  # Genera nuevamente el enemigo
        all_sprites.add(obstacle)
        obstacle_list.add(obstacle)
        if player1.shield <= 0:
            p1_loser = True  # Verifica su el jugador 1 muere

    # Colisiones - p2 - balap1
    hitsp1 = pygame.sprite.spritecollide(player2, bulletsp1, True)
    for hit in hitsp1:
        player2.shield -= 50  # Resta la vida del jugador 2
        if player2.shield <= 0:
            p2_loser = True  # Verifica su el jugador 2 muere

        # Colisiones - obstaculo - balap2
    hitsp2 = pygame.sprite.groupcollide(obstacle_list, bulletsp2, True, True)
    for hit in hitsp2:
        scorep2 += 500  # Suma puntos
        explosion_sound.play()  # Reproduce el sonido de exploison
        explosion = Explosion(hit.rect.center)  # Genera la explosion
        all_sprites.add(explosion)  # Añade el sprite al grupo
        obstacle = Obstacle()  # Genera nuevamente el enemigo
        all_sprites.add(obstacle)
        obstacle_list.add(obstacle)

    # Colisiones - p2 - obstaculo
    hitsp2 = pygame.sprite.spritecollide(player2, obstacle_list, True)
    for hit in hitsp2:
        player2.shield -= 25  # Resta vida al jugador 2
        obstacle = Obstacle()  # Genera nuevamente el enemigo
        all_sprites.add(obstacle)
        obstacle_list.add(obstacle)
        if player2.shield <= 0:
            p2_loser = True  # Verifica su el jugador 2 muere

    # Colisiones - p1 - balap2
    hitsp2 = pygame.sprite.spritecollide(player1, bulletsp2, True)
    for hit in hitsp2:
        player1.shield -= 50  # Resta vida el jugador 1
        if player1.shield <= 0:
            p1_loser = True  # Verifica su el jugador 1 muere

    screen.blit(background, [0, 0])  # Hubica el fondo

    all_sprites.draw(screen)  # Genera los sprites

    # Genera el marcador en pantalla
    draw_text(screen, str(scorep1), 25, WIDTH * 1 / 4, 10)
    draw_text(screen, str(scorep2), 25, WIDTH * 3 / 4, 10)

    # Genera la barra de salud
    draw_shield_barp1(screen, 5, 5, player1.shield)
    draw_shield_barp2(screen, 690, 5, player2.shield)


    # Función para leer la posición de los jugadores dentro del juego
    def read_pos(str):
        print(str)
        str = str.split(",")
        return int(str[0]), int(str[1])


    # Función que transforma la posición inicial pasandolo de string a una tupla
    def make_pos(tup):
        return str(tup[0]) + "," + str(tup[1])


    # Función que se encarga de llamar a la Network y ejecutar el juego dentro de ella
    def main():
        run = True
        n = Network()
        print(n.getPos())
        startPos = read_pos(n.getPos())
        clock = pygame.time.Clock()


    pygame.display.flip()  # Actualiza pygame
pygame.quit()  # Cierra pygame
main()  # Llama main
