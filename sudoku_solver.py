class Board:
    def __init__(self, board: list[list]) -> None:
        self.board = board

    def __str__(self) -> str:
        """
            print the updated board
        """

        upper_lines: str = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'
        middle_lines: str = f'╟───{"┼───"*2}{"╫───"}{"┼───"*2}{"╫───"}{"┼───"*2}╢\n'
        lower_lines: str = f'╚═══{"╧═══"*2}{"╩═══"}{"╧═══"*2}{"╩═══"}{"╧═══"*2}╝\n'
        board_string: str = upper_lines
        for index, line in enumerate(self.board):
            row_list: list = []
            for square_no, part in enumerate(
                    [line[:3], line[3:6], line[6:]], start=1
                    ):
                row_square: str = '|'.join(str(item) for item in part)
                row_list.extend(row_square)
                if square_no != 3:
                    row_list.append('║')

            row: str = f'║ {" ".join(row_list)} ║\n'
            row_empty: str = row.replace('0', ' ')
            board_string += row_empty

            if index < 8:
                if index % 3 == 2:
                    board_string += f'╠═══{"╪═══"*2}{"╬═══"}{"╪═══"*2}{"╬═══"}{"╪═══"*2}╣\n'
                else:
                    board_string += middle_lines
            else:
                board_string += lower_lines

        return board_string

    def find_empty_cell(self) -> tuple[int, int] | None:

        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row: int, num: int) -> bool:
        return num not in self.board[row]

    def valid_in_col(self, col: int, num: int) -> bool:
        return all(
            self.board[row][col] != num
            for row in range(9)
        )

    def valid_in_square(self, row: int, col: int, num: int) -> bool:
        row_start: int = (row // 3) * 3
        col_start: int = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty: tuple[int, int], num: int) -> bool:
        row, col = empty
        valid_in_row: bool = self.valid_in_row(row, num)
        valid_in_col: bool = self.valid_in_col(col, num)
        valid_in_square: bool = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self) -> bool:
        if (next_empty := self.find_empty_cell()) is None:
            return True
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                if self.solver():
                    return True
                self.board[row][col] = 0

        return False


def solve_sudoku(board):
    gameboard: Board = Board(board)
    print(f'\nPuzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print('\nSolved puzzle:')
        print(gameboard)
    else:
        print('\nThe provided puzzle is unsolvable.')
    return gameboard


puzzle = [
  [0, 0, 2, 0, 0, 8, 0, 0, 0],
  [0, 0, 0, 0, 0, 3, 7, 6, 2],
  [4, 3, 0, 0, 0, 0, 8, 0, 0],
  [0, 5, 0, 0, 3, 0, 0, 9, 0],
  [0, 4, 0, 0, 0, 0, 0, 2, 6],
  [0, 0, 0, 4, 6, 7, 0, 0, 0],
  [0, 8, 6, 7, 0, 4, 0, 0, 0],
  [0, 0, 0, 5, 1, 9, 0, 0, 8],
  [1, 7, 0, 0, 0, 6, 0, 0, 5]
]
solve_sudoku(puzzle)
