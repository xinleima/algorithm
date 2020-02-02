
def dfs(board, i, j, current,visited_list, word, row,col):
    word_len = len(word)
    if current == word_len:
        print(visited_list)
        return True

    if is_stop(visited_list,row,col):
        return False

    if board[i][j] == word[current]:
        print(board[i][j],word[current],i,j)
        visited_list[i][j] = True
        current +=1

    else:
        return False

    left = j - 1
    right = j + 1
    up = i - 1
    down = i + 1

    if left >= 0 and visited_list[i][left] == False and dfs(board, i, left, current,visited_list,word,row,col):
        return True

    if right < col and visited_list[i][right] == False and dfs(board, i, right, current, visited_list, word, row, col):
        return True

    if up >= 0 and visited_list[up][j]== False and dfs(board, up, j, current,visited_list,word,row,col):
        return True

    if down < row and visited_list[down][j]== False and dfs(board, down, j, current, visited_list, word, row, col):
        return True

    return False


def is_stop(visited_list,row, col):
    for i in range(0,row):
        for j in range(0,col):
            if visited_list[i][j] == False:
                return False
    return True



def exist(board, i, j, current, visited_list, word, row, col):
    for i in range(0, row):
        for j in range(0, col):
            if dfs(board, i, j, current, visited_list, word, row, col):
                return True


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    visited_list = [[False]*4 for i in range(3)]


    print(exist(board, 0, 0, 0, visited_list, "ABCB",3,4))

