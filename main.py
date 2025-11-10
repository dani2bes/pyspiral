from enum import Enum
import sys
from typing import List


class Direction(Enum):
    UP = "↑"
    DOWN = "↓"
    LEFT = "←"
    RIGHT = "→"


def print_spiral(matrix: List[List[Direction]]):
    print(f"Hi there! Here is your spiral")
    for row in matrix:
        print(" ".join(f"{cell.value}" for cell in row))


def generate_spiral(size: int) -> List[List[Direction]]:
    if size == 0:
        return []
    matrix = [[None] * size for _ in range(size)]
    direction = Direction.RIGHT
    row, col = 0, 0
    if size == 1:
        matrix[row][col] = direction
        return matrix
    while matrix[row][col] is None:
        if Direction.RIGHT == direction:
            if col + 1 < size and matrix[row][col + 1] is None:
                matrix[row][col] = Direction.RIGHT
                col += 1
            else:
                matrix[row][col] = Direction.DOWN
                direction = Direction.DOWN
                row += 1
            continue
        if Direction.DOWN == direction:
            if row + 1 < size and matrix[row + 1][col] is None:
                matrix[row][col] = Direction.DOWN
                row += 1
            else:
                matrix[row][col] = Direction.LEFT
                direction = Direction.LEFT
                col -= 1
            continue
        if Direction.LEFT == direction:
            if col - 1 >= 0 and matrix[row][col - 1] is None:
                matrix[row][col] = Direction.LEFT
                col -= 1
            else:
                matrix[row][col] = Direction.UP
                direction = Direction.UP
                row -= 1
            continue
        if Direction.UP == direction:
            if row - 1 >= 0 and matrix[row - 1][col] is None:
                matrix[row][col] = Direction.UP
                row -= 1
            else:
                matrix[row][col] = Direction.RIGHT
                direction = direction.RIGHT
                col += 1
            continue
    return matrix


def validate_arguments():
    if len(sys.argv) != 2:
        raise ValueError(
            "Argument Error: provide the size for the two-dimensional matrix"
        )
    size = int(sys.argv[1])
    if size < 0:
        raise ValueError("Argument Error: the size must be positive")


def main():
    validate_arguments()
    size = int(sys.argv[1])
    matrix = generate_spiral(size)
    print_spiral(matrix)


if __name__ == "__main__":
    main()
