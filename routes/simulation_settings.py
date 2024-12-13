from flask import Blueprint, jsonify, request
from models import SimulationSettings

# Create a blueprint
simulation_settings_bp = Blueprint('simulation_settings', __name__)

@simulation_settings_bp.route('/simulation_settings', methods=['GET', 'POST'])
def simulation_settings():
    if request.method == 'POST':
        data = request.json
        settings = SimulationSettings.query.first()
        settings.inflation_rate = data.get('inflation_rate', settings.inflation_rate)
        settings.min_wage = data.get('min_wage', settings.min_wage)
        settings.ebc_rate = data.get('ebc_rate', settings.ebc_rate)
        db.session.commit()
        return jsonify({'status': 'Settings updated'})
    else:
        settings = SimulationSettings.query.first()
        return jsonify({
            'inflation_rate': settings.inflation_rate,
            'min_wage': settings.min_wage,
            'ebc_rate': settings.ebc_rate,
        })
