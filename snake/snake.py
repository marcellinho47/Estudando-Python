import curses
import random
import time


def draw_screen(window):
    window.clear()
    window.border(0)


def draw_snake(window, snake):
    head = snake[0]
    draw_in_screen(window, head, '@')
    for part in snake[1:]:
        draw_in_screen(window, part, '*')


def draw_in_screen(window, actor, char):
    window.addch(actor[0], actor[1], char)


def move_snake(snake, direction):
    head = snake[0].copy()
    move_snake_part(head, direction)
    snake.insert(0, head)
    snake.pop()


def generate_new_fruit(window, snake):
    height, width = window.getmaxyx()
    return [
        random.randint(1, height - 2),
        random.randint(1, width - 2)
    ]


def move_snake_part(snake, direction):
    match direction:
        case curses.KEY_RIGHT:
            snake[1] += 1
        case curses.KEY_LEFT:
            snake[1] -= 1
        case curses.KEY_UP:
            snake[0] -= 1
        case curses.KEY_DOWN:
            snake[0] += 1


def get_new_direction(window, timeout):
    window.timeout(timeout)
    direction = window.getch()
    if direction in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_UP, curses.KEY_DOWN]:
        return direction
    return None


def check_hit_wall(snake, window):
    height, width = window.getmaxyx()
    head = snake[0]
    return head[0] in (0, height - 1) or head[1] in (0, width - 1)


def check_hit_fruit(snake, fruit):
    if snake[0] == fruit:
        return True


def check_hit_snake(snake):
    return snake[0] in snake[1:]


def direction_is_opposite(current_direction, direction):
    return (current_direction == curses.KEY_RIGHT and direction == curses.KEY_LEFT) or \
        (current_direction == curses.KEY_LEFT and direction == curses.KEY_RIGHT) or \
        (current_direction == curses.KEY_UP and direction == curses.KEY_DOWN) or \
        (current_direction == curses.KEY_DOWN and direction == curses.KEY_UP)


def finish_game(window, score):
    window.clear()
    window.border(0)
    height, width = window.getmaxyx()
    message = f'Game Over! Score: {score}'
    y = int(height / 2)
    x = int((width - len(message)) / 2)
    window.addstr(y, x, message)
    window.refresh()
    time.sleep(10)


def game_loop(window):
    curses.curs_set(0)
    snake = [
        [10, 15],
        [10, 14]
    ]
    fruit = generate_new_fruit(window, snake)
    current_direction = curses.KEY_RIGHT
    score = 0

    while True:
        draw_screen(window=window)
        draw_snake(window, snake)
        draw_in_screen(window, fruit, curses.ACS_DIAMOND)
        direction = get_new_direction(window=window, timeout=1)

        if direction is None:
            direction = current_direction

        if direction_is_opposite(current_direction, direction):
            direction = current_direction

        move_snake(snake=snake, direction=direction)

        if check_hit_wall(snake=snake, window=window):
            break

        if check_hit_snake(snake=snake):
            break

        if check_hit_fruit(snake=snake, fruit=fruit):
            fruit = generate_new_fruit(window, snake)
            snake.append(snake[-1].copy())
            score += 1

        current_direction = direction

    finish_game(window, score)


if __name__ == "__main__":
    try:
        curses.wrapper(game_loop)
        print('Perdeu!')
    except Exception as e:
        print(f"Erro ao iniciar o curses: {e}")
