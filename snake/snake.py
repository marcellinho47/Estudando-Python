import curses


def draw_screen(window):
    window.clear()
    window.border(0)


def draw_snake(window, snake):
    window.addch(snake[0], snake[1], curses.ACS_CKBOARD)


def move_snake(snake, direction):
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
    return snake[0] in (0, height - 1) or snake[1] in (0, width - 1)


def game_loop(window):
    curses.curs_set(0)
    snake = [10, 15]

    while True:
        draw_screen(window=window)
        draw_snake(window, snake)

        direction = get_new_direction(window=window, timeout=1000)

        if direction is not None:
            move_snake(snake=snake, direction=direction)

        if check_hit_wall(snake=snake, window=window):
            return


if __name__ == "__main__":
    try:
        curses.wrapper(game_loop)
        print('Perdeu!')
    except Exception as e:
        print(f"Erro ao iniciar o curses: {e}")
