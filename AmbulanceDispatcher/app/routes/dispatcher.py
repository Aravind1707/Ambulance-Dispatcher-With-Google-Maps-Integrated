from flask import Blueprint, render_template, request, jsonify
import random
import time

# Import the dispatch logic for the ambulance
from app.algorithms.dispatcher_logic import dispatch_ambulance

dispatcher_bp = Blueprint('dispatcher', __name__)

# Dummy ambulance data (You can replace it with actual database or simulation logic)
ambulances = [
    {'id': 1, 'location': [19.0760, 72.8777], 'status': 'available'},  # Example coordinates (Mumbai)
    {'id': 2, 'location': [28.7041, 77.1025], 'status': 'on-trip'},    # Example coordinates (Delhi)
    {'id': 3, 'location': [13.0827, 80.2707], 'status': 'available'},  # Example coordinates (Chennai)
]

# The main index route for showing the dispatch page
@dispatcher_bp.route('/')
def index():
    return render_template('index.html')

# Route to dispatch an ambulance based on the patient's location
@dispatcher_bp.route('/dispatch', methods=['POST'])
def dispatch():
    data = request.get_json()
    location = data.get('location', [0, 0])

    # Use the dispatch logic to find the closest ambulance
    ambulance = dispatch_ambulance(location)

    return jsonify({'assigned_ambulance': ambulance})

# Route to simulate ambulance location updates every 5 seconds
@dispatcher_bp.route('/update_location', methods=['GET'])
def update_location():
    # Here we simulate movement by slightly changing the ambulance's location
    # You can replace this logic with actual GPS tracking or real-time updates
    ambulance = random.choice(ambulances)

    # Simulate movement (adjusting coordinates)
    new_lat = ambulance['location'][0] + random.uniform(-0.001, 0.001)
    new_lng = ambulance['location'][1] + random.uniform(-0.001, 0.001)

    ambulance['location'] = [new_lat, new_lng]
    ambulance['status'] = 'on-trip' if ambulance['status'] == 'available' else 'available'

    return jsonify({'latitude': ambulance['location'][0], 'longitude': ambulance['location'][1]})

# Sample dispatcher logic (can be expanded)
def dispatch_ambulance(patient_location):
    # Calculate distance from the patient to each ambulance and select the closest one
    closest_ambulance = None
    min_distance = float('inf')

    for ambulance in ambulances:
        distance = calculate_distance(patient_location, ambulance['location'])
        if distance < min_distance:
            closest_ambulance = ambulance
            min_distance = distance

    return closest_ambulance

# A basic function to calculate Euclidean distance (you can replace this with a real distance formula)
def calculate_distance(loc1, loc2):
    lat1, lon1 = loc1
    lat2, lon2 = loc2

    # Haversine formula for more accurate distance calculation (optional, depending on precision needs)
    from math import radians, sin, cos, sqrt, atan2

    R = 6371.0  # Radius of the Earth in kilometers
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c  # Result in kilometers
    return distance
