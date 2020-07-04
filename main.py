import pygame
from rules import *
from widgets import Button

pygame.init()
size = (1000, 500)
screen = pygame.display.set_mode(size)
screen.fill([255, 255, 255])
pygame.display.set_icon(screen)
pygame.display.set_caption('')
clock, fps = pygame.time.Clock(), 30

grid = generate_grid()

class Rect():
    def __init__(self, x, y, w, h, xy_index):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.xy_index = xy_index

        self.rect = pygame.Rect(x, y, w, h)

    def __call__(self):
        return self.rect

#buttons
btn_counter_lock = 0
frames_to_wait = 5

y = 50
pause_btn = Button(600, y, 300, 50, text='Pause', surface_to_draw_to=screen) ; pause = False
y += 75
randomise_btn = Button(600, y, 300, 50, text='Randomise Field', surface_to_draw_to=screen)
y += 75
clear_btn = Button(600, y, 300, 50, text='Clear Field', surface_to_draw_to=screen)
y += 75
fill_btn = Button(600, y, 300, 50, text='Fill Field', surface_to_draw_to=screen)
y += 75
draw_grid_btn = Button(600, y, 300, 50, text='Toggle Grid', surface_to_draw_to=screen) ; draw_grid = False

while True:
    #region events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    key = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    #endregion
    screen.fill([51, 51, 51])

    # region buttons

    if pause : pause_btn.main_color = [50, 100, 50] ; pause_btn.text = 'Unpause'
    else:      pause_btn.main_color = [255, 255, 255] ; pause_btn.text = 'Pause'

    pause_btn.show()
    if pause_btn.update(mouse_pos, mouse_pressed) and btn_counter_lock == 0:
        pause = not pause
        btn_counter_lock = frames_to_wait
    
    randomise_btn.show()
    if randomise_btn.update(mouse_pos, mouse_pressed) and btn_counter_lock == 0:
        grid = generate_grid()
        btn_counter_lock = frames_to_wait

    clear_btn.show()
    if clear_btn.update(mouse_pos, mouse_pressed) and btn_counter_lock == 0:
        grid = generate_grid(fill=-1)
        btn_counter_lock = frames_to_wait

    fill_btn.show()
    if fill_btn.update(mouse_pos, mouse_pressed) and btn_counter_lock == 0:
        grid = generate_grid(fill=100)
        btn_counter_lock = frames_to_wait

    draw_grid_btn.show()
    if draw_grid_btn.update(mouse_pos, mouse_pressed) and btn_counter_lock == 0:
        draw_grid = not draw_grid
        btn_counter_lock = frames_to_wait

    if btn_counter_lock != 0 : btn_counter_lock -= 1
    #endregion

    #region grid management
    if not pause:
        grid = run_single_step(grid)

    w = (size[0]/2) / len(grid[0])
    h = size[1] / len(grid)

    rects = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            state = grid[y][x]
            color = [(not state) * 255 for _ in range(3)]
            r = Rect(x * w, y * h, w, h, [x,y])
            pygame.draw.rect(screen, color, r())

            if draw_grid:
                pygame.draw.rect(screen, [51, 51, 51], r(), 1)

            rects.append(r)
    #endregion

    #region drawing with mouse
    if pause:
        mx, my = mouse_pos
        if (index := pygame.Rect(mx, my, 1, 1).collidelist(rects)) != -1 and mouse_pressed == (1, 0, 0):
            x, y = rects[index].xy_index
            grid[y][x] = True
        if (index := pygame.Rect(mx, my, 1, 1).collidelist(rects)) != -1 and mouse_pressed == (0, 0, 1):
            x, y = rects[index].xy_index
            grid[y][x] = False
    #endregion

    pygame.display.update()
    clock.tick(fps)