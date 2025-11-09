from enum import Enum
import sys


class Direction(Enum):
    UP = "↑"
    DOWN = "↓"
    LEFT = "←"
    RIGHT = "→"


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(f"{matrix[i][j]}", end=" ")
        print()


def main():
    if len(sys.argv) != 2:
        raise ValueError(
            "Argument Error: provide the size for the bi-dimensional matrix"
        )
    size = int(sys.argv[1])
    matrix = [[None for i in range(size)] for s in range(size)]
    print(f"Hi there! Here is your Spiral")
    direction = Direction.RIGHT
    x = 0
    y = 0
    while matrix[x][y] is None:

        print(f"LOOP x:{x} y:{y} direction:{direction}")
        if Direction.RIGHT == direction:
            if x + 1 < size and matrix[x + 1][y] is None:
                matrix[x][y] = Direction.RIGHT
                x += 1
            else:
                matrix[x][y] = Direction.DOWN
                direction = Direction.DOWN
                y += 1
            continue

        if Direction.DOWN == direction:
            if y + 1 < size and matrix[x][y + 1] is None:
                matrix[x][y] = Direction.DOWN
                y += 1
            else:
                matrix[x][y] = Direction.LEFT
                direction = Direction.LEFT
                x -= 1
            continue
        if Direction.LEFT == direction:
            if x - 1 > 0 and matrix[x - 1][y] is None:
                matrix[x][y] = Direction.LEFT
                x -= 1
            else:
                matrix[x][y] = Direction.UP
                direction = Direction.UP
                y -= 1
            continue
        if Direction.UP == direction:
            if y - 1 > 0 and matrix[x][y - 1] is None:
                matrix[x][y] = Direction.UP
                y -= 1
            else:
                matrix[x][y] = Direction.RIGHT
                direction = direction.RIGHT
                x += 1
            continue
    print(matrix)


if __name__ == "__main__":
    main()
