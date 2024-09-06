import curses


def game_loop(window):
    curses.curs_set(0)
    window.border(0)
    height, width = window.getmaxyx()

    mob = [10, 15]
    window.addch(mob[0], mob[1], curses.ACS_DIAMOND)

    while True:
        window.timeout(1000)
        char = window.getch()

        window.clear()
        window.border(0)

        match char:
            case curses.KEY_RIGHT:
                mob[1] += 1
            case curses.KEY_LEFT:
                mob[1] -= 1
            case curses.KEY_UP:
                mob[0] -= 1
            case curses.KEY_DOWN:
                mob[0] += 1
            case _:
                pass

        if mob[0] in (0, height - 1) or mob[1] in (0, width - 1):
            return

        window.addch(mob[0], mob[1], curses.ACS_DIAMOND)


if __name__ == "__main__":
    try:
        curses.wrapper(game_loop)
        print('Perdeu!')
    except Exception as e:
        print(f"Erro ao iniciar o curses: {e}")
