from flask import Blueprint, render_template, request, redirect, url_for
import sqlite3

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
def admin_home():
    return render_template('admin.html')

@admin_bp.route('/register', methods=['POST'])
def register_ambulance():
    lat = request.form['latitude']
    lon = request.form['longitude']
    status = request.form.get('status', 'available')

    conn = sqlite3.connect('app/database/ambulance.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO ambulances (latitude, longitude, status) VALUES (?, ?, ?)", (lat, lon, status))
    conn.commit()
    conn.close()
    return redirect(url_for('admin.admin_home'))
