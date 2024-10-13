import pygame

pygame.init()
print('Setup Start')
window = pygame.display.set_mode(size=(600, 400))
print('Setup end')

print('loop Start')
while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # close window
            quit()  #fecha o pygame
