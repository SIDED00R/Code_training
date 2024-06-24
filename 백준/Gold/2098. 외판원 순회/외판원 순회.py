def tsp(graph):
    n = len(graph)
    dp = [[None] * (1 << n) for _ in range(n)]
    
    def visit(city, visited):
        if visited == (1 << n) - 1:
            return graph[city][0] or float('inf')
        
        if dp[city][visited] is not None:
            return dp[city][visited]
        
        min_cost = float('inf')
        for next_city in range(n):
            if not visited & (1 << next_city):
                cost = graph[city][next_city] + visit(next_city, visited | (1 << next_city))
                min_cost = min(min_cost, cost)
        
        dp[city][visited] = min_cost
        return dp[city][visited]
    
    return visit(0, 1 << 0)

n = int(input())
graph = []
for _ in range(n):
    line = []
    for num in list(map(int, input().split())):
        if num == 0:
            line.append(float('inf'))
        else:
            line.append(num)
    graph.append(line)

print(tsp(graph))