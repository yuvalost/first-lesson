import pygame

GAME_RES = 800, 600

pygame.init()
game_sc = pygame.display.set_mode(GAME_RES)
clock = pygame.time.Clock()

while True:
    game_sc.fill(pygame.color('black'))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.display.flip()
    clock.tick()



