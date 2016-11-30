#!/usr/bin/python
import random


ROW_COUNT = 4
COLUMN_COUNT = 4
TILE_COUNT = ROW_COUNT * COLUMN_COUNT - 1
LEFT, RIGHT, UP, DOWN = 'left', 'right', 'up', 'down'
KEY_ACTIONS = {'a': LEFT, 'd': RIGHT, 'w': UP, 's': DOWN}


def main():
    field = init_field()
    space_x = ROW_COUNT - 1
    space_y = COLUMN_COUNT - 1
    while not game_finished(field, space_x, space_y):
        render(field)
        while True:
            command = input('Enter a/s/d/w or exit: ')
            if command == 'exit':
                return
            if command in KEY_ACTIONS:
                break
            else:
                print('Unknown command. Please try again.')
        space_x, space_y = do_move(field, KEY_ACTIONS[command],
                                   space_x, space_y)
    print('Game over!')


def init_field():
    # Fill the field with tiles in random order.
    tiles = list(range(1, TILE_COUNT + 1))
    random.shuffle(tiles)
    field = []
    for y in range(ROW_COUNT):
        row = []
        for x in range(COLUMN_COUNT):
            row.append(tiles.pop(0) if len(tiles) else None)
        field.append(row)
    return field


def game_finished(field, space_x, space_y):
    for i in range(0, TILE_COUNT - 2):
        if field[i // COLUMN_COUNT][i % COLUMN_COUNT] != i + 1:
            return False
    return space_x == ROW_COUNT - 1 and space_y == COLUMN_COUNT - 1


def render(field):
    output = []
    for y in range(ROW_COUNT):
        output.append(' ----' * COLUMN_COUNT + '\n')
        output.append('|    ' * COLUMN_COUNT + '|\n')
        for x in range(COLUMN_COUNT):
            tile = field[y][x]
            output.append('| {} '.format(
                str(tile if tile else '  ').rjust(2)) )
        output.append('|\n')
        output.append('|    ' * COLUMN_COUNT + '|\n')
    output.append(' ----' * COLUMN_COUNT + '\n')
    output.append('\n')
    print(''.join(output))


def do_move(field, action, space_x, space_y):
    # Get the moving tile position.
    tile_x = space_x
    tile_y = space_y
    if action == LEFT:
        tile_x += 1
    elif action == RIGHT:
        tile_x -= 1
    elif action == UP:
        tile_y += 1
    elif action == DOWN:
        tile_y -= 1
    # Check if the tile position is not outside of the field.
    if (tile_x < 0 or tile_y < 0
            or tile_x >= COLUMN_COUNT or tile_y >= ROW_COUNT):
        # Can't move, no changes.
        return space_x, space_y

    # Move the tile.
    field[space_y][space_x] = field[tile_y][tile_x]
    field[tile_y][tile_x] = None
    return tile_x, tile_y


if __name__ == '__main__':
    main()