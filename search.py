dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]


# def dfs(board, i, j, current, visited_list, word, row, col):
#     if is_stop(visited_list, row, col) or i < 0 or i >= row or j < 0 or j >= col or visited_list[i][j]:
#         return False
#
#     word_len = len(word)
#     if current == word_len:
#         print(visited_list)
#         return True
#
#     if board[i][j] == word[current]:
#         print(board[i][j],word[current],i,j)
#         visited_list[i][j] = True
#         current += 1
#         print(visited_list)
#
#     else:
#         return False
#
#     left = j - 1
#     right = j + 1
#     up = i - 1
#     down = i + 1
#     flag = False
#
#     flag = dfs(board, i, left, current,visited_list,word,row,col) or dfs(board, i, right, current, visited_list, word, row, col) or dfs(board, up, j, current,visited_list,word,row,col) or dfs(board, down, j, current, visited_list, word, row, col)
#     visited_list[i][j] = False
#     print(word[current-1], i, j)
#     print(visited_list)
#     return flag


def dfs(board, i, j, visited_list, word, row, col, current_num):
    if is_stop(visited_list, row, col):
        return False

    visited_list[i][j] = True
    flag = False
    word_len = len(word)

    if current_num == word_len-1:
        return True

    for m in range(4):
        x = i + dirs[m][0]
        y = j + dirs[m][1]
        print(x,y,current_num)

        if x>=0 and y>=0 and x<row and y<col and current_num+1<word_len and board[x][y]==word[current_num+1] and visited_list[x][y]!=True :
            print(x, y, board[x][y], word[current_num+1])
            flag = dfs(board, x, y, visited_list, word, row, col, current_num+1)
        if flag:
            break

    visited_list[i][j] = False
    return flag


def is_stop(visited_list, row, col):
    for i in range(row):
        for j in range(col):
            if visited_list[i][j] == False:
                return False
    return True


def dfs1(matrix, last_number, i, j, path_length, visited_list, row, col):
    if is_stop(visited_list, row, col) or i < 0 or i >= row or j < 0 or j >= col or visited_list[i][j]:
        # print(visited_list)
        return path_length[1]


    if last_number < matrix[i][j]:
        path_length[0] += 1
        if path_length[1] < path_length[0]:
            path_length[1] = path_length[0]
        # print(last_number, matrix[i][j],path_length[0])
        visited_list[i][j] = True
    else:
        # print("max：",path_length[0])
        return path_length[0]

    left = j - 1
    right = j + 1
    up = i - 1
    down = i + 1

    # print(visited_list)

    dfs1(matrix, matrix[i][j], i, left, path_length, visited_list, row, col),
    dfs1(matrix, matrix[i][j], i, right, path_length, visited_list, row, col),
    dfs1(matrix, matrix[i][j], up, j, path_length, visited_list, row, col),
    dfs1(matrix, matrix[i][j], down, j, path_length, visited_list, row, col)


    visited_list[i][j] = False
    path_length[0] -= 1

    return path_length[1]


def longestIncreasingPath(matrix):
    row = len(matrix)
    col = len(matrix[0])

    visited_list = [[False] * col for i in range(row)]
    dp = [[-1] * col for i in range(row)]
    max_path_length = 0
    for i in range(row):
        for j in range(col):
            # print(i,j)
            current_path_length = dfs2(matrix,i,j,row,col,dp)
            if current_path_length > max_path_length:
                max_path_length = current_path_length
    return max_path_length



def dfs2(matrix,i,j,row,col,dp):
    path_length = 0
    for m in range(4):
        x = i + dirs[m][0]
        y = j + dirs[m][1]


        if x >= 0 and x< row and y >=0 and y <col and matrix[x][y] > matrix[i][j]:
            if dp[x][y]>=0:
                path_length = max(dp[x][y], path_length)

            else:
                path_length = max(dfs2(matrix, x, y, row, col,dp),path_length)

    path_length += 1

    dp[i][j] = path_length

    return path_length


def exist(board, i, j, visited_list, word, row, col,current):
    for i in range(row):
        for j in range(col):
            print("now",i,j)
            # board, i, j, visited_list, word, row, col, current_num
            if board[i][j]==word[0] and dfs(board, i, j, visited_list, word, row, col,current):
                return True
    return False


def bfs(maze,start,end,queue:list,current):
    print(current)
    if current == start:
        queue.append(start)
    if current == end:
        return True

    if len(queue) == 0:
        return False


    for i in range(len(maze[current])):
        if maze[current][i] == 1:
            print(i)
            queue.append(i)
            queue

    print(queue)
    for i in range(len(queue)):
        bfs(maze,start,end,queue,queue[-1])



if __name__ == '__main__':
    # board = [
    #     ['A', 'B', 'C', 'E'],
    #     ['S', 'F', 'C', 'S'],
    #     ['A', 'D', 'E', 'E']
    # ]
    #
    # visited_list = [[False]*4 for i in range(3)]
    # board, i, j, visited_list, word, row, col, current_num
    # print(exist(board, 0, 0, visited_list, "ABCF", 3, 4, 0))


    #
    # nums = [
    #     [7, 7, 5],
    #     [2, 4, 6],
    #     [8, 2, 0]
    # ]
    # print(longestIncreasingPath(nums))
    maze= [
        [0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0]
    ]

    print(bfs(maze,0,2,[],0))





