def get_hospitals():
    return [
        {"name": "City Hospital", "location": (1, 2)},
        {"name": "Metro Hospital", "location": (5, 5)},
    ]

def get_ambulances():
    return [
        {"id": 1, "location": (2, 3), "status": "available"},
        {"id": 2, "location": (6, 1), "status": "available"},
        {"id": 3, "location": (7, 8), "status": "busy"},
    ]