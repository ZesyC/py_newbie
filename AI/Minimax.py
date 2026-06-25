MAY = 'X'
NGUOI = 'O'


def minimax(board, luot_may):
    lines = []

    for i in range(3):
        lines.append(board[i])
        lines.append([board[0][i], board[1][i], board[2][i]])

    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line == [MAY, MAY, MAY]:
            return 1
        if line == [NGUOI, NGUOI, NGUOI]:
            return -1

    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return 0

    if luot_may:
        diem_tot_nhat = -float('inf')

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = MAY
                    diem = minimax(board, False)
                    board[i][j] = ' '
                    diem_tot_nhat = max(diem_tot_nhat, diem)

        return diem_tot_nhat

    diem_tot_nhat = float('inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = NGUOI
                diem = minimax(board, True)
                board[i][j] = ' '
                diem_tot_nhat = min(diem_tot_nhat, diem)

    return diem_tot_nhat


def bai_minimax():
    board = [
        ['X', 'O', 'X'],
        [' ', 'O', 'X'],
        [' ', ' ', 'O']
    ]

    nuoc_tot_nhat = None
    diem_tot_nhat = -float('inf')

    print("Bàn cờ hiện tại:")
    for row in board:
        print(' | '.join(row))
    print()

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = MAY

                print(f"Thử nước đi ({i}, {j}):")
                for row in board:
                    print(' | '.join(row))

                diem = minimax(board, False)
                board[i][j] = ' '

                print(f"Điểm = {diem}\n")

                if diem > diem_tot_nhat:
                    diem_tot_nhat = diem
                    nuoc_tot_nhat = (i, j)

    dong, cot = nuoc_tot_nhat
    board[dong][cot] = MAY

    print(f"Nước đi tốt nhất cho X: ({dong}, {cot})")
    print(f"Điểm của nước đi: {diem_tot_nhat}")
    print("Bàn cờ sau khi đi:")

    for row in board:
        print(' | '.join(row))


if __name__ == "__main__":
    bai_minimax()
