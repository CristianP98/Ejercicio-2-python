from django.shortcuts import render
from .tsp_solver import tsp_brute_force
import json

def home(request):
    context = {}
    if request.method == 'POST':
        # Procesar entrada del usuario
        locations = json.loads(request.POST['locations'])
        
        # Crear una matriz de distancias entre ubicaciones
        num_locations = len(locations)
        distance_matrix = [[0] * num_locations for _ in range(num_locations)]
        
        for i in range(num_locations):
            for j in range(num_locations):
                if i != j:
                    distance_matrix[i][j] = calculate_distance(locations[i], locations[j])
        
        # Resolver TSP
        shortest_route_indices, min_distance = tsp_brute_force(distance_matrix)
        shortest_route = [locations[i] for i in shortest_route_indices]
        
        context['shortest_route'] = json.dumps(shortest_route)
        context['min_distance'] = min_distance

    return render(request, 'tsp_app/home.html', context)

def haversine(lon1, lat1, lon2, lat2):
    import math
    # Radio de la Tierra en kilómetros
    R = 6371.0
    
    # Convertir grados a radianes
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    
    # Diferencias
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    # Fórmula de Haversine
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.asin(math.sqrt(a))
    
    return R * c

def calculate_distance(loc1, loc2):
    return haversine(loc1['lng'], loc1['lat'], loc2['lng'], loc2['lat'])
