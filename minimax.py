from sys import maxsize


def get_state(b):
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2]:
            if b[i][0] == 'x':
                return -1
            if b[i][0] == 'o':
                return 1
        if b[0][i] == b[1][i] == b[2][i]:
            if b[0][i] == 'x':
                return -1
            if b[0][i] == 'o':
                return 1
    if b[0][0] == b[1][1] == b[2][2]:
        if b[0][0] == 'o':
            return 1
        if b[0][0] == 'x':
            return -1
    if b[2][0] == b[1][1] == b[0][2]:
        if b[2][0] == 'o':
            return 1
        if b[2][0] == 'x':
            return -1
    if get_moves(b) is None:
        return 0
    return None


def get_moves(b):
    ls = []
    for i in range(3):
        for j in range(3):
            if b[i][j] == '-':
                ls.append((i, j))
    return ls if len(ls) > 0 else None


def minimax(b, depth, is_maximizing):
    state = get_state(b)
    if state is not None:
        return state

    if is_maximizing:
        moves = get_moves(b)
        best_score = -maxsize
        for move_ in moves:
            b[move_[0]][move_[1]] = 'o'
            score = minimax(b, depth + 1, False)
            b[move_[0]][move_[1]] = '-'
            best_score = max(score, best_score)
        return best_score
    else:
        moves = get_moves(b)
        best_score = maxsize
        for move_ in moves:
            b[move_[0]][move_[1]] = 'x'
            score = minimax(b, depth + 1, True)
            b[move_[0]][move_[1]] = '-'
            best_score = min(score, best_score)
        return best_score


def best_move(b):
    max_eval = -maxsize
    b_move = None, None
    available_moves = get_moves(b)
    try:
        for move_ in available_moves:
            b[move_[0]][move_[1]] = 'o'
            ev = minimax(b, 0, False)
            b[move_[0]][move_[1]] = '-'
            if max_eval < ev:
                b_move = move_
                max_eval = ev
    except TypeError:
        return None
    return b_move

