import math

def calculate_distance(loc1, loc2):
    return math.sqrt((loc1[0]-loc2[0])**2 + (loc1[1]-loc2[1])**2)

def assign_nearest_ambulance(request_location, ambulances):
    nearest = None
    min_distance = float('inf')

    for amb in ambulances:
        if amb['status'] == 'available':
            distance = calculate_distance(request_location, amb['location'])
            if distance < min_distance:
                min_distance = distance
                nearest = amb

    if nearest:
        nearest['status'] = 'assigned'
    return nearest if nearest else {"message": "No ambulances available"}
