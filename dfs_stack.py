N = int(input())
adjList = [[] for i in range(N)]
visited = [False for i in range(N)]
stack = [0]

for i in range(N):
    adjList[i] = list(map(int, input().split()))[::-1]

while len(stack ) != 0:
    head = stack.pop()
    print(head, end = ' ')
    visited[head] = True

    for i in range(len(adjList[head])):
        if not visited[adjList[head][i]]:
            stack.append(adjList[head][i])
