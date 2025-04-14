from flask import Flask
from app.routes.dispatcher import dispatcher_bp
from app.routes.admin import admin_bp
import os

# 💡 Explicit path to templates
template_path = os.path.join(os.path.dirname(__file__), 'app', 'templates')
app = Flask(__name__, template_folder=template_path)

# Register the blueprint
app.register_blueprint(dispatcher_bp)
app.register_blueprint(admin_bp)

if __name__ == '__main__':
    app.run(debug=True)