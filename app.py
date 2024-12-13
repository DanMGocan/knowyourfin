from flask import Flask, render_template, jsonify
import sqlite3

# Import blueprints and routes
from routes.simulation_settings import simulation_settings_bp
from routes.create_population import create_population_bp


app = Flask(__name__)

# Register blueprints
app.register_blueprint(simulation_settings_bp)
app.register_blueprint(create_population_bp)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
