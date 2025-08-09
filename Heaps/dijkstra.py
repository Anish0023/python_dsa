import heapq
def dijkstra(self, graph, start):

    # Initialize distances with infinity and set the start node distance to 0
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Priority queue to hold nodes to explore, initialized with the start node
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Nodes can only be added once to the priority queue, so we skip if we find a longer path
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Only consider this new path if it's better
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances