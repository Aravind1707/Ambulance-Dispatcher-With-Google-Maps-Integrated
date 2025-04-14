import sqlite3

def get_all_ambulances():
    conn = sqlite3.connect('app/database/ambulance.db')
    cur = conn.cursor()
    cur.execute("SELECT id, latitude, longitude FROM ambulances WHERE status = 'available'")
    ambulances = [{"id": row[0], "location": [row[1], row[2]]} for row in cur.fetchall()]
    conn.close()
    return ambulances

def dispatch_ambulance(location):
    ambulances = get_all_ambulances()

    def distance(loc1, loc2):
        return ((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2) ** 0.5

    if not ambulances:
        return {"id": "N/A", "location": [0, 0]}

    closest = min(ambulances, key=lambda amb: distance(amb["location"], location))
    return closest
