import heapq

def dijkstra(graph, start):
    # Inisialisasi jarak awal dengan tak terhingga, kecuali start (0)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue untuk memilih node dengan jarak terkecil
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak yang diambil lebih besar, lewati
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Contoh graf berbobot
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances = dijkstra(graph, start_node)
print("Jarak terpendek dari node", start_node, ":", distances)
