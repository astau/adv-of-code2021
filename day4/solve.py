def main():
    numbers, boards = parse_file("data.txt")
    
    winning_boards = {} 
    for i in range(len(numbers)):
        for key in boards:
            if not key in winning_boards:
                x, y = mark_board(boards[key], numbers[i])
                if x != None:
                    if check_board(boards[key], x, y):
                        winning_boards[key] = (i, key, numbers[i], board_score(boards[key], numbers[i]))

    win_keys = list(winning_boards.keys())
    print(f"Answer 1: {winning_boards[win_keys[0]][3]}") # 35670
    print(f"Answer 2: {winning_boards[win_keys[-1]][3]}") # 22704

def board_score(board, num):
    sum = 0
    for k in board:
        if board[k][1] == 1:
            sum += board[k][0]
    return sum * num

def mark_board(board, num):
    for key in board:
        if board[key][0] == num:
            board[key][1] = 0
            return key[0], key[1]
    return None, None

def check_board(board, x, y):
    x_sum = y_sum = 0
    for i in range(5):
        x_sum += board[(x, i)][1]
        y_sum += board[(i, y)][1]    
    return True if x_sum == 0 or y_sum == 0 else False

def parse_file(fname):    
    with open(fname, "r") as file:
        data = file.read().split('\n')
        numbers = [int(x) for x in data.pop(0).split(',')]
        data.pop(0) # empty line
        
        boards = {}
        for i in range(0, len(data), 6):
            board = {}
            for x, row in enumerate(data[i:i+5]):
                for y, num in enumerate(row.split()):
                    board[(x, y)] = [int(num), 1]
            boards[int(i/6)] = board
    return numbers, boards

if __name__ == "__main__":
    main()