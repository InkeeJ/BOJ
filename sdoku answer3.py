# 예전에 만든 코드의 간소화 버전. read/write file 등 필요 없는 코드가 포함되어 있음. 

from copy import deepcopy
from functools import reduce

def main(way=True, dg=False):
    start_board = [list(map(int, input().split())) for i in range(9)]
    start_bp, excp = initialize(start_board)
    if start_bp is None:
        string = "The given sudoku contains an error. \nPlease check '{}' on row {}, column {}. ".format(excp[2], excp[0], excp[1])
        if dg: print(string)
        write_except_file("Answer", string)
    else:
        answer = rec_func(start_bp, way, 0, dg)
        if answer is None:
            string = "No answer to the sudoku was found. "
            if dg: print(string)
            write_except_file("Answer", string)
        else:
            for i in range(9):
                print(' '.join(map(str,answer[i])))

def rec_func(start_bp, way, depth, dg):
    deadend, dend_type, dend_pos, dend_factor = stabilize_and_check_deadend(start_bp, way, dg, depth)
    done = check_whether_done(start_bp)
    if done:
        if dg: print_state(None, None, None, depth, 10, "simple")
        return deepcopy(start_bp[0])
    elif deadend:
        if dg: 
            if dend_type == 0: print_state(dend_pos//9, dend_pos%9, None, depth, 6, "format")
            else: print_state(dend_factor, dend_pos, None, depth, dend_type + 6, "format")
        return None
    else:
        i, j = find_min_blank(start_bp)
        for assume in range_object(way):
            if start_bp[1][i][j][assume-1]:
                new_bp = deepcopy(start_bp)
                delete_possibility(new_bp, i, j, assume, dg, depth, 0)
                returned_value = rec_func(new_bp, way, depth + 1, dg)
                if returned_value is not None:
                    if dg: print_state(None, None, None, depth, 11, "simple")
                    return returned_value
        if dg: print_state(None, None, None, depth, 5, "simple")
        return None

def stabilize_and_check_deadend(bp, way, dg, depth):
    board, possible = bp[0], bp[1]
    filled = False
    while not filled:
        filled = True
        for t in range(81):
            deadend, found_fill = sub_stabilize(bp, None, None, (t//9, t%9), (lambda x, y: x[0]), (lambda x, y: x[1]), (lambda x, y: y+1), False, dg, depth, 1)
            if deadend: return True, 0, t, None
            elif found_fill: filled = False
        for assume in range_object(way):
            for i in range(9):
                sublist = [(i, k) for k in range(9)]
                deadend, found_fill = sub_stabilize(bp, sublist, assume, i, lambda x, y: x, lambda x, y: y, lambda x, y: x, True, dg, depth, 2)
                if deadend: return True, 1, i, assume
                elif found_fill: filled = False
            for j in range(9):
                sublist = [(k, j) for k in range(9)]
                deadend, found_fill = sub_stabilize(bp, sublist, assume, j, lambda x, y: y, lambda x, y: x, lambda x, y: x, True, dg, depth, 3)
                if deadend: return True, 2, j, assume
                elif found_fill: filled = False
            for t in range(9):
                sublist = [((t//3)*3 + a, (t%3)*3 + b) for a in range(3) for b in range(3)]
                deadend, found_fill = sub_stabilize(bp, sublist, assume, t, lambda x, y: ((x//3)*3 + y//3), lambda x, y: ((x%3)*3 + y%3), lambda x, y: x, True, dg, depth, 4)
                if deadend: return True, 3, t, assume
                elif found_fill: filled = False
    return False, None, None, None # not deadend

def sub_stabilize(bp, sublist, assume, value, l_func1, l_func2, l_func3, filltype, dg, depth, showstring):
    board, possible = bp[0], bp[1]
    if filltype: condition = (assume not in [board[x][y] for x, y in sublist])
    else: condition = (board[value[0]][value[1]] == 0)
    if condition:
        if filltype: L = [possible[x][y][assume-1] for x, y in sublist]
        else: L = possible[value[0]][value[1]]
        num = L.count(True)
        if num == 0:
            return True, None # deadend
        elif num == 1:
            L_index = L.index(True)
            delete_possibility(bp, l_func1(value, L_index), l_func2(value, L_index), l_func3(assume, L_index), dg, depth, showstring)
            return False, True # not deadend, found place to fill
    return False, False # not deadend, not found place to fill

def delete_possibility(bp, i, j, assume, dg, depth, showstring):
    if dg: print_state(i, j, assume, depth, showstring, "delete_possibility")
    board, possible = bp[0], bp[1]
    board[i][j] = assume
    for j_t in range(9):
        possible[i][j_t][assume-1] = False
    for i_t in range(9):
        possible[i_t][j][assume-1] = False
    i3, j3 = (i//3)*3, (j//3)*3
    for b in range(3):
        for a in range(3):
            possible[i3 + a][j3 + b][assume-1] = False
    possible[i][j] = [False]*9

def print_state(i, j, assume, depth, showstring, state_type):
    message_list = ["Guessed the number. ",
                    "The number is the only possible one in the blank. ", 
                    "The number has a single position available in the row. ", 
                    "The number has a single position available in the column. ", 
                    "The number has a single position available in the 3×3 square. ", 
                    "No answer from guessing this blank was found. Therefore, we go backwards and guess. ", 
                    "row {}, column {}. ",
                    "row {}. ",
                    "column {}. ",
                    "3×3 square of position {}. ", 
                    "Answer to the sudoku is found. No more steps are needed. ", 
                    "Answer to the sudoku is already found. "]
    if state_type == "delete_possibility": string = "Placed '{}' on row {}, column {}: ".format(assume, i, j) + message_list[showstring]
    if state_type == "simple": string = message_list[showstring]
    if state_type == "format": 
        if showstring == 6: string = ("This is a deadend because no number can be placed on " + message_list[showstring]).format(i, j)
        else: string = ("This is a deadend because the number '{}' cannot be placed in the " + message_list[showstring]).format(i, j)            
    print('| '*depth + string)

def check_whether_done(bp):
    board = bp[0]
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True

def find_min_blank(bp):
    possible = bp[1]
    for t in range(9):
        up_c, le_c = t//3, t%3
        for delta in range(9):
            delta_x, delta_y = delta//3, delta%3
            real_x, real_y = (up_c + delta_y)%3, (le_c + delta_x)%3
            i, j = 3*delta_x + real_x, 3*delta_y + real_y
            if True in possible[i][j]:
                return i, j
    return -1, -1

def initialize(board):
    possible = []
    for k1 in range(9):
        possible.append([])
        for k2 in range(9):
            possible[k1].append([True]*9)
    bp = [board, possible]
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                if possible[i][j][board[i][j]-1]:
                    delete_possibility(bp, i, j, board[i][j], False, None, None)
                else:
                    return None, [i, j, board[i][j]]
    return bp, []

def sudoku_list_to_string(board):
    temp = list(map(lambda L: ''.join(map(str, L)), board))
    return '\n'.join(temp)

def possible_list_to_string(possible, assume):
    temp = ''
    for x1 in range(9):
        for x2 in range(9):
            temp += (str(possible[x1][x2][assume-1]) + ' ').ljust(6)
        temp = temp[:-1]
        temp += '\n'
    return temp

def read_sudoku_file(filename):
    board = []
    for k in range(9):
        board.append([-1]*9)
    file = open('{}.txt'.format(filename), 'r')
    for i in range(9):
        line = file.readline()
        for j in range(9):
            board[i][j] = int(line[j])
    file.close()
    return board

def write_sudoku_file(filename, board):
    file = open('{}.txt'.format(filename), 'w')
    string = sudoku_list_to_string(board)
    file.write(string)
    file.close()

def write_except_file(filename, string):
    file = open('{}.txt'.format(filename), 'w')
    file.write(string)
    file.close()

def range_object(way):
    if way:
        return range(1, 10)
    return range(9, 0, -1)

main(way = True, dg = False)