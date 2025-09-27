# קוד זה פותר לוח סודוקו ריק. ניתן לשנות את הלוח לדוגמה עם מספרים אחרים כדי לבדוק פתרונות שונים.
# הקוד משתמש באלגוריתם חזרה לאחור (backtracking) כדי למצוא פתרון חוקי לסודוקו.
# הקוד עובר על התאים בלוח בדורה לינארים משמאל לימין ומלעלה למעטה ומחפש תא ריק (0).
# כאשר הוא מוצא תא ריק, הוא מנסה למלא אותו עם מספרים מ-1 עד 9 ובודק אם המספר חוקי לפי כללי הסודוקו.
# אם המספר חוקי, הוא ממשיך לתא הבא. (כל זה בענף הרקורסי של התא הנוכחי)
# אם הוא מגיע למצב שבו לא ניתן למלא את התא הנוכחי עם אף מספר חוקי, הוא חוזר לתא הקודם ומנסה מספר אחר שם (נסיגה).
# התהליך נמשך עד שהלוח מתמלא לחלוטין או שאין פתרון חוקי.



def print_board(board):
    for i in range(9):
        row = ""
        for j in range(9):
            row += str(board[i][j]) + " "
            if (j + 1) % 3 == 0 and j != 8:
                row += "| "
        print(row)
        if (i + 1) % 3 == 0 and i != 8:
            print("- - - + - - - + - - -")

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:  # 0 = ריבוע ריק
                return i, j
    return None

def valid(board, num, pos):
    row, col = pos

    # בדיקה בשורה
    if num in board[row]:
        return False

    # בדיקה בעמודה
    for i in range(9):
        if board[i][col] == num:
            return False

    # בדיקה בריבוע 3x3
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True  # נפתר
    row, col = find

    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num

            if solve(board):
                return True

            board[row][col] = 0  # נסיגה

    return False


# דוגמה ללוח (0 = ריבוע ריק)
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

print("לוח לפני:")
print_board(board)
solve(board)
print("\nלוח אחרי:")
print_board(board)

