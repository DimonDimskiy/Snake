import time
import random
from config import *

# START_ROW = 5  # todo вынести константы в отдельный файл .config
# START_COL = 20
# START_LENGTH = 3
# HEIGHT = 10
# WIDTH = 50
# EMPTY_CELL = " "
# SNAKE_CELL = "#"
# APPLE_CELL = "@"


EMPTY_FIELD = {(y, x): EMPTY_CELL for y in range(HEIGHT) for x in range(WIDTH)}
START_SNAKE = [(START_ROW, x % WIDTH) for x in range((START_COL + 1) - START_LENGTH, (START_COL + 1))]


def print_field(field_):  # todo заменить функцию отрисовкой в окне, вынести отдельным модулем
    rows = []
    for i in range(HEIGHT):
        row = []
        for j in range(WIDTH):
            row.append(field_[(i, j)])
        row = "".join(row)
        rows.append(row)
    screen = '\n'.join(rows)
    print("-" * WIDTH)
    print(screen)
    print("-" * WIDTH)


def generate_apple(snake_, field_):
    field_ = field_.copy()
    snake_ = snake_.copy()
    for i in snake_:
        if i in field_:
            field_.pop(i)
    apple = random.choice(list(field_.keys()))
    apple_pos = {apple: APPLE_CELL}
    return apple_pos


def new_cell(cells):
    turn_right = None  # todo сделать опрос клавиатуры и вернуть True если нажата стрелка вправо, False если нажата стрелка влево, None если ничего не нажато
    head_cell = cells[-1]
    second_cell = cells[-2]
    y_head_cell, x_head_cell = head_cell
    y_second_cell, x_second_cell = second_cell
    is_moving_down = y_head_cell > y_second_cell and x_head_cell == x_second_cell  # todo учесть случай перехода через экран
    is_moving_up = y_head_cell < y_second_cell and x_head_cell == x_second_cell  # todo учесть случай перехода через экран
    is_moving_left = y_head_cell == y_second_cell and x_head_cell < x_second_cell  # todo учесть случай перехода через экран
    is_moving_right = True #y_head_cell == y_second_cell and x_head_cell > x_second_cell  # todo учесть случай перехода через экран

    if is_moving_down:
        if turn_right:
            x_head_cell -= 1
        elif turn_right is None:
            y_head_cell += 1
        else:
            x_head_cell += 1

    elif is_moving_up:
        if turn_right:
            x_head_cell += 1
        elif turn_right is None:
            y_head_cell -= 1
        else:
            x_head_cell -= 1

    elif is_moving_right:
        if turn_right:
            y_head_cell += 1
        elif turn_right is None:
            x_head_cell += 1
        else:
            y_head_cell -= 1

    elif is_moving_left:
        if turn_right:
            y_head_cell -= 1
        elif turn_right is None:
            x_head_cell -= 1
        else:
            y_head_cell += 1

    return y_head_cell % HEIGHT, x_head_cell % WIDTH


snake = START_SNAKE.copy()
apple_dict = generate_apple(snake, EMPTY_FIELD)
while True:
    time.sleep(0.05)

    snake_dict = {i: SNAKE_CELL for i in snake}
    field = EMPTY_FIELD.copy()
    field.update(snake_dict)
    field.update(apple_dict)

    print_field(field)

    y_head, x_head = new_cell(snake)


    if (y_head, x_head) in snake:
        print("GAME OVER")  # todo добавить текущий счёт, добавить вывод максимального счета в конце игры, добавить файл в который будет записываться максимальный счёт
        break

    if (y_head, x_head) not in apple_dict:
        snake.pop(0)
        snake.append((y_head, x_head))
    else:
        snake.append((y_head, x_head))
        apple_dict = generate_apple(snake_dict, field)


