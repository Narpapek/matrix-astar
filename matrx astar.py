import heapq

def ArrayToGraph(array):
    n = len(array) 
    m = len(array[0])
    graph = {} 

    for i in range(n):
        for j in range(m):
            graph[(i, j)] = {
                "value": array[i][j],
                "neighbors": {},   
            } ## номера ячейки и всех её соседей

    for i in range(n):
        for j in range(m):
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < m:
                    graph[(i, j)]["neighbors"][(ni, nj)] = array[ni][nj] # алг следит, чтобы соседи не переходили границу матрицы и вслучае положительного результата, записывает стоимость перехода и координату соседа

    return graph

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
def reconstruct_path(nestPos, endPos):
    if endPos not in nestPos:
        return None
    path = []
    cur = endPos
    while cur is not None:
        path.append(cur)
        cur = nestPos[cur]
    path.reverse()
    return path
def Astar(graph, startPos, endPos):
    cost = {startPos: 0}            
    nestPos = {startPos: None} 
    pq = [(manhattan_distance(startPos, endPos), startPos)]

    while pq:
        curCost, curPos = heapq.heappop(pq)

        if curPos == endPos:
            break

        if curCost > cost[curPos] + manhattan_distance(curPos, endPos):
            continue

        for neighbor in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = curPos[0] + neighbor[0], curPos[1] + neighbor[1]

            if (x, y) not in graph:
                continue


            weight = graph[(x, y)]["value"]
            newCost = cost[curPos] + weight

            if newCost < cost.get((x, y), float("inf")):
                cost[(x, y)] = newCost
                nestPos[(x, y)] = curPos
                f = newCost + manhattan_distance((x, y), endPos)
                heapq.heappush(pq, (f, (x, y)))

    return cost, nestPos

def userInput():
    return input().strip().split()

mapArr = [
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5],
    [1,2,3,4,5]
]

graph = ArrayToGraph(mapArr)


for row in mapArr:
    print(row)

startPointCord = tuple(map(int, userInput()))
endPointCord = tuple(map(int, userInput()))

cost, parent = Astar(graph, startPointCord, endPointCord)

if endPointCord in cost:
    print("Стоимость:", cost[endPointCord])
    print("Путь:", reconstruct_path(parent, endPointCord))
else:
    print("Путь не найден")