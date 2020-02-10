# edges表示邻接矩阵
edges = [[0, 1, 12, -1, -1, -1],
         [-1, 0, 9, 3, -1, -1],
         [-1, -1, 0, -1, 5, -1],
         [-1, -1, 4, 0, 13, 15],
         [-1, -1, -1, -1, 0, 4],
         [-1, -1, -1, -1, -1, 0]]
dis = {2: 1, 3: 12, 4: -1, 5: -1, 6: -1}

visited = []

def dijkstra():
    min_dis = float("inf")
    min_pos = 3
    while len(visited) < 5:
        for pos, distance in dis.items():
            if distance > 0 and pos not in visited and distance < min_dis:
                min_dis = distance
                min_pos = pos
                # print("min",min_pos)

        visited.append(min_pos)


        for pos, distance in dis.items():
            if pos not in visited and edges[min_pos-1][pos-1]!=-1 and (dis[pos] == -1 or (min_dis + edges[min_pos-1][pos-1]) < dis[pos]):
                dis[pos] = min_dis + edges[min_pos-1][pos-1]

        print(min_pos)
        print(dis)

        min_dis = float("inf")
        min_pos = min_pos + 1

    return dis


if __name__ == '__main__':
    print(dijkstra())





