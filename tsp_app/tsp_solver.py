from itertools import permutations

def calculate_route_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    total_distance += distance_matrix[route[-1]][route[0]]
    return total_distance

def tsp_brute_force(distance_matrix):
    n = len(distance_matrix)
    shortest_route = None
    min_distance = float('inf')
    
    for perm in permutations(range(n)):
        current_distance = calculate_route_distance(perm, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_route = perm
    
    return shortest_route, min_distance
