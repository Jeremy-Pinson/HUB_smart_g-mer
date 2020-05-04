#!/usr/bin/env python3

import pygame
import random

score = 0

background_color = (50, 50, 50)
snake_color = (100, 255, 100)
is_start = True
mode = (500, 500)
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
window = pygame.display.set_mode(mode)
apple = pygame.Rect(random.randrange(0, 500, 20), random.randrange(0, 500, 20), 20, 20)

snake_piece = pygame.Rect(60, 60, 20, 20)
snake_piece_list = [snake_piece, ]
move_snake_x = 0
move_snake_y = 0
new_piece = False


while is_start:
    pygame.time.delay(200)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_start = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_snake_x = 0
                move_snake_y = -20
            if event.key == pygame.K_DOWN:
                move_snake_x = 0
                move_snake_y = 20
            if event.key == pygame.K_LEFT:
                move_snake_x = -20
                move_snake_y = 0
            if event.key == pygame.K_RIGHT:
                move_snake_x = 20
                move_snake_y = 0

    window.fill(background_color)

    snake_save = snake_piece_list[-1].copy()

    i = -1
    while snake_piece_list[i] != snake_piece_list[0]:
        snake_piece_list[i] = snake_piece_list[i - 1].copy()
        i -= 1

    snake_piece_list[0].left += move_snake_x
    snake_piece_list[0].top += move_snake_y

    if snake_piece_list[0].center == apple.center:
        new_piece = True
        score += 1
        apple.top = random.randrange(0, 500, 20)
        apple.left = random.randrange(0, 500, 20)

    if new_piece:
        new_piece = False
        snake_piece_list.append(snake_save)

    tmp_list = snake_piece_list.copy()
    tmp_list.pop(0)
    if snake_piece_list[0].top == 500 or snake_piece_list[0].left == 500 or snake_piece_list[0].top < 0 or snake_piece_list[0].left < 0:
        print("lose")
        exit(score)
    for snake in tmp_list:
        if snake == snake_piece_list[0]:
            print("lose")
            exit(score)

    pygame.draw.rect(window, (255, 100, 100), apple)
    for snake in snake_piece_list:
        pygame.draw.rect(window, snake_color, snake)

    score_str_obj = myfont.render("score : {}".format(score), False, (0, 0, 0))
    window.blit(score_str_obj, (400, 20))
    pygame.display.flip()
